import numpy as np
from regex import P
from scipy.stats import poisson

p=poisson.pmf(10,10)
print(p)
p=poisson.pmf(8,10)
print(p)
p=poisson.cdf(5,10)
print(p)
p=poisson.sf(15,10)
print(p)

p=poisson.cdf(15,10)
t = poisson.cdf(6,10)
print(p-t)

