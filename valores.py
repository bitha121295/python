#! /usr/bin/env python
# -*- coding: utf-8 -*-
def maximo(x,y):
    if x>y:
		return x
    else:
		return y
valor1=int(raw_input("valor1:"))
valor2=int(raw_input("valor2:_"))
print "el valor maximo es ",maximo(valor1,valor2)
