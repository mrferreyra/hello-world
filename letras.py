# Imprime la frecuencia de letras de un texot


# Inicializo array

letra = [0] * 26

file = open("argentina.txt","r")

for line in file:
	for l in line:
		a = ord(l.upper())
		if(a < 65 or a > 90):
			continue
		letra[a-ord('A')] += 1

# Creo tuplas
t = []
for i in range(0,25):
	t.append((chr(i+ord('A')),letra[i]))

#Las ordeno segun la cantidad de veces que aparecio la letra
t = sorted(t, key=lambda x: x[1], reverse=True)

#Imprimo la lista

#for i in t:
#	print(i[0],' -> ',i[1])

#Grafico de barras de la lista

import matplotlib.pyplot as plt

# plt.bar(list(map(lambda x: x[0],t)),list(map(lambda x: x[1],t)))
labels = list(map(lambda x: x[0],t))
values = list(map(lambda x: x[1],t))

plt.bar(range(len(values)),values,tick_label=labels)
plt.text(15,15000,'Frecuencia de Letras')

plt.show()
