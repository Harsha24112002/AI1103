import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import exp

dx=0.005
x=np.arange(0,4.5,dx)
y1=(1/3)*(np.exp(-(x/3)))
y2=0.2*(np.exp(-(x/5)))
cdf1=np.cumsum(y1*dx)
cdf2=np.cumsum(y2*dx)
calculated1=(exp(-1.5))
calculated2=exp(-0.9)
print("The experimental value for probability of type 1 error is: ")
print(1-cdf1[len(cdf1)-1])
print("The calculated value for probability of type 1 error is: ")
print(calculated1)
print("The absolute difference between the calculated and experimental values for the probability of the type 1 error is: ")
print(abs(calculated1-(1-cdf1[len(cdf1)-1])))
print("The experimental value for power of the test is : ")
print(1-cdf2[len(cdf2)-1])
print("The calculated value for power of the test is : ")
print(calculated2)
print("The absolute difference between the calculated and experimental values for the power of the test is: ")
print(abs(calculated2-(1-cdf2[len(cdf2)-1])))






