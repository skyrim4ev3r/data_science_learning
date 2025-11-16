import numpy as np

x = [1, 2, 3, 4, 3, 2, 1]

print(np.mean(x), sum(x)/ len(x))

mean_x = sum(x)/ len(x)
var = 0
for num in x:
    var += (num - mean_x) ** 2
var /= (len(x) - 1)
print("variance: {}  {}  {}".format(np.var(x), np.var(x, ddof=1), var)) # Delta Degrees of Freedom: in np defaul is 1/n
#ddof=1 is unbiased, but in larger dataset it desnt matter 1/1_000_000 vs 1/1_000_001
# check variance, standard deviasion, mean abs value

print(np.mean(x))
sample = np.random.choice(x, size=3, replace=True)
print(np.mean(sample))
###########################################################
import matplotlib.pyplot as plt

n = 1000
sample_means = np.zeros(n)

for i in range(n):
    sample_means[i] = np.mean(np.random.choice(x, size=3, replace=True))

popmean = np.mean(x)

plt.hist(sample_means, bins=40, density=True)
plt.plot([popmean, popmean], [0, .3], 'm--')
plt.ylabel('Count')
plt.xlabel('Sample mean')
plt.show()