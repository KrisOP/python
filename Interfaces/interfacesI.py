from tkinter import *  #importar libreria


raiz=Tk()#llamada a la clase Tk()

raiz.title("Ventana de pruebas")

#raiz.iconbitmap('.ico')
raiz.iconbitmap(r'C:\Users\KrisOP\Desktop\Phyton\Interfaces\ff.ico')#agregar icono a la ventana
#raiz.geometry("650x350")#definir las dimensiones de la ventana
#raiz.resizable(1,0)#evitar redimencionar la ventana//width y height//podemos utilizar true y false tambien
raiz.config(bg="blue")#cambiar el color de fondo de la pantalla

miFrame=Frame() # construir un frame
miFrame.pack(side="right", anchor="n")#empaquetar el frame para que este en el interior de la raiz//al redimencionar se ancla en la parte derecha y arriba
miFrame.config(bg="red")
miFrame.config(width="650",height="350")
raiz.mainloop()#mainloop es equivalent a un ciclo infinito para mantener la interfaz en continua ejecucion