cuenta = [1, 2, 3, 4, 5,]
frutas = ['mangos', 'naranjas', 'peras', 'guayabas' ]
cambio = [1, 'centavo', 2, 'cuatro', 3, 'dolar']
perros = ['collie', 'maltez', 'labrador', 'retriever', 'pastor', 'aleman' ]
for numero in cuenta:
    print "Numeros %d" %numero



for fruta in frutas:
    print "una fruta de tipo: %s" %fruta




for i in cambio:
    print "tengo %r" %i



    elementos = []




for i in range(0, 9):
    print "agregar %d a la lista.2" % i
    elementos.append(i)


for i in elementos:
    print "	Elementos agregado: %d" % i




for index, perro in enumerate(perros):
    place = str(index)
    print("posicion: " + place + "Perro Raza: " + perro.title())



