import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("reiser.csv", index_col = 0, skiprows = (0, 1), \
    sep =";", na_values=[".", ".."], encoding = "latin-1")
#print(data)
#data.columns = ["2018K3","2018K4","2019K1","2019K2","2019K3","2019K4","2020K1","2020K2"]
data.columns= data.columns.str.replace("Personer ","")
data=data.transpose()
ax=data.plot(figsize=(12,6))
ax.legend(loc='center left',bbox_to_anchor = (1.02,0.5))
plt.xticks(fontsize=8)  

plt.grid(True)
plt.tight_layout()
plt.show()


