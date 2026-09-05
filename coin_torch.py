import numpy as np
import matplotlib.pyplot as plt
import torch
N = 100000
#构建正反面的概率
fair_probs=torch.tensor([0.5,0.5])
#进行N次试验，replacement=True表示拿过的还可以再拿
samples=torch.multinomial(fair_probs,N,replacement=True)
#累计正面朝上的次数
cum_heads=(samples==0).cumsum(dim=0)
#正面朝上的频率
head_frqc=cum_heads/torch.arange(1,N+1)
head_frqc=head_frqc.numpy()

plt.figure(figsize = (8,5))
plt.plot(range(1,N+1),head_frqc)
plt.xlabel("Total number of throws")
plt.ylabel("Heads frequency")
plt.ylim(0,1)
plt.xscale('log')
plt.axhline(y=0.5,color='black', linestyle='dashed')
plt.show()
