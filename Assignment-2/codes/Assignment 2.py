from scipy.stats import uniform
import seaborn as sns
sns.set(color_codes=True)
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':(5,5)})
n=10000
#taking expectation value of x 
start=0
end =2
data_uniform=uniform.rvs(size=n,loc=start,scale=end)
ax=sns.distplot(data_uniform,bins=100,kde=True,color='skyblue',hist_kws={"linewidth":15,'alpha':1})
ax.set(xlabel='Interval',ylabel='Probability')
plt.savefig('plot.png',dpi=300,bbox_inches='tight')
plt.show()
