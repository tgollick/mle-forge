# Polynomial Solver - Week 2

# Program that solves polynomials using the quadratic formula, returning the roots if > 0
def solve_quadratic(a: float, b: float, c: float):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None

    sqrt_delta = delta**0.5
    denominator = 2*a

    root1 = (-b + sqrt_delta) / denominator
    root2 = (-b - sqrt_delta) / denominator

    return (root1, root2) if (root1 != root2) else (root1,)

if __name__ == "__main__":
    a, b, c = map(float, input("Please enter a, b and c: ").split())

    roots = solve_quadratic(a, b, c)

    if roots is None:
        print("ERROR: Discriminant < 0 (Complex roots are not supported")
    else:
        print(f"Roots: {roots}")

