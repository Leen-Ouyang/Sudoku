import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from RandomSudoku import generate_sudoku_parallel

# 更新数独显示
def update_sudoku_display(idx):
    for i in range(9):
        for j in range(9):
            if sudoku_puzzles[idx][i][j] == 0:
                entries[idx][i][j].delete(0, tk.END)
            else:
                entries[idx][i][j].delete(0, tk.END)
                entries[idx][i][j].insert(0, str(sudoku_puzzles[idx][i][j]))

# 切换数独题目
def switch_sudoku(event):
    global notebook
    idx = int(notebook.index(notebook.select()))
    update_sudoku_display(idx)

# 函数：高亮格子并绑定数字选择事件
def highlight_cell(row, col):
    global current_selected_cell

    # Reset previous highlight
    if current_selected_cell:
        entries[current_selected_cell[0]][current_selected_cell[1]][current_selected_cell[2]].config(bg='white')

    # Set new highlight
    entries[current_thread][row][col].config(bg='yellow')
    current_selected_cell = (current_thread, row, col)

# 生成界面
def generate_interface(thread_count):
    global notebook
    global entries  
    global current_thread
    global current_selected_cell

    root = tk.Tk()
    root.title("数多窟")

    # 创建标签页
    notebook = ttk.Notebook(root)
    notebook.pack()

    for i in range(thread_count):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=f"Puzzle{i+1}")
        
        # 为存储 Entry 对象的子列表初始化为空列表
        entry_row = []
        for row in range(9):
            entry_row.append([])
            for col in range(9):
                entry = tk.Entry(frame, width=2, font=("Arial", 18))
                entry.grid(row=row, column=col)
                entry.bind('<Button-1>', lambda e, row=row, col=col: highlight_cell(row, col))
                entry_row[row].append(entry)
        
        # 将 Entry 对象列表添加到 entries
        entries.append(entry_row)

    current_selected_cell = None
    current_thread = 0  # Default to the first thread

    # 更新数独显示
    switch_sudoku(None)

    # 绑定事件
    notebook.bind("<<NotebookTabChanged>>", switch_sudoku)

    # 创建难度选择部分
    difficulty_frame = ttk.Frame(root)
    difficulty_frame.pack(side="right", padx=20, pady=20)

    # 难度选择标签
    ttk.Label(difficulty_frame, text="难度选择").grid(row=0, column=0, columnspan=3, pady=(0, 10))

    # 难度选择按钮
    difficulty_buttons = {}
    for idx, difficulty in enumerate(["新手", "简单", "中等", "困难", "地狱"]):
        difficulty_buttons[difficulty] = tk.Button(difficulty_frame, text=difficulty, width=8, command=partial(change_difficulty, difficulty, thread_count))
        difficulty_buttons[difficulty].grid(row=1 + idx//3, column=idx%3, padx=5, pady=5)

    # 数字选择部分
    number_frame = ttk.Frame(root)
    number_frame.pack(side="right", padx=20, pady=20)

    ttk.Label(number_frame, text="数字选择").grid(row=0, column=0, columnspan=3, pady=(0, 10))

    for i in range(3):
        for j in range(3):
            button_number = i * 3 + j + 1
            button = tk.Button(number_frame, text=str(button_number), width=8, command=partial(select_number, button_number))
            button.grid(row=i + 1, column=j, padx=5, pady=5)

    root.mainloop()

# 函数：切换难度
def change_difficulty(difficulty, thread_count):
    global current_difficulty
    global sudoku_puzzles

    current_difficulty = difficulty
    # 生成新的数独题目
    global current_thread
    current_thread = notebook.index(notebook.select())
    sudoku_puzzles[current_thread], _ = generate_sudoku_parallel(thread_count, difficulty)
    # 更新数独显示
    switch_sudoku(None)
    messagebox.showinfo("提示", f"已切换难度为 {difficulty}")

# 函数：选择数字
def select_number(number):
    global current_thread
    global current_selected_cell

    if current_selected_cell:
        entries[current_selected_cell[0]][current_selected_cell[1]][current_selected_cell[2]].delete(0, tk.END)
        entries[current_selected_cell[0]][current_selected_cell[1]][current_selected_cell[2]].insert(0, str(number))
        current_selected_cell = None

# 例子使用：生成3个数独题目和答案
thread_count = 9
sudoku_puzzles , sudoku_answers = generate_sudoku_parallel(1, "中等")

# 存储界面中的所有Entry
entries = []

# 生成界面
generate_interface(thread_count)
