import os
import pymysql
from pymysql.cursors import DictCursor
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
import uvicorn
from typing import Annotated

app = FastAPI()

# ----------------- 1. 数据模型 -----------------
class UserData(BaseModel):
    user_id: int = Field(ge=1, le=120, description="用户唯一id")
    username: str = Field(default="bob", min_length=2, max_length=20, description="用户名称")

# ----------------- 2. 数据库配置 -----------------
# 优先从环境变量读取（容器化部署的标准做法），本地测试时默认回退到 127.0.0.1
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),   # 在 Docker Compose 里环境变量会设为 "db"
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "123456"),
    "database": os.getenv("DB_NAME", "test_db"),
    "cursorclass": DictCursor  # 让查询结果返回 dict 字典格式，方便转成 JSON
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


# ----------------- 3. 依赖项：管理数据库连接生命周期 -----------------
def get_db():
    conn = pymysql.connect(**DB_CONFIG)
    try:
        yield conn  # 把连接借给接口使用
    finally:
        conn.close()  # 接口响应完成后，自动安全关闭连接

# ----------------- 4. 业务接口 -----------------
# 注意：这里用普通 def，不要用 async def，FastAPI 会自动开启线程池防卡顿
@app.get("/api/get_user_data/", response_model=UserData)
def get_user_data(user_id: int, db: pymysql.Connection = Depends(get_db)):
    with db.cursor() as cursor:
        # 使用参数化查询（%s），防止 SQL 注入！不要自己用 f-string 拼接
        sql = "SELECT id AS user_id, username FROM users WHERE id = %s"
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()

    # 查不到数据返回 404
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"未找到 ID 为 {user_id} 的用户"
        )

    return result

# ----------------- 5. 启动入口 -----------------
if __name__ == "__main__":
    uvicorn.run()

