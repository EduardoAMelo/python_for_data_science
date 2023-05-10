import matplotlib.pyplot as plt
import random
notas_matematica = []

for notas in range(8):
  notas_matematica.append(random.randrange(0,11))
x= list(range(1, 9))
y= notas_matematica

plt.plot(x, y, marker='o')
plt.title('matplot1')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.savefig('matplot1/notas.png')
