#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pokar_AG12024.py
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
#! /usr/bin/env python

#  Ejercicio de poker en python y las reglas del juego son
# todos diferentes.	
# 2 num repetidos: par
# 2 repeticiones de cada uno: 2 pares
# 3 repeticiones: tercia
# 1 par y un trio: full
# 4 repeticiones: poker
# todo repetido: pocarin

import random #importando la funcion random
print"/*-----------------------RESULTADO------------*/"
print"/*--------------------------------------------*/"
num_carta=int(raw_input("Numero: "))
for i in range(5):#usando el fot con range 5 porque me pide 5 digitos
	carta= str(num_carta)#convierto carta en cadena
	tercia=0;#tercia es igual a cero
	espar=0;#par es igual a cero
	poker=0#poker es igual a cero
	pokarin=0#pocarin es igual a cero
	cero=carta.count('0')# count es un entero que se representa por la cantidad de apariciones de subcadena dentro de la cadena carta
	uno=carta.count('1')
	dos=carta.count('2')
	tres=carta.count('3')
	cuatro=carta.count('4')
	cinco=carta.count('5')
	seis=carta.count('6')
	siete=carta.count('7')
	ocho=carta.count('8')
	nueve=carta.count('9')
if cero==2:
	espar+=1  
if  uno==2:
	espar+=1 
if 	dos==2: 
	espar+=1 
if 	tres==2: 
	espar+=1 
if 	cuatro==2: 
	espar+=1 
if 	cinco==2:
	espar+=1 
if 	seis==2: 
	espar+=1 
if 	siete==2: 
	espar+=1 
if  ocho==2:
	espar+=1  
if 	nueve==2:
	espar+=1 

if cero==3 or uno==3 or dos==3 or tres==3 or cuatro==3 or cinco==3 or seis==3 or siete==3 or ocho==3 or nueve==3:

	print("Es Tercia")
	tercia=1
if espar==2:
	print("dos repeticiones de cada uno asi que son""dos pares")
	
elif espar==1:
	if tercia==1:
		print "un par y un trio  es  full"
	else:
		print "tienes dos numeros repetidos por lo tanto tienes un par";	
if cero==4 or uno==4 or dos==4 or tres==4 or cuatro==4 or cinco==4 or seis==4 or siete==4 or ocho==4 or nueve==4:
	print "Tienes cuatro repeticiones por lo tanto tienes poker";
	poker=1
if cero==5 or uno==5 or dos==5 or tres==5 or cuatro==5 or cinco==5 or seis==5 or siete==5 or ocho==5 or nueve==5:
	print "todos los numeros repetidos asi que es un Pokarin";
	pokarin=1
if espar==0 and pokarin==0 and poker==0 and tercia==0:
	print "el resultado es Todos Diferentes";



