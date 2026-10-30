FROM python:3.10-slim

WORKDIR /app

# 安装 fastapi 和 uvicorn
RUN pip install --no-cache-dir fastapi uvicorn pydantic pymysql

# 将代码拷入容器
COPY test.py .

EXPOSE 8000

# 启动命令
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000","--reload","--reload-dir","/app"]