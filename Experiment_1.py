import numpy as np
import matplotlib.pyplot as plt

#------------PROGRAM 1------------------------
# n = np.arange(-4,5)
# x = []
# for i in n:
#     if i == 0:
#         x.append(1)
#     else:
#         x.append(0)

# plt.stem(n,x)
# plt.title("1. Impulse Function Graph")
# plt.grid()
# plt.show()

#-------------PROGRAM 2----------------
# n = np.arange(-4,5)
# x = []
# for i in n:
#     if i >=0:
#         x.append(1)
#     else:
#         x.append(0)
# plt.stem(n,x)
# plt.grid()
# plt.title("2. Unit Step Function")
# plt.xlabel("x")
# plt.ylabel("x[n]")
# plt.show()

#-----------------PROGRAM 3------------------
# n = np.arange(-4,5)
# x = []
# for i in n:
#     if i >=0:
#         x.append(i)
#     else:
#         x.append(0)
# plt.stem(n,x)
# plt.grid()
# plt.title("3. Unit Ramp Function")
# plt.xlabel("x")
# plt.ylabel("x[n]")
# plt.show()

#-------------PROGRAM 4--------------------
# n = np.arange(1,11)
# x = []
# for i in n:
#     x.append(2**i)
# plt.stem(n,x)
# plt.grid()
# plt.title("4. Exponential Function")
# plt.show()

#-------------PROGRAM 5------------------------
n = np.arange(1,21)
x=[]
for i in n:
    x.append(np.sin(i))
plt.stem(n,x)
plt.grid()
plt.title("5. Sinusoidal Function")
plt.show()

