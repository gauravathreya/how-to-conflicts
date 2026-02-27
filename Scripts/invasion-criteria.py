import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl 

drive = False
imprinting = False
sexualantagonism = True

svalues = np.linspace(0,1,100)

if drive:
    # for h in np.arange(0.0, 1.25, 0.25):
    #     kmin = (1 + svalues)/(2*(1 + h*svalues))
    #     plt.plot(svalues, kmin, c=mpl.colormaps['plasma'](0.25 + h/2), linewidth=2)

    # plt.plot(svalues, [0.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    # plt.plot(svalues, [0.5]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    # plt.plot(svalues, [1.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)

    # plt.ylim([-0.05,1.05])
    # plt.xlim([-0.05,1.05])

    # plt.yticks(np.arange(0.0, 1.25, 0.25))
    # plt.tick_params(axis='both', which='major', labelsize=17)
    # plt.savefig('drive-invasion-persistence-criteria.pdf', format='pdf')
    # plt.show()

    # # dynamical fates for a given dominance coefficient h

    # h = 0.25

    # kinv = (1 + svalues)/(2*(1+h*svalues))
    # kfix = (1 + 2*h*svalues)/(2*(1+h*svalues))

    # plt.plot(svalues, kinv, c='b', linewidth=2)
    # if h>=0.5:
    #      plt.plot(svalues, kfix, c='g', linewidth=2)

    # plt.plot(svalues, [0.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    # plt.plot(svalues, [0.5]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    # plt.plot(svalues, [1.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)

    # plt.ylim([-0.05,1.05])
    # plt.xlim([-0.05,1.05])

    # plt.yticks(np.arange(0.0, 1.25, 0.25))
    # plt.tick_params(axis='both', which='major', labelsize=17)
    # plt.savefig('drive-invasion-persistence-criteria' + 'h=' + str(h) + '.pdf', format='pdf')
    # plt.show()

    # equilibrium frequency

    k = 0.75
    h=0.75
    peq = ((1+h*svalues)*(2*k-1) - svalues*(1-h))/(svalues*(2*h-1))
    plt.plot(svalues,peq, c='k', linewidth=2)
    plt.show()


# imprinting invasion

if imprinting:
    cbybvalues = np.linspace(0.5,1,100) 

    mmin = 2 - 1/cbybvalues

    plt.plot(cbybvalues, mmin, c='r', linewidth=2)

    plt.plot(svalues, [0.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)
    plt.plot(svalues, [1.0]*len(svalues), '--', c='k', alpha=0.3, linewidth=1)

    plt.ylim([-0.05,1.05])
    plt.xlim([-0.05,1.05])

    plt.yticks(np.arange(0.0, 1.25, 0.25))
    plt.savefig('imprinting-invasion-persistence-criteria.pdf', format='pdf')
    plt.show()


if sexualantagonism:
    # to plot invasion criteria for male beneficial mutations
    Mvaluespos = np.arange(0.0, 1.05, 0.05)
    plt.plot(Mvaluespos, 1.0/(2+Mvaluespos), 'k')
    plt.fill_between(Mvaluespos, 1.0/(2+Mvaluespos), color='red', alpha=0.7)
    plt.fill_between(Mvaluespos, 1.0/(2+Mvaluespos), 1, color='green', alpha=0.7)
    plt.plot(Mvaluespos, [0.5]*len(Mvaluespos), '--', c='k', alpha=0.7, linewidth=1)

    plt.ylim([0,1.1])
    plt.savefig('sexant-conflict-M>0.pdf', format='pdf')
    plt.show()

    # to plot invasion criteria for female beneficial mutations

    Mvaluesneg = np.arange(0.0, -1.05, -0.05)

    plt.plot(Mvaluesneg, 1.0/(2+Mvaluesneg), 'k')
    plt.fill_between(Mvaluesneg, 1.0/(2+Mvaluesneg), color='green', alpha=0.7)
    plt.fill_between(Mvaluesneg, 1.0/(2+Mvaluesneg), 1, color='red', alpha=0.7)
    plt.plot(Mvaluesneg, [0.5]*len(Mvaluesneg), '--', c='k', alpha=0.7, linewidth=1)

    plt.ylim([0,1.1])
    plt.savefig('sexant-conflict-M<0.pdf', format='pdf')
    plt.show()


        


