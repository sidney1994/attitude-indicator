#from gh_internal import plot_g_h_results
#import  book_plots
import numpy as np
import matplotlib.pyplot as plt

def g_h_filter(data,x0,dx,g,h,dt=1.,pred=None):
    x=x0
    results=[]
    for z in data:
        x_est=x+(dx*dt)
        dx=dx
        if pred is not None:
            pred.append(x_est)
        residual=z-x_est
        dx=dx+h*(residual)/dt
        x=x_est+g*residual
        results.append(x)
    return np.array(results)

weights=np.array([158.0, 164.2, 160.3, 159.9, 162.1, 164.6,
                  169.6, 167.4, 166.4, 171.0, 171.2, 172.6])
#book_plots.plot_track([0, 11], [160, 172], label='Actual weight')
data = g_h_filter(data=weights, x0=160, dx=1, g=3./10, h=1./3, dt=1.)
print data
print type(data)

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])


plt.plot(x,data,color="red")
plt.plot(x,weights,color="blue")
plt.show()
#plot_g_h_results(weights, data);


