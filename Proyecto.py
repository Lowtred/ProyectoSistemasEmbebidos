#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####################################################
# Proyecto.py
# Author: Ulises Limones Moscoso
# Controlador de dispositivos de una casa
# ## ###############################################

from tkinter import *
#import RPi.GPIO as GPIO
import time
import datetime
import _thread

# Configuracion de pines para Raspberry pi
'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT) # Camaras
GPIO.setup(7, GPIO.OUT) # Foco
GPIO.setup(5, GPIO.IN) #Timbre
GPIO.setup(8,GPIO.OUT) #Foco con atenuacion
pwm_led=GPIO.PWM(8,100)
pwm_led.start(100)
GPIO.setup(10,GPIO.OUT)#Puerta cochera
pwm_motor=GPIO.PWM(10,50)
pwm_motor.start(2.5)
'''
#Programado de encendido y apagado
encendido=0
apagado=0

sinc = _thread.allocate_lock()

raiz=Tk()
raiz.title("Simulador")
cuadro=Frame(raiz,widt=500,height=400)
cuadro.pack()
##Acciones
def Revision():
  Verifica1=1
  Verifica2=1
  
  while True:
    sinc.acquire()
    global encendido
    global apagado
    # Deteccion de timbre (Falta aplicarlo en todo momento)
    #if GPIO.input(5) == GPIO.HIGH:
    #    print("Timbre activo")
    # Apagado y encendido automatico
    Hora=int(datetime.datetime.strftime(datetime.datetime.now(),'%H'))
    if Hora==encendido and Verifica1==1:
      print("encendido")
      Verifica1=0
      Verifica2=1
      #GPIO.output(7, GPIO.HIGH)
      EncenderFoco()
      #pwm_led.ChangeDutyCycle(100)
      
    if Hora==apagado and Verifica2==1:
      print("apagado")
      Verifica1=1
      Verifica2=0
      #GPIO.output(7, GPIO.LOW)
      ApagarFoco()
      #pwm_led.ChangeDutyCycle(0)   
    time.sleep(1)
    sinc.release()

_thread.start_new_thread(Revision, ())
      
def IntensidadFoco():
    try:
      opcion=int(cuadroTexto1.get())
      if opcion>=0 and opcion<=100:
        #pwm_led.ChangeDutyCycle(opcion)
        texto="Foco a "+str(opcion)+"% de brillo"
        escribirTexto=Label(cuadro,text=texto)
        escribirTexto.grid(row=8,column=1)
        
      else:
        escribirTexto=Label(cuadro,text="Opcion no valida")
        escribirTexto.grid(row=8,column=1)
    except:
        escribirTexto=Label(cuadro,text="Opcion no valida")
        escribirTexto.grid(row=8,column=1)
    #Imagenes del simulador
    if opcion>=0 and opcion<20:
        Foco1=PhotoImage(file="FocoApagado.PNG")
        imgLabel=Label(cuadro,image=Foco1).grid(row=10,column=1)
        imgLabel.image="FocoApagado.PNG"
    if opcion>=20 and opcion<40:
        Foco1=PhotoImage(file="Foco20p.PNG")
        imgLabel=Label(cuadro,image=Foco1).grid(row=10,column=1)
        imgLabel.image="Foco20p.PNG"
    if opcion>=40 and opcion<60:
        Foco1=PhotoImage(file="Foco40p.PNG")
        imgLabel=Label(cuadro,image=Foco1).grid(row=10,column=1)
        imgLabel.image="Foco40p.PNG"
    if opcion>=60 and opcion<80:
        Foco1=PhotoImage(file="Foco60p.PNG")
        imgLabel=Label(cuadro,image=Foco1).grid(row=10,column=1)
        imgLabel.image="Foco60p.PNG"
    if opcion>=80 and opcion<100:
        Foco1=PhotoImage(file="Foco80p.PNG")
        imgLabel=Label(cuadro,image=Foco1).grid(row=10,column=1)
        imgLabel.image="Foco80p.PNG"
    if opcion==100:
        Foco1=PhotoImage(file="Foco100p.PNG")
        imgLabel=Label(cuadro,image=Foco1).grid(row=10,column=1)
        imgLabel.image="Foco100p.PNG"
    
def EncendidoAutom():
    global encendido
    try:
      opcion=int(cuadroTexto2.get())
      if opcion>=0 and opcion<=24:
        encendido=opcion
        texto="Encendido automatico a las "+str(opcion)+"hrs"
        escribirTexto=Label(cuadro,text=texto)
        escribirTexto.grid(row=8,column=1)
      else:
          escribirTexto=Label(cuadro,text="Opcion no valida")
          escribirTexto.grid(row=8,column=1)
    except:
        escribirTexto=Label(cuadro,text="Opcion no valida")
        escribirTexto.grid(row=8,column=1)
    
def ApagadoAutom():
    global apagado
    try:
      opcion=int(cuadroTexto3.get())
      if opcion>=0 and opcion<=24:
        apagado=opcion
        texto="Apagado automatico a las "+str(opcion)+"hrs"
        escribirTexto=Label(cuadro,text=texto)
        escribirTexto.grid(row=8,column=1)
      else:
        escribirTexto=Label(cuadro,text="Opcion no valida")
        escribirTexto.grid(row=8,column=1)
    except:
        escribirTexto=Label(cuadro,text="Opcion no valida")
        escribirTexto.grid(row=8,column=1)
    
def EncenderCamaras():
    #GPIO.output(3, GPIO.HIGH)
    escribirTexto=Label(cuadro,text="      Camaras Encendidas      ")
    escribirTexto.grid(row=8,column=1)
    camara=PhotoImage(file="Encendido.PNG")
    imgLabel=Label(cuadro,image=camara).grid(row=10,column=1)
    imgLabel.image="Encendido.PNG"
  
    
def ApagarCamaras():
    #GPIO.output(3, GPIO.LOW)
    escribirTexto=Label(cuadro,text="      Camaras Apagadas      ")
    escribirTexto.grid(row=8,column=1)
    camara=PhotoImage(file="Apagado.PNG")
    imgLabel=Label(cuadro,image=camara).grid(row=10,column=1)
    imgLabel.image="Apagado.PNG"
 
def EncenderFoco():
    #GPIO.output(7, GPIO.HIGH)
    escribirTexto=Label(cuadro,text="      Foco Encendido      ")
    escribirTexto.grid(row=8,column=1)
    Foco2=PhotoImage(file="Foco100p.PNG")
    imgLabel2=Label(cuadro,image=Foco2).grid(row=10,column=1)
    imgLabel2.image="Foco100p.PNG"
    
def ApagarFoco():
    #GPIO.output(7, GPIO.LOW)
    escribirTexto=Label(cuadro,text="      Foco Apagado      ")
    escribirTexto.grid(row=8,column=1)
    Foco2=PhotoImage(file="FocoApagado.PNG")
    imgLabel2=Label(cuadro,image=Foco2).grid(row=10,column=1)
    imgLabel2.image="FocoApagado.PNG"
    
def AbrirCochera():
    #pwm_motor.ChangeDutyCycle(7.5)
    escribirTexto=Label(cuadro,text="      Cochera Abierta      ")
    escribirTexto.grid(row=8,column=1)
    Porton=PhotoImage(file="Abierto.PNG")
    imgLabel3=Label(cuadro,image=Porton).grid(row=10,column=1)
    imgLabel3.image="Abierto.PNG"
    
def CerrarCochera():
    #pwm_motor.ChangeDutyCycle(2.5)
    escribirTexto=Label(cuadro,text="      Cochera Cerrada      ")
    escribirTexto.grid(row=8,column=1)
    Porton=PhotoImage(file="Cerrado.PNG")
    imgLabel3=Label(cuadro,image=Porton).grid(row=10,column=1)
    imgLabel3.image="Cerrado.PNG"
    
def SonarTimbre():
    escribirTexto=Label(cuadro,text="            Timbre Sonando           ")
    escribirTexto.grid(row=8,column=1)
    
##Interfaz
etiqueta1=Label(cuadro,text="Intensidad Foco1(0 a 100):")
etiqueta1.grid(row=1,column=0)
cuadroTexto1=Entry(cuadro)
cuadroTexto1.grid(row=1,column=1)
pos1=Label(cuadro,text=".")
pos1.grid(row=1,column=2)
aceptar1=Button(pos1,text="Aceptar",command=IntensidadFoco)
aceptar1.pack()

etiqueta2=Label(cuadro,text="Encendido Autom.(0 a 24):")
etiqueta2.grid(row=2,column=0)
cuadroTexto2=Entry(cuadro)
cuadroTexto2.grid(row=2,column=1)
pos2=Label(cuadro,text=".")
pos2.grid(row=2,column=2)
aceptar2=Button(pos2,text="Aceptar",command=EncendidoAutom)
aceptar2.pack()

etiqueta3=Label(cuadro,text="Apagado Autom.(0 a 24):")
etiqueta3.grid(row=3,column=0)
cuadroTexto3=Entry(cuadro)
cuadroTexto3.grid(row=3,column=1)
pos3=Label(cuadro,text=".")
pos3.grid(row=3,column=2)
aceptar3=Button(pos3,text="Aceptar",command=ApagadoAutom)
aceptar3.pack()

etiqueta4=Label(cuadro,text="Camaras:")
etiqueta4.grid(row=4,column=0)
pos41=Label(cuadro,text=".")
pos41.grid(row=4,column=1)
pos42=Label(cuadro,text=".")
pos42.grid(row=4,column=2)
encender1=Button(pos41,text="Encender",command=EncenderCamaras)
encender1.pack()
apagar1=Button(pos42,text="Apagar",command=ApagarCamaras)
apagar1.pack()

etiqueta5=Label(cuadro,text="Foco2:")
etiqueta5.grid(row=5,column=0)
pos51=Label(cuadro,text=".")
pos51.grid(row=5,column=1)
pos52=Label(cuadro,text=".")
pos52.grid(row=5,column=2)
encender2=Button(pos51,text="Encender",command=EncenderFoco)
encender2.pack()
apagar2=Button(pos52,text="Apagar",command=ApagarFoco)
apagar2.pack()

etiqueta6=Label(cuadro,text="Cochera:")
etiqueta6.grid(row=6,column=0)
pos61=Label(cuadro,text=".")
pos61.grid(row=6,column=1)
pos62=Label(cuadro,text=".")
pos62.grid(row=6,column=2)
encender3=Button(pos61,text="Abrir",command=AbrirCochera)
encender3.pack()
apagar3=Button(pos62,text="Cerrar",command=CerrarCochera)
apagar3.pack()

postimb=Label(cuadro,text=".")
postimb.grid(row=9,column=1)
encender3=Button(postimb,text="Timbre",command=SonarTimbre)
encender3.pack()

etiqueta7=Label(cuadro,text="Alertas:")
etiqueta7.grid(row=7,column=0)
##Avisos
escribirTexto=Label(cuadro,text="Bienvenido")
escribirTexto.grid(row=8,column=1)
escribirTexto.config(bg="white")
escribirTexto.config(width="40",height="5")


raiz,mainloop()
