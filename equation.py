
from sympy import symbols, solve
print("sympy is needed for the script")
X1 = int(input())
X2 = int(input())
X3 = int(input())
x = symbols('x')
expr = ((X1 * x ** 2) + (X2 * x) + X3)
cont = int(0)
while cont == 0:
    print("Your equation is=" + str(X1) + "*X^2+" + str(X2) + "X" + "+" + str(X3))
    print("Choose what you seek\n"
          "1.When the equation meets X=0\n"
          "2.When the equation meets Y=0\n"
          "3.What is the changing point\n"
          "4.What kind is the changing point\n")
    asnw = int(input())
    if asnw == 1:
        sol = solve(expr)
        print(sol)
    if asnw == 2:
        print(X3)
    if asnw == 3:
        expr1 = (2 * X1 * x + X2)
        sol1 = solve(expr1)
        print(sol1)
    if asnw == 4:
        print(2 * X1)
        print("When its negative, its max. and when its positive its min")
    print("\n\n\n")
