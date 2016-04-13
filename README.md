# CFD
##### For MAE6286 Practical Numerical Methods from GWU.
##### This is my answer to Module 1 in modeling rocket dynamics.
##### Course Info can be found at http://openedx.seas.gwu.edu/courses/GW/MAE6286/2014_fall/info

![Alt Text](https://github.com/gzshao/CFD/blob/master/equation.png)

* h: altitude of rocket, m
* ms=50 Kg, weight of satellite
* mp=100 Kg, initial weight of propellant
* v: velocity of the rocket, m/s
* ve=325 m/s, velocity of exhaust leaving the rocket
* Cd=0.15, drag coefficient
* The fuel is consumed at 20 Kg/s at constant rate.


# How to use Sympy?
1.  import sympy
2.  sympy.init_printing()
3.  write down equations
    *   u_max, u_star, rho_max, rho_star, A, B = sympy.symbols('u_max u_star rho_max rho_star A B')
    *   eq1 = sympy.Eq( 0, u_max*rho_max*(1 - A*rho_max-B*rho_max**2) )
    *   eq2 = sympy.Eq( 0, u_max*(1 - 2*A*rho_star-3*B*rho_star**2) )
    *   eq3 = sympy.Eq( u_star, u_max*(1 - A*rho_star - B*rho_star**2) )
4.  calculation of equations
    *   eq4 = sympy.Eq(eq2.lhs - 3*eq3.lhs, eq2.rhs - 3*eq3.rhs)
5.  solving equation
    *   rho_sol = sympy.solve(eq4,rho_star)[0]
    *   B_sol = sympy.solve(eq1,B)[0]
    *   quadA = eq2.subs([(rho_star, rho_sol), (B,B_sol)])
    *   A_sol = sympy.solve(quadA, A)
6.  plug in numbers
    *   aval = A_sol[0].evalf(subs={u_star: 0.7, u_max:1.0, rho_max:10.0} )
