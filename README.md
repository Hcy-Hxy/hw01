# N-Queens Problem Solver

使用回溯算法解决 N 皇后问题的 Python 实现。

## 项目结构

```
hw01/
├── src/
│   ├── __init__.py
│   └── n_queens.py       # N 皇后求解器实现
├── tests/
│   ├── __init__.py
│   └── test_n_queens.py  # 单元测试
└── README.md
```

## 功能

- `solve_n_queens(n)`: 返回 N 皇后问题的所有解
- `solve_n_queens_single(n)`: 返回 N 皇后的一个解
- `is_safe(board, row, col)`: 检查在指定位置放置皇后是否安全

## 使用方法

```python
from src.n_queens import solve_n_queens, solve_n_queens_single

# 获取所有解
solutions = solve_n_queens(8)
print(f"8 皇后问题共有 {len(solutions)} 个解")

# 获取一个解
solution = solve_n_queens_single(8)
print(f"一个解: {solution}")
```

## 运行测试

```bash
pytest tests/
```

## 测试覆盖

- N=1: 有 1 个解
- N=4: 有 2 个解
- N=8: 有 92 个解
- N=2, N=3: 无解
