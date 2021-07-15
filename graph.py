import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')

sympy.var('x')
y = sympy.exp(-x**2)
f = 3*x + 2
g = x**2 - 3 * x + 2
p = sympy.plot(f, g, (x, -4, 8), legend = True, show = False)
p[1].line_color = "red"
p.show()