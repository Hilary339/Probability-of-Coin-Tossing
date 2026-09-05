import matplotlib.pyplot as plt
import random
N=100000000
heads = []
head = 0
for i in range(1,N+1):
    if random.random()>0.5:
        head+=1
    heads.append(head/i)
plt.figure(figsize = (8,5))
plt.plot(range(1,N+1),heads)
plt.xlabel("all")
plt.xscale("log")
plt.ylim(0,1)
plt.ylabel("heads")
plt.axhline(y=0.5, color='black', linestyle='dashed')
plt.grid(True)

plt.show()
