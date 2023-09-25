|这个作业属于哪个课程|[班级的链接](https://bbs.csdn.net/forums/fzusdn-0831)|
|-- |-- |
|这个作业要求在哪里|[作业要求的链接](https://bbs.csdn.net/topics/617255492)|
|个人学号|102299120|
| 结对成员学号 |102299210|
|GitHub 仓库地址|[GitHub仓库地址](https://github.com/Leen-Ouyang/Sudoku)|

# 一、项目概述
- **项目名称：** 数多窟（Sudoku）
- **项目类型：** 高级休闲游戏开发
- **项目范围：** 数多窟是一款高级数独游戏，旨在为用户提供有挑战的游戏和益智体验。游戏包括以下主要功能和特性：
  - **多线程9x9x9的并发数独：** 同时挑战和解决多个数独，用户可以在一个游戏会话中锻炼解谜技能，提高反应速度和逻辑思维能力。
  - **高效率生成数独：** 系统需要实现高效的数独生成算法，以确保生成数独的过程尽可能快速，减少用户等待时间。
  - **清爽简约的用户界面**：PC端大屏应用，数独网格规整清晰不密集，减轻用户的视觉疲劳。
  - **不同难度级别的数独谜题：** 包括“新手”，“简单”，“中等”，“困难”，“地狱”5个等级。
- **目标用户：** 本项目的目标用户是高级数独挑战者，他们不满足于一次玩一张数独，更希望能够一次性畅玩9个数独。此外，该游戏也适合其他数独爱好者和寻找益智游戏的用户。
- **业务需求：** 以下是项目的主要业务需求和其优先级：
  1. 多并发高级数独游戏，可以同时挑战解决多个九宫格数独 - 优先级：高
  2. 实现高效的数独生成算法，以确保生成数独的过程尽可能快速 - 优先级：高
  3. 提供清爽简约的用户界面，适应不同用户环境和喜好 - 优先级：中
  4. 提供多个数独谜题难度级别（初级、中级、高级） - 优先级：中
 
# 二、需求分析的NABCD模型
1. **Need（需求）：** 明确该产品的目标用户是谁，他们的需求是什么。
2. **Approach（做法）：** 在了解客户需求的基础上，确定应对方式。
3. **Benefit（好处）：** 明确该产品能给用户带来哪些益处。
4. **Competition（竞争）：** 分析与该产品相竞争的其他产品或服务，找出其优势和劣势。
5. **Delivery（推广）：** 在确定了该产品的需求、方法、益处和竞争优势后，考虑如何将其交付给目标用户。

### Need（需求）：
1. **并发生成数独**：系统能够同时生成9个九宫格数独，以满足用户同时挑战多个数独的需求，提高游戏难度和效率。
2. **保证数独可解性**：系统确保生成的每个九宫格数独都可解，以保证用户能够在后续游戏中解决这些数独，展示他们的解谜技能。

### Approach（做法）：
设计一个满足需求的数独生成的网页。
具体功能如下：
1. **数字选择：** 用户无需使用键盘输入，使用鼠标点选相应数字填入。
2. **难度设置：** 有1-5个难度可选，分别为“新手”，“简单”，“中等”，“困难”，“地狱”。
3. **并行生成独立数独页面：** 9个9宫格数独并行生成，每个数独都可独立求解，在界面上方标签栏以“puzzle1”~“puzzle9”的标签展现。

### Benefit（好处）：
1. **数字选择：** 目光只需专注于屏幕，保证了游戏的沉浸感和便利性，使用直观便捷。
2. **难度设置：** 多种难度可选，适应不同水平的用户，满足玩家的挑战心理，符合成长曲线，延长产品生命周期，提高游戏的丰富度。
3. **界面设置：** 相比前后移动按钮等其他形式的UI设计：
   - 只需点选一次随时选择其中任意一个数独页面，操作便捷。
   - 为每个数独页面编码，方便用户切换查找。

### Competition（竞争）：
|   产品    | 优势 (Strengths)| 劣势 (Weaknesses)  | 机会 (Opportunities)       | 威胁 (Threats)      |
| --| -- | -- | -- | -- |
| 数多窟 | - 并发生成多个数独<br />\- 直观的数字选择界面<br />\- 多个难度级别可选<br />- 适用于大屏幕设备<br />- 单机游戏无需互联网连接 | - 用户需要下载和安装<br />- UI界面不够清爽 | \- 推出新的数独挑战模式<br />- 断改进和优化用户体验 | \- 强大竞品的存在<br />\- 市场饱和度 |
| 移动端数独应用| - 已有大用户基础<br />- 手机端利用碎片化休闲时间 | - 界面可能相对较小<br />- 广告多，沉浸感差 | - 持续改进应用  | - 竞争激烈  |
| 在线数独网站 | - 免费在线访问<br />- 社区和讨论区  | - 需要互联网连接<br />- 广告多，沉浸感差 | - 提供多样化的数独挑战 | - 用户流失率可能较高 |
| 桌面数独游戏应用 | - 适用于大屏幕设备<br />\- 单机游戏无需互联网连接 | - 受限于桌面平台 | - 提供高质量的数独体验  | - 用户流失率可能较高  |

针对竞争，我们的优势在于**并发生成多个数独**，提供了更高的挑战性和娱乐性，以及**直观的UI界面**。此外，我们可以通过不断改进和优化用户体验来吸引更多用户。

### Delivery（推广）：
推广策略包括以下方面：
1. **精准广告定位**：使用在线广告平台，如B站等，将广告针对那些对数独感兴趣的用户，并突出多并发生成的特点。选择在数独爱好者的社交群体中投放广告。
2. **社交媒体宣传**：在社交媒体平台上创建精彩的广告和宣传内容，强调“数多窟”可以同时生成多个数独，提供更高的挑战和娱乐性。使用视觉效果来演示并发生成的过程。
3. **教程和演示视频**：制作教程和演示视频，展示“数多窟”如何同时生成多个数独，以及用户如何使用这个功能。将视频分享到B站、知乎、小红书等社交媒体上，并在应用内提供链接。

# 三、PSP表格
|PSP任务 | 估计时间（分钟）| 实际时间（分钟） |
| --- | --- |---|
|计划制定|60|90|
|需求分析|120|180|
|具体编码|300|480|
|测试（单元测试，功能测试等）|100|60|
|代码审查|60|60|
|编写文档	|180|240|
|用户接受测试|20|15|
|重构代码|60|30|
|项目总结	|60|30|
|合计|960|1185|

# 四、原型开发
- **工具：** 墨刀
- **原型展示在线链接：**[数多窟](https://modao.cc/proto/YxRiGpLs1fla6urv1ETm/sharing?view_mode=device&screen=rbpTqfZFDGXbNDTNp&canvasId=rcTqfZFDTqglflLbVMKdG1)

# 五、用户指南
## 运行方式
- 运行 GUI.py
- 运行 /dist/数多窟.exe &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;←优先选择

## 使用说明
- 选中一个格子时，该格子会被高亮，此时可以点击数字选择按钮向其中填入数字，而题目默认生成的格子为灰色，会与填入的格子做以区分
- 当玩家自认完成后，可以单击显示答案按钮，以获取该题目的参考答案
- 当玩家认为当前难度不适合或已做完当前生成的九道题目时，可以单击难度选择按钮重新生成符合自己要求的难度的数独题目
（Tips：默认难度为中等）

## 难度说明
本游戏中，难度等级对应留空数量：
- 新手：10%
- 简单：30%
- 中等：50%
- 困难：70%
- 地狱：90%

## 运行结果展示
### 主界面
![主界面](/images/1.png)
### 显示答案
![显示答案](/images/answer.png)
### 切换难度
![切换难度](/images/difficultchange.png)
### 高亮选中格子
![高亮显示](/images/select.png)

# 六、算法思路
### 数独生成
1. 生成一个完整的数独解：通过随机填充数独格子，并确保填充的数字满足数独规则（每行、每列、每个3x3子网格中的数字不重复）来生成一个完整的数独解。
2. 随机删除数字：从完整的数独解中随机删除一些数字，直到达到所需的难度。

由此生成具备可解性的数独，并根据难度进行空格数量的调整
### 并发性
1. generate_sudoku_puzzle:
这个函数用于生成一个数独题目和其对应的答案。在不同线程中，它调用 sudokum.generate 生成数独题目，然后尝试解答这个数独题目。这一部分并发地在多个线程中同时运行，每个线程独立生成数独题目。
```python
#根据难度生成数独题目
def generate_sudoku_puzzle(difficulty_level):
    # 获取对应难度级别的mask_rate
    mask_rate = difficulty_mapping.get(difficulty_level, 0.5)
    
    while True:
        # 获取对应难度级别的mask_rate
        mask_rate = difficulty_mapping.get(difficulty_level, 0.5)

        # 使用sudokum生成数独题目
        puzzle = sudokum.generate(mask_rate)

        # 尝试解答数独题目
        solve_result = sudokum.solve(puzzle)
    
        if solve_result[0]:
            # 如果成功解答，返回数独的答案
            answer = solve_result[1]
            return puzzle , answer
```
2. generate_sudoku_parallel:
这个函数根据传入的线程数，在不同线程中调用 generate_sudoku_puzzle 来生成多个数独题目和答案。它使用 ThreadPoolExecutor 来并发地处理生成数独的任务。
```python
#根据线程数生成多个数独
def generate_sudoku_parallel(thread_count, difficulty_level):
    # 定义线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        # 同时生成多个数独题目和答案
        results = [executor.submit(generate_sudoku_puzzle, difficulty_level) for _ in range(thread_count)]
        
        # 获取数独题目和答案
        sudoku_puzzles, sudoku_answers = zip(*[result.result() for result in results])
    
    return sudoku_puzzles, sudoku_answers
```

# 七、协同工作记录
![线上会议1](/images/a.jpg)
![线上会议2](/images/b.png)