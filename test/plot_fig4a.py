# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:16:11 2022
These codes are only to prepare plots
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as mticker

sns.set_style('ticks')

### Load the dataset
dataset = pd.read_csv('IL_51.csv',  delimiter=',', keep_default_na=False, na_values=[''])

print('\t')
print(f'Filetype: {type(dataset)}, Shape: {dataset.shape}')
print(dataset.head(n=10))

### Visualize the dataset
### Set fontsize
fontsize = 20

### Set canvas
fig = plt.figure(figsize=(2, 5), dpi=100)
ax = fig.add_subplot(111)

### Set border width and color
for m in ['top', 'bottom', 'left', 'right']:
    ax.spines[m].set_linewidth(1)
    ax.spines[m].set_color('black')
    
## Plot data
sns.barplot(
    data=dataset,
    x='Metal',
    y='Ext',
    palette=['blue', 'red', 'purple']
    )

X = dataset['Metal']
Y = dataset['Ext']
Err = dataset['Err']

### Set error bar
ax.errorbar(X, Y, xerr=None, yerr=Err, fmt='none', elinewidth=1, ecolor='black', capsize=3, capthick=1)

### Set interval of the canvas
# interval = 10
# ax.set_xlim(min(dataset['Ext']) - 0.5 * interval, max(dataset['Ext']) + 0.5 * interval)
# ax.set_ylim(min(dataset['LogEC50']) - 0.03 * interval, max(dataset['LogEC50']) + 0.15 * interval)
ax.set_ylim(0, 100)

### Set font properties
sizes = [fontsize, 0.7 * fontsize]
fonts = [fm.FontProperties(family='arial', size=sizes[i], weight='normal', style='normal') for i in range(len(sizes))] 

### Set axes labels
ax.set_xlabel('', labelpad=0, fontsize=0)
ax.set_ylabel('$E$ (%)', labelpad=10, fontproperties=fonts[0])

### Set ticker position
ticker_arg = [5, 20, 10, 20]
tickers = [mticker.MultipleLocator(ticker_arg[i]) for i in range(len(ticker_arg))]

# ax.xaxis.set_minor_locator(tickers[0])
# ax.xaxis.set_major_locator(tickers[1])
ax.yaxis.set_minor_locator(tickers[2])
ax.yaxis.set_major_locator(tickers[3])

### Modify fontsize of the ticklabels
xcoord = ax.xaxis.get_major_ticks()
ycoord = ax.yaxis.get_major_ticks()

[(i.label.set_fontproperties('arial'), i.label.set_fontsize(sizes[0])) for i in xcoord]
[(j.label.set_fontproperties('arial'), j.label.set_fontsize(sizes[0])) for j in ycoord]

# ### Set legend
# ax.legend(loc='upper center', ncol=4, title='Predicted Selectivity', title_fontsize=sizes[1], prop=fonts[1], 
#           frameon=True, fancybox=True, shadow=False)

fig.savefig('fig4a.jpg', dpi=300, bbox_inches='tight')
plt.show()
