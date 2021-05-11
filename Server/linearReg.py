from matplotlib import pyplot as plt

X=list(range(-3,4))
Y=[62,63,67,40,13,10,9]
Xsum=0.0
X2sum=0.0
Ysum=0.0
XY=0.0
n=len(X)
for i in range(n):
    Xsum+=X[i]
    Ysum+=Y[i]
    XY+=X[i]*Y[i]
    X2sum+=X[i]**2
k=(Xsum*Ysum/n-XY)/(Xsum**2/n-X2sum)
b=(Ysum-k*Xsum)/n
print('the line is y=%f*x+%f' % (k,b) )

Z=[]
for i in X:
    Z.append(k*i+b)
plt.plot(X, Z, label='First Curve')
plt.scatter(X, Y, c='r' , alpha=0.5, marker=(9, 3, 30))

plt.grid(True)
plt.show()

