import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl 


############### this script makes the plots necessary for figures 3,4,5 of the main text

# to make plots from figure 3, related to the meiotic drive model, set the flag `drive` to True. Similarly the flags `imprinting` and `sexualantagonism` 
# will show and save panels of figures 4 and 5 respectively. 

drive = False
imprinting = False
sexualantagonism = True

svalues = np.linspace(0,1,100)

if drive:
    for h in np.arange(0.0, 1.25, 0.25):
        kmin = (1 + svalues)/(2*(1 + h*svalues))
        plt.plot(svalues, kmin, c=mpl.colormaps['plasma'](0.25 + h/2), linewidth=2)

    plt.plot(svalues, [0.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    plt.plot(svalues, [0.5]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    plt.plot(svalues, [1.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)

    plt.ylim([-0.05,1.05])
    plt.xlim([-0.05,1.05])

    plt.yticks(np.arange(0.0, 1.25, 0.25))
    plt.tick_params(axis='both', which='major', labelsize=17)
    plt.savefig('drive-invasion-persistence-criteria.pdf', format='pdf')
    plt.show()

    # dynamical fates for a given dominance coefficient h

    h = 0.25

    kinv = (1 + svalues)/(2*(1+h*svalues))
    kfix = (1 + 2*h*svalues)/(2*(1+h*svalues))

    plt.plot(svalues, kinv, c='b', linewidth=2)
    if h>=0.5: # this line plots the maximum k at which fixation takes place after invasion; above this k the outcome is stable polymorphism of the 
               # driving and non-driving alleles. But for this to happen the positive fitness effect of not having a driving allele must be 
               # partially dominant (see main text eq. 7). So the plotting of kfix is inside an if-statement with condition h>0.5  
         plt.plot(svalues, kfix, c='g', linewidth=2)
     
    # plot horizontal lines at k=0, 0.5, and 1 for reference
    plt.plot(svalues, [0.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    plt.plot(svalues, [0.5]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    plt.plot(svalues, [1.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)

    # axis limits and make axis ticks large
    plt.ylim([-0.05,1.05])
    plt.xlim([-0.05,1.05])
    plt.yticks(np.arange(0.0, 1.25, 0.25))
    plt.tick_params(axis='both', which='major', labelsize=17)

    plt.savefig('drive-invasion-persistence-criteria' + 'h=' + str(h) + '.pdf', format='pdf')
    plt.show()


# imprinting invasion

if imprinting:
    # cost by benefit values
    cbybvalues = np.linspace(0.5,1,100) 

    # minimum imprinting strength (prob. of altruism being silenced when paternally inherited) for invasion (see main text eq. 13, some reorganisation necessary)
    mmin = 2 - 1/cbybvalues

    # plot mmin, m = 0,1 for reference, and make things look nice 
    plt.plot(cbybvalues, mmin, c='r', linewidth=2)
    plt.plot(svalues, [0.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    plt.plot(svalues, [1.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)

    plt.ylim([-0.05,1.05])
    plt.xlim([-0.05,1.05])

    plt.yticks(np.arange(0.0, 1.25, 0.25))
    plt.savefig('imprinting-invasion-persistence-criteria.pdf', format='pdf')
    plt.show()


if sexualantagonism:
    # plot invasion criteria for male beneficial mutations
    Mvaluespos = np.arange(0.0, 1.05, 0.05)
    plt.plot(Mvaluespos, 1.0/(2+Mvaluespos), 'k')
    plt.fill_between(Mvaluespos, 1.0/(2+Mvaluespos), color='red', alpha=0.7) # the y-value here is the maximum dominance required for conflict (see main text eq. 22 and sentence immediately after)
    plt.fill_between(Mvaluespos, 1.0/(2+Mvaluespos), 1, color='green', alpha=0.7)
    plt.plot(Mvaluespos, [0.5]*len(Mvaluespos), '--', c='k', alpha=0.7, linewidth=1)

    plt.ylim([0,1.1])
    plt.savefig('sexant-conflict-M>0.pdf', format='pdf')
    plt.show()

    # to plot invasion criteria for female beneficial mutations
    Mvaluesneg = np.arange(0.0, -1.05, -0.05)

    plt.plot(Mvaluesneg, 1.0/(2+Mvaluesneg), 'k')
    plt.fill_between(Mvaluesneg, 1.0/(2+Mvaluesneg), color='green', alpha=0.7) # the y-value here is the minimum dominance required for conflict (see main text eq. 23 and sentence immediately after)
    plt.fill_between(Mvaluesneg, 1.0/(2+Mvaluesneg), 1, color='red', alpha=0.7)
    plt.plot(Mvaluesneg, [0.5]*len(Mvaluesneg), '--', c='k', alpha=0.7, linewidth=1)

    plt.ylim([0,1.1])
    plt.savefig('sexant-conflict-M<0.pdf', format='pdf')
    plt.show()


        


