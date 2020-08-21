import tkinter as tk

ventana = tk.Tk()
ventana.geometry("380x300")
ventana.title("promedio del estudiante")
ventana.configure(background= '#37474f')
var=tk.DoubleVar()

c1 = tk.Label(ventana, text= "Calificación 1", bg="#ffb74d", fg="white")
c1.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

c2 = tk.Label(ventana, text= "Calificación 2", bg="#ffb74d", fg="#f5f5f5")
c2.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada2 = tk.Entry(ventana)
entrada2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

c3 = tk.Label(ventana, text= "Calificación 3", bg="#ffb74d", fg="#f5f5f5")
c3.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada3 = tk.Entry(ventana, textvariable= entrada1)
entrada3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

def promedioSuma():
    c1 = float(entrada1.get()) + float(entrada2.get()) + float(entrada3.get())
    c1 = c1/3
    return var.set(c1)


resultado= tk.Label(ventana, textvariable = var, padx = 5, pady= 5, width = 50)
resultado.pack()
boton1 = tk.Button(ventana, text= "Resultado", bg = "#42a5f5", command = promedioSuma)
boton1.pack(side= tk.TOP)


c4 = tk.Label(ventana, text= "Nota Examen final", bg="#ffb74d", fg="white")
c4.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada4 = tk.Entry(ventana)
entrada4.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

c5 = tk.Label(ventana, text= "Nota trabajo final", bg="#ffb74d", fg="white")
c5.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada5 = tk.Entry(ventana)
entrada5.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

def porcetajeParcial(promedio):
    return promedioSuma(promedio) * 0.55

c6 = tk.Label(ventana, text= "Promedio de las tres calificaciones", bg="#ffb74d", fg="#f5f5f5")
c6.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada6 = tk.Entry(ventana)

resultado2= tk.Label(ventana, textvariable = var, padx = 5, pady= 5, width = 50)
resultado2.pack()

ventana.mainloop()