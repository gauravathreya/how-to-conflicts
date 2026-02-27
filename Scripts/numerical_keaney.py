#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Date created: 2025-11-21 11:40:00
Date last modified: 2025-12-01 10:54:08
Purpose: Numerically solve the recursion we derived to analytically replicate Keaney et al 2021 Proc B
'''

#%%
#import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
#define recursion
def p_traj(km, kf, beta_o, beta_s, gamma_so, gamma_os, p0 = 0.5,T=100):
    
    '''
    Implement the recursion we derived for sex-specific drive
    with multiple mating and homozygous lethality from the mating table in the supplementary.
    
    Inputs:
        km (float in [0,1]) - what fraction of a heterozygous (EsEo) male's gametes carry the Es allele? 0.5 indicates fair segregation, > 0.5 is drive , < 0.5 is drag
        kf (float in [0,1]) - what fraction of a heterozygous (EsEo female's gametes carry the Es allele? 0.5 indicates fair segregation, > 0.5 is drive , < 0.5 is drag
        beta_o (float in [0,1]) - remating probability of a female who mates with a wildtype (EoEo) male
        beta_s (float in [0,1]) - remating probability of a female who mates with a heterozygous (EsEo) male
        gamma_so (float in [0,1]) - proportion of offspring sired by first male when the heterozygous male mates first
        gamma_os (float in [0,1]) - proportion of offspring sired by first male when the wildtype male mates first
        p0 (float in (0,1)) - Initial allele frequency of the selfish element Es
        T (int > 0) - total time, in number of generations, for which to run the simulation
    
    Output:
        An array of length T+1 containing the trajectory of the allele frequency over time
    '''
    
    #initialize
    p_traj = np.zeros(T+1)
    p_traj[0] = p0
    i = 0
    
    #the recursion step
    while i < T:
        p = 2*p_traj[i] #multiply by two to convert from allele to genotype frequency
        
        #number of Es alleles
        N_s = (1-beta_s)*(p*(1-p))*km + beta_s*(p**2)*(1-p)*km + beta_o*p*((1-p)**2)*km*(1-gamma_os) + beta_s*p*((1-p)**2)*km*gamma_so + (1-beta_o)*p*(1-p)*kf + (1-beta_s)*(p**2)*(kf*(1-km) + km*(1-kf)) + beta_o*p*((1-p)**2)*kf + beta_s*(p**3)*(kf*(1-km) + km*(1-kf)) + beta_o*(p**2)*(1-p)*(gamma_os*kf + (1-gamma_os)*(kf*(1-km)+km*(1-kf))) + beta_s*(p**2)*(1-p)*((1-gamma_so)*kf+(gamma_so)*(kf*(1-km)+km*(1-kf)))
        
        #number of Eo alleles
        N_o = (1-beta_o)*((1-p)**2) + (1-beta_s)*p*(1-p)*(1-km) + beta_o*((1-p)**3) + beta_s*(p**2)*(1-p)*(1-km) + beta_o*p*((1-p)**2)*(gamma_os+(1-gamma_os)*(1-km))+beta_s*p*((1-p)**2)*(1-gamma_so+(gamma_so)*(1-km))+(1-beta_o)*p*(1-p)*(1-kf)+(1-beta_s)*(p**2)*(1-km)*(1-kf)+beta_o*p*((1-p)**2)*(1-kf)+beta_s*(p**3)*(1-kf)*(1-km)+beta_o*(p**2)*(1-p)*(gamma_os*(1-kf)+(1-gamma_os)*(1-kf)*(1-km)) + beta_s*(p**2)*(1-p)*((1-gamma_so)*(1-kf)+(gamma_so)*(1-km)*(1-kf))
        
        #Bruck's original recursion equations, which do not allow multiple mating
        #N_s = p*(1-p)*(km+kf) + (p**2)*(kf*(1-km)+km*(1-kf))
        #N_o = (1-p)**2 + p*(1-p)*(2-km-kf) + (p**2)*(1-kf)*(1-km)


        p_traj[i+1] = 0.5*N_s/(N_s+N_o) #multiply by half to convert from genotype to allele frequency


        i += 1

    return p_traj
# %%

########################
# Replicate Bruck

# Define Bruck parameters

km = 0.9 #segregation ratio to driving allele in males
kf = 0.5 #segretation ratio to driving allele in females

#no remating for Bruck
beta_o = 0 #remating probability when a female is mated with a wildtype (EoEo) male
beta_s = 0 #remating probability when a female is mated with a heterozygous (EsEo) male

gamma_so = 1 #proportion of offspring sired by first male when the heterozygous male mates first
gamma_os = 1 #proportion of offspring sired by first male when the wildtype male mates first

p0 = 0.1 #initial frequency of selfish allele
T = 50 #Total time for which to run the simulation

def bruck_fixed_point(km,kf):
    '''
    Return the equilibrium fixed point we analytically calculated for Bruck's model allowing for drive in females
    '''
    return (0.5 - 0.5*np.sqrt( 1+(1/(km*kf)) - (1/km) - (1/kf) )  )


# %%
#Time series line plots

#Make all labels bold
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams['axes.titleweight'] = "bold"

traj = p_traj(km, kf, beta_o, beta_s, gamma_so, gamma_os,p0, T)
print("eq. freq = "+str(traj[-1]))
plt.plot(range(T+1),traj)
plt.xlabel("Time (in generations)")
plt.ylabel("Frequency of selfish element (p)")
plt.axhline(y=bruck_fixed_point(km,kf),linestyle='--',color='black',label='Equilibrium frequency (p*)')
plt.ylim([0,1])
plt.legend()
plt.savefig('sex_specific_drive_traj.pdf',format='pdf')
plt.show()

# %%
########################
# Replicate Keaney

#Define Keaney parameters

km = 0.944 #segregation ratio to driving allele in males
kf = 0.5 #segretation ratio to driving allele in females

beta_o = 0.3 #remating probability when a female is mated with a wildtype (EoEo) male
beta_s = 0.75 #remating probability when a female is mated with a heterozygous (EsEo) male

p0 = 0.1 #initial frequency of selfish allele
T_final = 100 #Total time for which to run the simulation


# %%
#simulate over a range of gamma_ij values
gammaso_range = np.linspace(0,0.5,100)#.round(4) #range of gamma_ij values to simulate
gammaos_range = np.linspace(0,0.5,100)#.round(4)

my_data = []
for i in range(len(gammaso_range)):
    gamma_so = gammaso_range[i]
    for j in range(len(gammaos_range)):
        gamma_os = gammaos_range[j]
        p_out = p_traj(km, kf, beta_o, beta_s, gamma_so, gamma_os, p0 = 0.1,T=100)[-1]
        my_data.append([gamma_so,gamma_os,p_out])

#Collect the output in dataframe
my_data = pd.DataFrame(my_data)

my_data.columns = ['gamma_so','gamma_os','pstar']

pivoted_data = my_data.pivot(index='gamma_so',columns='gamma_os',values='pstar')

#%%
#plot
hmap = sns.heatmap(pivoted_data.T,
                   xticklabels=20, #plot every 20th value
                   yticklabels=20,
                   #vmax = 0.5,
                   #vmin = 0.1,
                   cmap='crest')


sns.set_theme(rc={'text.usetex' : True})

#hmap.invert_yaxis()
plt.yticks(rotation=0)
hmap.figure.axes[0].set_xlabel(r'$\gamma_{so}$', size=26)
hmap.figure.axes[0].set_ylabel(r'$\gamma_{os}$', size=26)
hmap.figure.axes[-1].set_ylabel('Equilibrium frequency\n of $E_s$ allele ($p^*$)', size=16)

xaxistexts = [f'{float(text._text):.1f}' for text in hmap.get_ymajorticklabels()]
yaxistexts = [f'{float(text._text):.1f}' for text in hmap.get_xmajorticklabels()]

hmap.set_xticklabels(xaxistexts, fontsize = 15)
hmap.set_yticklabels(yaxistexts, fontsize = 15)
#hmap.set_title('$k_m = $'+str(km) + ', $k_f = $'+str(kf)+', $\beta_o = $'+str(beta_o) + ', $\beta_s = $'+str(beta_s))

hfig = hmap.get_figure()
hfig.savefig('multiple_mate_drive_hmap.pdf',format='pdf',bbox_inches='tight')


# %%
