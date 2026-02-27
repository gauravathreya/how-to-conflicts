import numpy as np 
import matplotlib.pyplot as plt 

def gauss(mu,sigma,x):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-mu)**2/(2*sigma**2))

xvalues = np.linspace(-4, 4, 100)

mu1 = -1
sigma1 = 1

mu2 = +1
sigma2 = 1

gauss1 = gauss(mu1, sigma1, xvalues)
gauss2 = gauss(mu2, sigma2, xvalues)


fig,ax=plt.subplots()

ax.fill_between(xvalues, gauss1, alpha=0.4)
ax.fill_between(xvalues, gauss2, alpha=0.4)
ax.set_yticks([])
ax.set_xticks([])
plt.ylim([0,0.65])
plt.savefig('2-gaussians.pdf', format='pdf')
plt.show()