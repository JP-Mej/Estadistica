
import tkinter as tk
from graficas import *


#Interfaz:
raiz = tk.Tk()
raiz.title("Interfaz estadistica")
raiz.geometry("400x300")

titulo=tk.Label(raiz,text="Elija una opcion", font="tahoma")
#crea los botones
boton1=tk.Button(raiz, text="Ojiva de ingresos",command= ojiva_ingreso)
boton2=tk.Button(raiz, text = "Ojiva de egresos", command=ojiva_egreso)
boton3=tk.Button(raiz,text = "Las dos ojivas",command= ojiva_dos)
boton4=tk.Button(raiz,text="Poligono de frecuencia",command= pol)


#posiciona los botones
titulo.pack(pady=5)
boton1.pack(pady=10)
boton2.pack(pady=10)
boton3.pack(pady=10)
boton4.pack(pady=10)

raiz.mainloop()




