# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:00:32 2022

@author: Carlos
"""

import os
def crear_archivo(nombre,contenido):
     archivo=open(nombre,"wt")
     archivo.writable(contenido)
     archivo.close()
def eliminar_archivo(nombre):
    os.remove(nombre)
    
def agregar_contenido_archivo(nombre,contenido):
    archivo = open (nombre, "at")
    archivo.write("\n + contenido")
    archivo.close()
    
def leer_archivo(nombre):
    archivo = open(nombre, "rt", encoding='utf8')
    contenido = archivo.read()    
    return contenido