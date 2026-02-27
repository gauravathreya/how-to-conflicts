import numpy as np 
import matplotlib.pyplot as plt 


#### this script is used to plot two gaussian functions that overlap 

# normal distribution as a function of the mean mu, standard deviation sigma, and position on the x-axis x
def gauss(mu,sigma,x):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-mu)**2/(2*sigma**2))

xvalues = np.linspace(-4, 4, 100)

# define mean and standard deviation for two distributions 
mu1 = -1
sigma1 = 1

mu2 = +1
sigma2 = 1

gauss1 = gauss(mu1, sigma1, xvalues)
gauss2 = gauss(mu2, sigma2, xvalues)

# plot them

fig,ax=plt.subplots()
ax.fill_between(xvalues, gauss1, alpha=0.4)
ax.fill_between(xvalues, gauss2, alpha=0.4)
ax.set_yticks([])
ax.set_xticks([])
plt.ylim([0,0.65])
plt.savefig('2-gaussians.pdf', format='pdf')
plt.show()