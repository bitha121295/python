def saludo():
    print"ESTAMOS APRENDIENDO FUNCIONES EN PYTHON"
    print"TODAVIA ESTOY EN LA FUNCION SALUDO"
saludo()
def multiplo(x,y): #aca se declaran los argumentos
    print x*y
multiplo(2,8) #aca se pasan los arguemntos
def multiplicacion(i,z=0):
    print "valor de i =",i
    print "valor de z =",z
    return i * z
print multiplicacion(i=2,z=4)
def multiples(*args):
    print args
multiples("1,2,3,4,5,6") #definiendo multiples argumentos
lista=[1,"dos",False,[45,"cien"]]#definiendo la lista
lista[1]=5 #asociamos el numero 5 al elemento con indice 1 de la lista
num=lista[1]#le asignamos a la variable num elemento con indice de uno
print num #para ver el cambio del nuevo elemento
print lista #para ver como queda el cambio de la lista
lista =[1,"dos",False,[45,"cien"]] #vamos a particionar una lista
ejemplo=lista[0:3:2]
print ejemplo
lista2=[1,"dos",False,[45,"cien"]]
lista2[0:2]=[5,"mil"] #estamos modificano una fraccion de una lista
print lista2
nombres=["Culbert""Alexander""Martin""Lorena""Natalia"]
print nombres[-1] #nosdevuelve el ultimo elemento de nuestra lista
def duplicado(lista3):
    new_list=list(set(lista3))
    if len(new_list)!=len(lista3):
        return True #retornando True si hay duplicados
    else:
            return False #retorna false si no hay duplicado bueno esto es una creacion de lsita con funciones
print duplicado
def multiplo(x,y): #aca se declaran los argumentos
    print x*y
multiplo(2,8) #aca se pasan los arguemntos
def multiplicacion(i,z=0):
    print "valor de i =",i
    print "valor de z =",z
    return i * z
print multiplicacion(i=2,z=4)
def multiples(*args):
    print args
multiples("1,2,3,4,5,6") #definiendo multiples argumentos
lista=[1,"dos",False,[45,"cien"]]#definiendo la lista
lista[1]=5 #asociamos el numero 5 al elemento con indice 1 de la lista
num=lista[1]#le asignamos a la variable num elemento con indice de uno
print num #para ver el cambio del nuevo elemento
print lista #para ver como queda el cambio de la lista
lista =[1,"dos",False,[45,"cien"]] #vamos a particionar una lista
ejemplo=lista[0:3:2]
print ejemplo
lista2=[1,"dos",False,[45,"cien"]]
lista2[0:2]=[5,"mil"] #estamos modificano una fraccion de una lista
print lista2
nombres=["abigail""ashley ""kelly""alex "Natalia"]
print nombres[-1] #nosdevuelve el ultimo elemento de nuestra lista
def duplicado(lista3):
    new_list=list(set(lista3))
    if len(new_list)!=len(lista3):
        return True #retornando True si hay duplicados
    else:
            return False #retorna false si no hay duplicado bueno esto es una creacion de lsita con funciones
print duplicado
url =raw_input("ingresa a la direccion web del blog:")
print "http://www.pythondiario.com"
print "gracias por visitar la pagina",url
suma =input("Ingrese la suma deseada:")
print""
print "la suma es:",suma
