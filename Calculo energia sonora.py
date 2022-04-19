#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


tt, pp = np.loadtxt('primeiropulsodb.txt', unpack=True)
ppdB=(((pp*166/100)+130)/10)#normalização dos dados brutos de dBa para dB
Pot=np.float_power(10,ppdB)*np.float_power(10,-12)*2*np.pi*0.04
Wk=np.trapz(Pot,tt)
print ("Integral da Potência:", Wk,"J")
#Ww =W-0.5*np.float_power(10, -22)
plt.xlabel("Tempo(s)")
plt.ylabel("Potência (W)")
plt.plot(tt,Pot)
