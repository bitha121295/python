#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  horas.py
#  
#  Copyright 2016 user <user@computoB3>
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
class Datos:
	def horas(self):
		self.horas=float(raw_input("Horas trabajadas por dia: "))
		self.horasExtra=float(raw_input("Horas Extras: "))
		self.valorHora=float(raw_input("Pago por hora: "))
		self.valorHoraExtra=float(raw_input("Pago por hora Extra: "))
	def descuentos(self):
		self.renta=float(raw_input("RENTA: "))
		self.isss=float(raw_input("ISSS: "))
		self.afp=float(raw_input("AFP: "))
class calcular(Datos):
	def calcular_pago(self):
		horasAlMes=self.horas*30
		self.pagoHorasExtras=self.horasExtra*self.valorHoraExtra
		self.pagoHorasNormales=horasAlMes*self.valorHora 
		self.pagoFinalBruto=(self.pagoHorasExtras+self.pagoHorasNormales)
		self.pagoFinalNeto=self.pagoFinalBruto-self.pagoFinalBruto*(self.isss+self.afp+self.renta)
	def imprimir(self):
		print "Horas extras",self.pagoHorasExtras
		print self.pagoHorasNormales
		print self.pagoFinalBruto
		print self.pagoFinalNeto
calculos=calcular()
calculos.horas()
calculos.descuentos()
calculos.calcular_pago()
calculos.imprimir()				
		
		
			
