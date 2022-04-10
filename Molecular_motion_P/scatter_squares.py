import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
#In momentul in care modificam range-ul in x_values, de la un numar la altul,
#y_values stocheaza informatia in cifre in functie de cat ai ridicat la putere
#de exexmplu:
# graficul mi se duce pana la 729.0.
#el calculeaza asa: 5*5*5 = stocheaza(125 pe grafic)
#6*6*6 = stocheaza(216 pe grafic)
#7*7*7 = stocheeaza(343 pe grafic)
#8*8*8 = stocheaza(512 pe grafic)
#9*9*9 = 729.0 si se opreste, deoarece pe 10 nu il mai ia in considerare
#deoarece numaratoarea de la face la 5 la 9.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

#Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')