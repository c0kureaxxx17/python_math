import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')
Sol2=sympy.solve(x**2 - 3 * x + 2)
Sol2=sympy.solve(x**3 - 8)
print(Sol2)

expr1 = 4 * x + 2 * y - 2
expr2 = 4 * x + 5 * y + 7

print(sympy.solve([expr1, expr2]))
