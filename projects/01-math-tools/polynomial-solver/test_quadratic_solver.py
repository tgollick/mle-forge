# Test cases to make sure the correct output is observed
import pytest
from main import solve_quadratic

# Main functionality, distinct real roots
@pytest.mark.parametrize("a, b, c, expected", [
    (1, -5, 6, (2.0, 3.0)),
    (1, 1, -6, (-3.0, 2.0)),
    (2, -3, -2, (2.0, -0.5)),
    (-1, 5, -6, (2.0, 3.0)),
])
def test_two_real_roots(a, b, c, expected):
    result = solve_quadratic(a, b, c)
    assert result is not None
    assert tuple(sorted(result)) == pytest.approx(tuple(sorted(expected)))

# Handle edge case, repeated routs (-2, 2)
def test_repeated_roots():
    result = solve_quadratic(1, -4, 4)
    assert result == (2.0,)

# Handle edge case, no real roots (delta < 0)
def test_no_real_roots():
    result = solve_quadratic(1, 0, 1)
    assert result is None

# To verifying we can plug the roots back into the equation
@pytest.mark.parametrize("a, b, c", [
    (2, -4, -6),
    (1, 0, -4),
])
def test_roots_satisfy_equation(a, b, c):
    roots = solve_quadratic(a, b, c)
    assert roots is not None
    for root in roots:
        assert abs(a*root**2 + b*root + c) < 0.001

