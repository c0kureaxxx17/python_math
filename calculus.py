import sympy

x = sympy.Symbol('x')

# 微分計算
y = x**2 - 2*x + 2
Dy = sympy.Derivative(y, x).doit()
print(Dy)
Dfy = sympy.diff(y, x).subs(x,2)
print(Dfy)
# 積分計算
y = 6*x**2 + 2*x - 3
Iy = sympy.integrate(y,x)
print(Iy)
Diy = sympy.integrate(y, (x, -2, 1))
print(Diy)