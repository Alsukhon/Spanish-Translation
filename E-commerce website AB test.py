from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import warnings
%matplotlib inline
warnings.filterwarnings("ignore")


# Import both data files
df = pd.read_csv(r"C:\Users\Mohammad\Documents\Thinkful\13.10 Capstone 2  - narrative analytics and experimentation\spanish_translation\test_table.csv")
users = pd.read_csv(r"C:\Users\Mohammad\Documents\Thinkful\13.10 Capstone 2  - narrative analytics and experimentation\spanish_translation\user_table.csv")

# Merge dataframes and delete them after
data = pd.merge(df, users , how='inner', on="user_id")
del df
del users
data.head()
len(data)

# Produce a summary dataframe, grouped by Country and test group with counts of each group:
sample_sizes = data[['country','test','conversion']].groupby(['country','test'], as_index=False).count()

# Produce a similar dataframe containing conversion ratios of each group:
conversions = data[['country','test','conversion']].groupby(['country','test'],as_index=False).sum()

# Merge dataframes, rename columns, re-index the new dataframe to have country column as index
summary = pd.merge(sample_sizes,conversions,on=['country','test'])
summary = summary.rename(columns={'conversion_x':'sample_size','conversion_y':'conversion'})


# Add a conversion ratio column, where the ratio = conversion/sample size
summary['conv_ratio'] = summary['conversion']/summary['sample_size']
summary

Arg_Uru = (len(data[data['country']=='Argentina'])+len(data[data['country']=='Uruguay']))/len(data)*100
print(str(round(Arg_Uru,2))+'%')




# Remove observations from the 3 countries from the 'data' dataframe
data = data[data['country'] != 'Spain']
data = data[data['country'] != 'Argentina']
data = data[data['country'] != 'Uruguay']

# Remove observations from the 3 countries from the 'summary' dataframe
summary = summary[summary['country'] != 'Argentina']
summary = summary[summary['country'] != 'Spain']
summary = summary[summary['country'] != 'Uruguay']

print('data: {}'.format(len(data)))
print('summary: {}'.format(len(summary)))

# Parse date column values to datetime
data["date"] = pd.to_datetime(data["date"], infer_datetime_format=True)

# Plot our dataframe
fig = data[data.test==1][
    ['date', 'conversion']].groupby('date').mean().plot()
data[data.test==0][
    ['date', 'conversion']].groupby('date').mean().plot(ax=fig)
plt.legend(['test','control'])
plt.title('Conversion Rates by Date')
plt.ylabel("Conversion")
plt.show()


# Power test to determine sample size for a certain stat power & significance level:
def sample_power_probtest(p1, p2, power=0.8, sig=0.05):
    z = stats.norm.isf([sig/2]) #two-sided t test
    zp = -1 * stats.norm.isf([power]) 
    d = (p1-p2)
    s =2*((p1+p2) /2)*(1-((p1+p2) /2))
    n = s * ((zp + z)**2) / (d**2)
    return int(round(n[0]))

p1 = data[data['test']==1]['conversion'].mean()
p2 = data[data['test']==0]['conversion'].mean()
sample_power_probtest(p1, p2)


# Compute t-test for each day of the experiment and display them in lists along with p-values
statistic_list = []
for date in data.date.unique():
    dated_data = data[data.date == date]
    statistic = (list(stats.ttest_ind(dated_data[dated_data.test == 1].conversion,
                          dated_data[dated_data.test == 0].conversion)))
    statistic[1] = "%.16f" % statistic[1]
    statistic_list.append(statistic)
print(statistic_list)



test_diff = []
ctrl_diff = []

# Subtract control & test sample sizes and get the maximum difference we accepted:
for val in np.unique(summary['country']):
        control = summary[summary['country']==val]['sample_size'].iloc[0]  
        test = summary[summary['country']==val]['sample_size'].iloc[1]
        c_diff = round(abs(test-control)/control*100,1)
        t_diff = round(abs(test-control)/test*100,1)
        ctrl_diff.append(c_diff)
        test_diff.append(t_diff)
        
print ('Max difference for control: '+str(max(ctrl_diff))+'%')
print ('Max difference for test: '+str(max(test_diff))+'%')