#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mixto_congruencial.py
#  
#  Copyright 2016 Dell <abby@dell-Inspiron-3521>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
print "--------------------------------MENU------------------------------------"
print "1) Método Congruencial Mixto o Lineal [Xn+1 = (a*Xn + c)]"
print "2) Método Congruencial Mixto o Lineal [Xn+1 = (a*Xn)]"
print ""
print ""
n = input(" Ingrese el numero 1,2,3 dependiendo del metodo que desee:  " )
print ""
print ""
def congruencialmixto():
	print "" 
	print "Método Congruencial Mixto o Lineal [Xn+1 = (a*Xn + c)]"
	print "------------------------------------------------------"
	n = input("Ingrese la cantidad de numeros aleatorios a generar : ") #es la semilla
	Xo = input("Ingrese el valor para la semilla Xo: ") #es la semilla
	a = input("Ingrese el valor para el multiplicador a: ") #el multiplicador
	c = input("Ingrese el valor para la constante aditiva c: ") #la constante aditiva 
	m = input("Ingrese el valor para el modulo m: ") #el modulo
	print ""
	print ""
	if m <= Xo or m <= a or m <= c:
		print "Error no se cumple la condición: (m > Xo, a, c)"
	else:
		if Xo <= 0 or a <=0 or c <=0:
			print "Error no se cumple la condición: (Xo, a, c >0)" 
		else:
			print ""
			print "n|","Xn+1|","Aleatorios"
			print ""
			i = 1
			while i <= n:
				Xo = float((a*Xo + c) % m)# valor para Xn
				aleatorio = float(Xo/m)#generando numero aleatorio
				lista = [i, Xo, aleatorio]#lista 
				print lista#imprimiendo lista
				i+=1#incrementando el valor de i 
def congruencialmultiplicativo(): 
	print "Método Congruencial Multiplicativo [Xn+1 = (a*Xn)]"
	print "------------------------------------------------------"
	n = input("Ingrese la cantidad de numeros aleatorios a generar : ") #es la semilla
	Xo = input("Ingrese el valor para la semilla Xo: ") #es la semilla
	a = input("Ingrese el valor para el multiplicador a: ") #el multiplicador
	m = input("Ingrese el valor para el modulo m: ") #el modulo
	print ""
	print ""
	if m <= Xo or m <= a:
		print "Error no se cumple la condición: (m > Xo, a, c)"
	else:
		if Xo <= 0 or a <=0:
			print "Error no se cumple la condición: (Xo, a, c >0)" 
		else:
			print ""
			print "n|","Xn+1|","Aleatorios"
			print ""
			i = 1
			while i <= n:
				Xo = float((a*Xo) % m)# valor para Xn
				aleatorio = float(Xo/m)#generando numero aleatorio
				lista = [i, Xo, aleatorio]#lista 
				print lista#imprimiendo lista
				i+=1#incrementando el valor de i 
						
if n ==1:
	congruencialmixto()
elif n == 2:
	congruencialmultiplicativo()
else:
	print "!!!Error Opcion invalida!!!"
