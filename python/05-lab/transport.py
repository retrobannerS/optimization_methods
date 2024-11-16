from cvxopt.modeling import variable, op
import time
start = time.time()
x = variable(25, 'x')
c= [7, 4, 8, 8, 7, 3, 7, 8, 5, 4, 8, 8, 3, 6, 5, 2, 8, 6, 2, 5]
z=sum(c[i]*x[i] for i in range(20))
mass = []
mass += [sum(x[i] for i in range(4)) == 170]
mass += [sum(x[i] for i in range(4, 8)) == 65]
mass += [sum(x[i] for i in range(8, 12)) == 115]
mass += [sum(x[i] for i in range(12, 16)) == 130]
mass += [sum(x[i] for i in range(16, 20)) == 140]
mass += [sum(x[i] for i in range(0, 20, 4)) == 195]
mass += [sum(x[i] for i in range(1, 20, 4)) == 190]
mass += [sum(x[i] for i in range(2, 20, 4)) == 135]
mass += [sum(x[i] for i in range(3, 20, 4)) == 100]
mass += [x >= 0]    

problem =op(z, mass)
problem.solve(solver='glpk')  
print("Результат Xopt:")
for i, value in enumerate(x.value, start=1):
    print(f"{int(value):3}", end=' ')
    if i % 4 == 0:
        print()
print(f"Стоимость доставки: {problem.objective.value()[0]}")
stop = time.time()
print (f"Время:{stop - start:.2f}")