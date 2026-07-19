import numpy as np
import matplotlib.pyplot as plt

#PROBLEM 1-----------------

# n1 = [-2,-1,0,1,2,3,4,5,6,7]
# x1 = [2,4,3,1,2,3,4,1,1,3]

# plt.figure(1)
# plt.stem(n1,x1)
# plt.title("Problem 1")
# plt.xlabel("n")
# plt.ylabel("x[n]")
# plt.grid(True)
# plt.show()

#PROBLEM 2------------------------
# n2 = [1,2,3,4,5,6,7]
# x2 = [1,2,3,4,3,2,1]
 
# plt.figure(2)
# plt.step(n2, x2, where="post")
# plt.title("Problem 2")
# plt.xlabel("n")
# plt.ylabel("x[n]")
# plt.grid(True)
# plt.show()

#PROBLEM 3-----------------------

# x1 = np.linspace(-2, -1, 50)
# y1 =[-2]*50

# x2 = np.linspace(-1, 1, 50)
# y2 =2*x2

# x3 = np.linspace(1, 2, 50)
# y3 = [2]*50

# plt.plot(x1, y1)
# plt.plot(x2, y2)
# plt.plot(x3, y3)

# plt.plot([-2, -2], [0, -2])
# plt.plot([2, 2], [2, 0])

# plt.grid()
# plt.xlabel("n")
# plt.ylabel("x[n]")
# plt.title("PROBLEM 3")
# plt.show()


#PROBLEM 4--------------------

# n = np.arange(-2, 11)
# x = []
# for i in n:

#     if i<0:
#         x.append(0)
#     elif i<3:
#         x.append(1)
#     elif i<7:
#         x.append(0)
#     else:
#         x.append(-5)

# plt.stem(n, x)
# plt.grid()
# plt.xlabel("n")
# plt.ylabel("x[n]")
# plt.title("Problem 4")
# plt.show()

#PROBLEM 5 --------------------
n = np.arange(-3, 4)
x = []
for i in n:

    if i==-1:
        x.append(5)
    elif i==0:
        x.append(1)
    elif i==1:
        x.append(3)
    else:
        x.append(0)

plt.stem(n, x)
plt.grid()
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Problem 5")
plt.show()