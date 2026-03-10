import pytest
from src.n_queens import solve_n_queens, solve_n_queens_single


class TestNQueens:
    def test_n_1(self):
        result = solve_n_queens(1)
        assert result is not None
        assert len(result) == 1
        assert result[0] == [0]

    def test_n_4(self):
        result = solve_n_queens(4)
        assert result is not None
        assert len(result) == 2
        for solution in result:
            assert len(solution) == 4
            assert set(solution) == {0, 1, 2, 3}

    def test_n_8(self):
        result = solve_n_queens(8)
        assert result is not None
        assert len(result) == 92
        for solution in result:
            assert len(solution) == 8
            assert set(solution) == {0, 1, 2, 3, 4, 5, 6, 7}

    def test_n_2_no_solution(self):
        result = solve_n_queens(2)
        assert result is None

    def test_n_3_no_solution(self):
        result = solve_n_queens(3)
        assert result is None

    def test_n_1_single(self):
        result = solve_n_queens_single(1)
        assert result is not None
        assert result == [0]

    def test_n_4_single(self):
        result = solve_n_queens_single(4)
        assert result is not None
        assert len(result) == 4
        assert set(result) == {0, 1, 2, 3}

    def test_n_8_single(self):
        result = solve_n_queens_single(8)
        assert result is not None
        assert len(result) == 8
        assert set(result) == {0, 1, 2, 3, 4, 5, 6, 7}

    def test_n_2_single_no_solution(self):
        result = solve_n_queens_single(2)
        assert result is None

    def test_n_3_single_no_solution(self):
        result = solve_n_queens_single(3)
        assert result is None
