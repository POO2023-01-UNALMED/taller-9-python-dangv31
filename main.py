import tkinter
from tkinter import Tk, Button, Label

# Metodos
resultado = False
def agregar(opcion):
    global resultado
    if opcion != "=" and resultado == False:
        entrada.set(entrada.get() + opcion)
    elif resultado:
        entrada.set(opcion)
        resultado = False
    else:
        resultado = True
        entrada.set(eval(entrada.get()))
# Configuración ventana principal
root = Tk()
root.title("Hola")
root.resizable(0,0)
root.geometry("")

# Configuración pantalla de salida
entrada = tkinter.StringVar()
pantalla = Label(root, width=19, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"), textvariable=entrada)
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=0, pady=0)
boton_1.bind("<Button-1>", lambda p: agregar("1"))
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=0, pady=0)
boton_2.bind("<Button-1>", lambda p: agregar("2"))
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=0, pady=0)
boton_3.bind("<Button-1>", lambda p: agregar("3"))
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=0, pady=0)
boton_4.bind("<Button-1>", lambda p: agregar("4"))
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=0, pady=0)
boton_5.bind("<Button-1>", lambda p: agregar("5"))
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=0, pady=0)
boton_6.bind("<Button-1>", lambda p: agregar("6"))
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=0, pady=0)
boton_7.bind("<Button-1>", lambda p: agregar("7"))
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=0, pady=0)
boton_8.bind("<Button-1>", lambda p: agregar("8"))
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=0, pady=0)
boton_9.bind("<Button-1>", lambda p: agregar("9"))
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=0, pady=1)
boton_igual.bind("<Button-1>", lambda p: agregar("="))
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=0, pady=1)
boton_punto.bind("<Button-1>", lambda p: agregar("."))
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=0, pady=1)
boton_mas.bind("<Button-1>", lambda p: agregar("+"))
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=0, pady=1)
boton_menos.bind("<Button-1>", lambda p: agregar("-"))
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=0, pady=1)
boton_multiplicacion.bind("<Button-1>", lambda p: agregar("*"))
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=0, pady=1)
boton_division.bind("<Button-1>", lambda p: agregar("/"))

root.mainloop()