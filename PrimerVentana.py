#se integra la librería "tkinter" con un *. El * funciona como comodín que indica que debe de traer todos los comoponentes de tkinter
#si solo se quiere incorporar un componente, por ejemplo un boton, sería de la siguiente manera seguido de la declaración de la librería:
#from tkinter import button
from tkinter import *
#para empezar a ejecutar la ventana, definimos el nombre la ventana, en este caso "Raiz" seguido de la funcion Tk()
Raiz = Tk()
#la función geometry sirve para definir el tamaño (en píxeles en el eje de la X y en el eje de la Y) de la ventana
Raiz.geometry("500x500")
#resizable en False: bloquea la función de ampliación de la ventana. Al igual que geometry, se maneja en los ejes de las X y Y.
Raiz.resizable(False,False)
#la función title, sirve para colocar el nombre de la ventana
Raiz.title("Mi primer ventana en tkinter")

#para ciclar la ventana, se usa la funcion mainloop(), en caso de no colocarlo no funcionaría el programa.
Raiz.mainloop()