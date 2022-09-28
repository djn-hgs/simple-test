import pytest
from main import quadratic_solver


def test_quadratic_solver_type_error():
    with pytest.raises(TypeError):
        quadratic_solver(a="one", b="one", c="three")


def test_quadratic_solver_double_root():
    assert quadratic_solver(a=1, b=12, c=36) is (-6, -6)


def test_quadratic_solver_normal_root():
    assert quadratic_solver(a=1, b=7, c=10) is (-5, -2)


def test_quadratic_solver_no_roots():
    with pytest.raises(ValueError):
        quadratic_solver(a=1, b=1, c=1)


def test_quadratic_solver_not_quadratic():
    with pytest.raises(ValueError):
        quadratic_solver(a=0, b=0, c=0)
