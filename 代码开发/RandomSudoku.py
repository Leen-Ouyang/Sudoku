import sudokum
import concurrent.futures

difficulty_mapping = {
    "新手":0.1,
    "简单":0.3,
    "中等":0.5,
    "困难":0.7,
    "地狱":0.9,
}

default_difficulty_level="简单"

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

#根据线程数生成多个数独
def generate_sudoku_parallel(thread_count, difficulty_level):
    # 定义线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        # 同时生成多个数独题目和答案
        results = [executor.submit(generate_sudoku_puzzle, difficulty_level) for _ in range(thread_count)]
        
        # 获取数独题目和答案
        sudoku_puzzles, sudoku_answers = zip(*[result.result() for result in results])
    
    return sudoku_puzzles, sudoku_answers
    #此处生成的题目和答案访问格式：for puzzle in sudoku_puzzles:/for answer in sudoku_answers:

""" thread_count = 9
sudoku_puzzles, sudoku_answers = generate_sudoku_parallel(thread_count, "地狱")

print("生成的数独题目：")
for puzzle in sudoku_puzzles:
    print(puzzle)
    print("-----")

print("\n数独的答案：")
for answer in sudoku_answers:
    print(answer)
    print("-----") """