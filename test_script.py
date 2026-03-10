import sys
sys.path.append('src')
from n_queens import solve_n_queens, solve_n_queens_single

print("测试 N=1:")
result = solve_n_queens(1)
print(f"解的数量: {len(result) if result else 0}")
print(f"解: {result}")

print("\n测试 N=4:")
result = solve_n_queens(4)
print(f"解的数量: {len(result) if result else 0}")
print(f"解: {result}")

print("\n测试 N=8:")
result = solve_n_queens(8)
print(f"解的数量: {len(result) if result else 0}")

print("\n测试 N=2 (无解):")
result = solve_n_queens(2)
print(f"解的数量: {len(result) if result else 0}")
print(f"解: {result}")

print("\n测试 N=3 (无解):")
result = solve_n_queens(3)
print(f"解的数量: {len(result) if result else 0}")
print(f"解: {result}")
