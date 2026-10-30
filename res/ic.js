resources.push(...[
['hdlbits','HDLBits','https://hdlbits.01xz.net/wiki/Main_Page','入门 · 从组合逻辑、时序逻辑到状态机，在线编写 Verilog 并通过仿真反馈检查 RTL。',['Verilog','RTL 练习','英文']],
['chipverify','ChipVerify','https://www.chipverify.com/','入门到进阶 · 按专题学习 Verilog、SystemVerilog 和 UVM，配合示例理解语法与验证。',['SystemVerilog','UVM','英文']],
['verification-academy','Verification Academy','https://verificationacademy.com/','验证进阶 · Siemens 的功能验证课程、UVM Cookbook 与覆盖率资料；部分内容需注册。',['验证方法学','覆盖率','英文']],
['ysyx','一生一芯','https://ysyx.oscc.cc/','项目实践 · 跟随中文讲义学习处理器与 SoC 设计、软硬件协同，适合长期项目实践。',['处理器设计','SoC','中文']],
['mit-digital','MIT 6.004 · Computation Structures','https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/','基础课程 · 从数字逻辑到处理器与计算机系统，配合课程讲义和实验建立硬件设计基础。',['数字逻辑','体系结构','英文']],
['eda-playground','EDA Playground','https://www.edaplayground.com/','实践工具 · 在浏览器编写和仿真 Verilog / SystemVerilog，练习 Testbench；工具权限以账号为准。',['在线仿真','Testbench','英文']],
['yosys','Yosys 官方文档','https://yosyshq.readthedocs.io/projects/yosys/en/latest/','综合进阶 · 学习开源 RTL 综合工具的流程、优化与脚本，理解 RTL 如何转化为网表。',['逻辑综合','RTL → 网表','英文']],
['openroad','OpenROAD 官方文档','https://openroad.readthedocs.io/en/latest/main/README.html','后端进阶 · 学习开源数字芯片物理设计工具，探索布局、时钟树与布线等实现步骤。',['物理设计','布局布线','英文']]
].map(([id,name,url,desc,tags])=>({id,name,url,desc,tags,cat:'ic',icon:'IC',bg:'#e6f1e6',fg:'#4d8250'})));
