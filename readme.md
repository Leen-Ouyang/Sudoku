|这个作业属于哪个课程|[班级的链接](https://bbs.csdn.net/forums/fzusdn-0831)|
|-- |-- |
|这个作业要求在哪里|[作业要求的链接](https://bbs.csdn.net/topics/617255492)|
|个人学号|102299120|
| 结对成员学号 |102299210|
|GitHub 仓库地址|[GitHub仓库地址](https://github.com/Leen-Ouyang/Sudoku)|


# 运行方式
- 运行 GUI.py
- 运行 /dist/数多窟.exe &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;←优先选择

# 使用说明
- 选中一个格子时，该格子会被高亮，此时可以点击数字选择按钮向其中填入数字，当一个格子被填入数字后，其将会保持高亮状态，以对玩家填入的数值和题目原本的数字做以区分
- 当玩家自认完成后，可以单击显示答案按钮，以获取该题目的参考答案
- 当玩家认为当前难度不适合或已做完当前生成的九道题目时，可以单击难度选择按钮重新生成符合自己要求的难度的数独题目
（Tips：默认难度为中等）

# 难度说明
本游戏中，难度等级对应留空数量：
- 新手：10%
- 简单：30%
- 中等：50%
- 困难：70%
- 地狱：90%

# 运行结果展示
### 主界面
![主界面](/images/1.png)
### 显示答案
![显示答案](/images/answer.png)
### 切换难度
![切换难度](/images/difficultchange.png)
### 高亮选中格子
![高亮显示](/images/select.png)

# 算法思路
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
