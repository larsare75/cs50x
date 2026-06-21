import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("ssbmedier.csv", index_col = 0, skiprows = (0, 1), \
    sep =";", na_values=[".", ".."], encoding = "latin-1")
K = []   # lager ei tom liste K 
startVerdi = 2010   # lager variabel for det første årstallet
for i in range(0, 10):
    K.append(startVerdi + i)
data.columns = K  # setter radoverskriftene i variabelen data lik innholdet av lista K 
#print(data)
#print(data.describe())
utdrag=data.iloc[[1,10]]
utdrag=utdrag.transpose()
utdrag.plot().legend(bbox_to_anchor=(1,1))
plt.xlabel("Årstall")
plt.ylabel("Minutter per dag i gjennomsnitt")
plt.title("Tid brukt på fjernsyn og internett 2010–2019")
plt.suptitle("Kilde: Statistisk sentralbyrå", fontsize = 8)
plt.grid(True)
plt.show()
