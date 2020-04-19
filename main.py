import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

###   Plot Example

# x=np.linspace(0,6,100)
# y=np.exp(-x)*np.sin(4*x)
# plt.plot(x,y)
# plt.show()


###   Time Series Data Objects

mylynx_df = pd.read_csv("LYNXdata.csv", header=0, names=["year", "trappings"], index_col=0)
print(mylynx_df.head(5))
mylynxts = pd.Series(mylynx_df['trappings'].values, index=pd.date_range('31/12/1821', periods=114, freq='A-DEC'))
print(mylynxts.head(10))

nottem_df = pd.read_csv("nottem.csv", header=0, names=["index", "time", "value"], index_col=0)
print(nottem_df.head(5))
nottemts = pd.Series(nottem_df['value'].values, index=pd.date_range('1920-01-31', periods=240, freq='M'))
print(nottemts.head(10))

###   Time Series Visualizations
plt.figure(figsize=(12, 8))
# mylynxts.plot()
plt.title('Lynx Trappings in Canada 1821-1934')
plt.xlabel('Year of Trappings')
plt.ylabel('Number of Lynx Trapped')
plt.legend(['Lynx', 'Cumulative total'])
cumsum_lynx = np.cumsum(mylynxts)
print(cumsum_lynx.head(10))
plt.plot(mylynxts)
plt.plot(cumsum_lynx)
plt.show()

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(mylynxts)
plt.title('Lynx Trappings')
plt.subplot(2, 1, 2)
plt.plot(cumsum_lynx)
plt.title('Cumsum of Lynx')
plt.tight_layout()
plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
mylynxts.plot(ax=ax1)
cumsum_lynx.plot(ax=ax2)
ax1.set_title("Lynx Trappings")
ax2.set_title("Cumsum of Lynx")
plt.tight_layout()
plt.show()
