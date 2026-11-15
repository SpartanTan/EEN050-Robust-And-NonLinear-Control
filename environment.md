# 环境和运行说明

[返回主线](../robust_nonlinear_control_learning_plan.md)

MATLAB 为原生作业主路线，Python 做补充。课程设计不需要先安装所有软件；R0 用检查脚本决定当前能运行哪些任务。

## MATLAB

在课程根目录运行：

~~~matlab
run('self_study/tools/check_environment.m')
~~~

- Control System Toolbox：状态空间、响应、LQR/LQI、Gramian 等基础操作。
- Robust Control Toolbox：原生 F‑16 的 h2syn/hinfsyn、不确定对象与鲁棒分析；这是完整复现 A2/A3 的主要依赖。
- YALMIP 加可用 SDP 求解器：Exercise 5.3 等 LMI 任务。YALMIP 是建模层，不自带所有求解器；官方 [安装说明](https://yalmip.github.io/tutorial/installation/) 与 [半正定教程](https://yalmip.github.io/tutorial/semidefiniteprogramming/)。
- 非线性作业主要使用基础 MATLAB 的 ode45、绘图和矩阵计算；符号工具可选，不作为推导前提。

本次没有运行 MATLAB、查询许可证或替你安装工具箱。检查脚本中的 which 仅检查函数是否在路径上，不保证许可证/求解器可用。做一例已知可行的 Lyapunov 问题，另做一个不可行例，检查求解状态与余量。

[exercise_5_3_checked.m](tools/exercise_5_3_checked.m) 是带诊断的自学模板，不是声称原参数域可稳定的答案；原域含无阻尼顶点，应理解严格证书为何不成立。

## Python 补充

从 SSY230 的虚拟环境复用 NumPy/SciPy/Matplotlib，或在本课根目录另建：

~~~powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install numpy scipy matplotlib
.\.venv\Scripts\python.exe self_study\tools\sanity_lab.py
~~~

输出：[先修与模型检查](examples/sanity_check.json)、[F‑16 原矩阵](examples/f16_source_matrices.json)。这些是检查数据，不是六次作业的已完成解答。

已在本机现有隔离运行时执行 sanity_lab，核对一阶系统 H₂ 的时频一致性、Lyapunov 残差、SEIR 守恒和 F‑16 矩阵契约；原文件未改动。没有创建上述 .venv 或修改系统 Python。

## 没有 Robust Control Toolbox 时

基础范数、互联、LQR、相平面和非线性作业可用 NumPy/SciPy 完成；LMI 可用另行配置的 SDP 工具。H∞/H₂ 综合可研究 Python 控制库及其底层依赖，但本次未安装/验证这一替代栈，不把它称为开箱可用。

可先完成本地标量 Riccati 题、给定控制器的鲁棒验证和非线性主线；完整 F‑16 输出反馈综合保留为待具备工具条件后完成的原生步骤。不能把有限网格调参称为已经等价完成一般 H∞ 最优综合。

为避免课程被环境阻断，所有理论关卡均给出手推/小规模验证入口；但最终报告必须诚实区分原生任务和替代任务。
