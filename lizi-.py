import  numpy  as np
import   matplotlib.pyplot as plt


x=np.linspace(0,10,1000)
y=np.sin(x)
z=np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("tume")
plt.ylabel("volt")
plt.title("pyplot first example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()