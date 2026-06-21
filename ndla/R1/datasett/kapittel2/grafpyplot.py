import numpy as np
from matplotlib import pyplot as pyp

x=np.linspace(-2,6,90)
f=(x-2)**2-4
pyp.plot(x,f,label="$f(x) = (x-2)^2-4$")

pyp.grid(True)
pyp.gca().spines['right'].set_visible(False)
pyp.gca().spines['top'].set_visible(False)
pyp.gca().spines['bottom'].set_position("zero")
pyp.gca().spines['left'].set_position("zero")

pyp.xlabel("$x$") # Tittel på x-aksen
pyp.ylabel("$y$", rotation=0)
pyp.gca().yaxis.set_label_coords(0.3,1)
pyp.gca().xaxis.set_label_coords(1,0.23)


# Lager tekstboks med funksjonsuttrykk
pyp.legend(bbox_to_anchor=(0.6,0.5))


pyp.show()


#print(x)