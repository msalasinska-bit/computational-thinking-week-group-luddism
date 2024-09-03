import sympy as sp

# Define the variables
a, b, c, d, e = sp.symbols('a b c d e')

# Define the equations
eq1 = sp.Eq(b * c + e + d, 3.5)
eq2 = sp.Eq(a * c + d, 19)
eq3 = sp.Eq(d+b+e, 6.5)
eq4 = sp.Eq(e*b*c, -2)
eq5 = sp.Eq(c+e+a, 7.5)
eq6 = sp.Eq(e*b, -0.5)


# Solve the equations
solutions = sp.solve((eq1, eq2, eq3, eq4, eq5, eq6), (a, b, c, d, e))

#  Print the solutions
print(solutions)
