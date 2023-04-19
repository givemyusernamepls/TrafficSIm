import matplotlib.pyplot as plt
import numpy as np



p= len(l)
T= np.arange(0, 600, 600/p)
plt.ylabel('Durchschnittswert der pro Sekunde stehenden Autos')
plt.xlabel('Zeit in Sekunden')
plt.plot(T, l, '-', color='k')
plt.suptitle('Mittelwert der pro Sekunde stehenden Autos über die Zeit')
plt.title('Ampel mit r= 56 und insgesamt 424 passierten Autos')
plt.ylim(-0.25,50)
plt.show()

