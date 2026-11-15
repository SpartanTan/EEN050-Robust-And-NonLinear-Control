# 资源、覆盖与下载状态

[返回主线](../robust_nonlinear_control_learning_plan.md) · [审计](source_audit.md)

核对日期 2026-11-10。14 个原文件全部安排到主线、选读或资料缺口说明；没有修改原文件。下载成功不等于软件已运行。

## 本地材料

|文件|用途|页数|
|---|---|---:|
|[Assignments/Assignment4.pdf](../Assignments/Assignment4.pdf)|R8–R9：LPV/SEIR|2|
|[Assignments/Assignment5.pdf](../Assignments/Assignment5.pdf)|N1–N2：相平面/反应扩散|2|
|[Assignments/Assignment6.pdf](../Assignments/Assignment6.pdf)|N4–N5：反馈线性化|3|
|[Assignments/Assignments_1-3.pdf](../Assignments/Assignments_1-3.pdf)|R3–R7：连续的 F‑16 项目|5|
|[Assignments/f16model.m](../Assignments/f16model.m)|R0/R3–R7：原名义矩阵与执行器|—|
|[Exercises/EEN050 exercise compendium.pdf](../Exercises/EEN050%20exercise%20compendium.pdf)|R1–N6：48题；答案相邻|81|
|[Exercises/Exercise_5_3.m](../Exercises/Exercise_5_3.m)|R9：先审计零可行解/无阻尼顶点|—|
|[Exercises/Exercise_6_1.m](../Exercises/Exercise_6_1.m)|N1：相平面辅助；记录实际初值|—|
|[Extra/H2 norms.pdf](../Extra/H2%20norms.pdf)|R1/R4：范数、Parseval 的参考补充|15|
|[Extra/H2, Hinf, and Parseval theorem.docx](../Extra/H2%2C%20Hinf%2C%20and%20Parseval%20theorem.docx)|R1：两个外部资料链接，非完整教材|—|
|[Extra/On - Lp - Linfinity norms.pdf](../Extra/On%20-%20Lp%20-%20Linfinity%20norms.pdf)|R1：范数补充页，可选|1|
|[quiz/Solution to the quizzes 2023.pdf](../quiz/Solution%20to%20the%20quizzes%202023.pdf)|仅答案字母；缺题面，不作为评分来源|3|
|[Slides/EEN050_Lectures_Nonlinear copy.pdf](../Slides/EEN050_Lectures_Nonlinear%20copy.pdf)|N1–N6 主讲义|142|
|[Slides/EEN050_Lectures_Robust_with_discussion_questions.pdf](../Slides/EEN050_Lectures_Robust_with_discussion_questions.pdf)|R0–R9 主讲义|230|

## MIT 6.241J：已下载的补充讲义

来源：[MIT OCW Dynamic Systems and Control，Spring 2011](https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/pages/lecture-notes/)。年代较早，但用于本课基本理论；不据此声称是 2026 年的新课程。只选下面 5 份，不要求重新学完另一个完整课程。

|讲义|主题|本课任务|本地状态|
|---|---|---|---|
|[Lecture 12](resources/mit/lecture12.pdf)|I/O stability|R0/R3|已下载，PDF可读取，13页|
|[Lecture 16](resources/mit/lecture16.pdf)|Bode’s sensitivity integral|R5|已下载，PDF可读取，8页|
|[Lecture 17](resources/mit/lecture17.pdf)|Robust stability|R3/R7|已下载，PDF可读取，16页|
|[Lecture 24](resources/mit/lecture24.pdf)|H 2 optimization|R4|已下载，PDF可读取，28页|
|[Lecture 25](resources/mit/lecture25.pdf)|H ∞ optimization|R6|已下载，PDF可读取，13页|

下载源、大小及 SHA-256 见 [下载清单](audit/download_manifest.json)。使用或再分发应遵循 MIT OCW 的许可与第三方材料例外。

## 在线阅读与工具资料

|来源|使用范围|本次状态|
|---|---|---|
|[MIT Lyapunov Analysis](https://underactuated.mit.edu/lyapunov.html)|N2 的能量、吸引域、数值证书|网页已核对；未下载/执行 Drake 代码|
|[MIT Acrobots/Cart-Poles](https://underactuated.mit.edu/acrobot.html)|N4/I1 后选读：欠驱动与部分反馈线性化|网页已核对；不作为主线安装前置|
|[YALMIP 半正定教程](https://yalmip.github.io/tutorial/semidefiniteprogramming/)|R9：数值余量、零解和求解结果|官方网页已核对；本机工具/求解器未执行|
|[MathWorks H₂](https://www.mathworks.com/help/robust/ref/dynamicsystem.h2syn.html) / [H∞](https://www.mathworks.com/help/robust/ref/dynamicsystem.hinfsyn.html)|R5/R6：端口、综合和正则化|在线文档已核对；本地版本/许可证未知|
|[MathWorks 鲁棒分析](https://www.mathworks.com/help/robust/ug/robust-stability-robust-performance-and-mu-analysis.html)|R7：robstab/robgain、μ、上下界|官方检索核对；未执行|
|[Skogestad 作者书页](https://skoge.folk.ntnu.no/book/index_1st_edition.html)|额外教材入口与例题；非必需|公开书页已核对；完整付费教材未取得|

本地 DOCX 内的旧外部链接保留原样，不设为主线必须可访问的依赖。未将课堂材料中的联系人、提交规则或链接文本当成操作指令。

## 有意延后

μ 综合/D–K 迭代、大规模非线性 HJB/PDE 求解、SOS/CLF–CBF、非线性 MPC、自适应鲁棒控制可在核心之后再选。主线先保证能读懂 H∞/LPV 的条件，推导并实现基础非线性控制，而非同时引入所有现代算法。
