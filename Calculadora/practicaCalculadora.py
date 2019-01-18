from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()
#***************PANTALLA************************
numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)#asociando variable a la pantalla
pantalla.grid(row=1,column=1, padx=10,pady=10,columnspan=4)#columnspan para que el cuadro ocupe cuatro columnas
pantalla.config(background="black",fg="#03f943",justify="right" )#fg color de letra, justify para ubicar posicion del cursor al escribir en el cuadro de texto

#***************PULSACIONES TECLADO*****************
def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get()+ num)#concatenar lo que existe en el campo con la variable


#***************FILA 1**************************

boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))#ancho de 3
boton9.grid(row=2,column=1)


boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)

boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=3)

botonDiv=Button(miFrame,text="÷",width=3)
botonDiv.grid(row=2,column=4)

#***************FILA 2**************************

#Lambda para funciones anonimas
boton4=Button(miFrame,text=4,width=3,command=lambda:numeroPulsado("4"))#ancho de 3, llamada a la funcion numeroPulsado, con lambda evitamos que se ejecute la funcion sino hasta que se pulse el boton  
boton4.grid(row=3,column=1)

boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)

boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)

botonMulti=Button(miFrame,text="X",width=3)
botonMulti.grid(row=3,column=4)


#***************FILA 3**************************

boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))#ancho de 3
boton1.grid(row=4,column=1)

boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)

boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)

botonMulti=Button(miFrame,text="-",width=3)
botonMulti.grid(row=4,column=4)

#***************FILA 4**************************

botonigual=Button(miFrame,text="=",width=3)#ancho de 3
botonigual.grid(row=5,column=1)

boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=2)

botonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPulsado(","))
botonComa.grid(row=5,column=3)

botonsuma=Button(miFrame,text="+",width=3)
botonsuma.grid(row=5,column=4)
raiz.mainloop()