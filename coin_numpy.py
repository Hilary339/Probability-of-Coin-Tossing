import matplotlib.pyplot as plt
import random
import numpy as np
N = 100000000
samples = np.random.choice([0,1],size=N,p=[0.5,0.5])
cum_heads = np.cumsum(samples)
head_frequency = cum_heads/np.arange(1,N+1)

plt.figure(figsize = (8,5))
plt.plot(range(1,N+1),head_frequency)
plt.xlabel("Total number of throws")
plt.ylabel("Heads frequency")
plt.ylim(0,1)
plt.xscale('log')
plt.axhline(y=0.5,color='black', linestyle='dashed')
plt.show()
