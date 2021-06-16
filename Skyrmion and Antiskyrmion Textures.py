#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Skyrmions and antiskyrmions are topologically protected magnetic textures, which are plotted below

#Import libraries
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Define x and y grids
x, y = np.meshgrid(np.linspace(-30,30,30),
                   np.linspace(-30,30,30))

#RC is core radius, nS is n value for skyrmion, c is helicity
RC = 10
nS = -1
c = np.pi/2

#Define theta and phi components of magnetization
#mtheta will apply for both skyrmion and antiskyrmion, while mphi will be defined separately for each
#The formula for mtheta comes from A. Altland and B. Simons, Condensed matter field theory (Cambridge University Press, 2010)
mtheta = 2*np.arctan(RC**2/(x**2+y**2))+np.pi
mphiS = nS*np.arctan2(x,y)-c

#Define x and y components of magnetization for skyrmion
uS = np.sin(mtheta)*np.cos(mphiS)
vS = np.sin(mtheta)*np.sin(mphiS)

#Normalize skyrmion magnetization vectors, where cos(mtheta) is the z-component of magnetization
uS_normalized = uS/np.sqrt(uS**2+vS**2+np.cos(mtheta)**2)
vS_normalized = vS/np.sqrt(uS**2+vS**2+np.cos(mtheta)**2)


# In[6]:


#Skyrmion plot
plt.quiver(x, y, uS_normalized, vS_normalized, color='b')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.axis('equal')
plt.title('Skyrmion',size=15)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.xlabel('x (nm)', size=15)
plt.ylabel('y (nm)', size=15)


# In[4]:


#nAS is n value for antiskyrmion, mphiAS is the phi component of magnetization for antiskyrmion
nAS = 1
mphiAS = nAS*np.arctan2(x,y)-c

#Define x and y components of magnetization for antiskyrmion
uAS = np.sin(mtheta)*np.cos(mphiAS)
vAS = np.sin(mtheta)*np.sin(mphiAS)


#Normalize antiskyrmion magnetization vectors, where cos(mtheta) is the z-component of magnetization
uAS_normalized = uAS/np.sqrt(uAS**2+vAS**2+np.cos(mtheta)**2)
vAS_normalized = vAS/np.sqrt(uAS**2+vAS**2+np.cos(mtheta)**2)


# In[5]:


#Antiskyrmion plot
plt.quiver(x, y, uAS_normalized, vAS_normalized, color='r')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.axis('equal')
plt.title('Antiskyrmion',size=15)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.xlabel('x (nm)', size=15)
plt.ylabel('y (nm)', size=15)

