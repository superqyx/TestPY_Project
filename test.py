import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(1)
# x = np.arange(10)
# y = np.random.randint(0,9,10)
#
# plt.plot(x,y)
# plt.show()

def f2(x,w):
    return (x+w) * x * (x+2)
x = np.linspace(-3, 3, 100)
# plt.plot(x, f2(x,2), color='black', label='$w=2$')
# plt.plot(x, f2(x,1), color='blue', label='$w=1$')
# plt.legend(loc='upper center')
# plt.title("$f_2(x)$")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(-15,15)
# plt.grid(True)
#
# plt.show()

plt.figure(figsize=(30,10))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.title(i+1)
    plt.plot(x,f2(x,i),color='red')
    plt.ylim(-15,15)
    plt.grid(True)
plt.show()
