from tkinter import Button,Tk, Frame, Entry, END

from matplotlib.ft2font import BOLD

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("274x328")
ventana.config(bg="white")
ventana.resizable(0,0)

#hover

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

i=0
def obtener(dato):
    global i
    i = i + 1
    Resultado.insert(i ,dato)

def operacion():
    global i
    
    ecuacion = Resultado.get()
    if i != 0:
        try:
            result = str(eval(ecuacion))
            Resultado.delete(0, END)
            Resultado.insert(0, result)
            longitud = len(result)
            i = longitud
        except:
            result = "Error"
            Resultado.delete(0, END)
            Resultado.insert(0, result)
    else:
        pass

def borrar_uno():
    global i
    Resultado.delete(i, END)
    i = i - 1

def borrar_todo():
    Resultado.delete(0, END)
    i = 0

frame = Frame(ventana, bg="black", relief="raised")
frame.grid(column=0, row=0, padx=6, pady=3)

Resultado = Entry(frame, width=18, relief="groove", bg="#9EF8E8", font=("Monstserrat", 16), justify="right")
Resultado.grid(columnspan=4, row=0, padx=1, pady=3, ipadx=1, ipady=1)

#fila 1

Button1 = HoverButton(frame, text="1", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(1))
Button1.grid(column=0, row=1, padx=1, pady=1)

Button2 = HoverButton(frame, text="2", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(2))
Button2.grid(column=1, row=1, padx=1, pady=1)

Button3 = HoverButton(frame, text="3", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(3))
Button3.grid(column=2, row=1, padx=1, pady=1)

Botton_borrar = HoverButton(frame, text="C", width=5, borderwidth=2, height=2, bg="#FD0371", font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="red", command=borrar_todo)
Botton_borrar.grid(column=3, row=1, padx=2, pady=2)

#fila 2

Button4 = HoverButton(frame, text="4", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(4))
Button4.grid(column=0, row=2, padx=1, pady=1)

Button5 = HoverButton(frame, text="5", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(5))
Button5.grid(column=1, row=2, padx=1, pady=1)

Button6 = HoverButton(frame, text="6", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(6))
Button6.grid(column=2, row=2, padx=1, pady=1)

Button_mas = HoverButton(frame, text="+", width=5, height=2, bg="#2A16F7", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="#FEEF02", command=lambda: obtener("+"))
Button_mas.grid(column=3, row=2, padx=2, pady=2)

#fila 3

Button7 = HoverButton(frame, text="7", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(7))
Button7.grid(column=0, row=3, padx=1, pady=1)

Button8 = HoverButton(frame, text="8", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(8))
Button8.grid(column=1, row=3, padx=1, pady=1)

Button9 = HoverButton(frame, text="9", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(9))
Button9.grid(column=2, row=3, padx=1, pady=1)

Button_menos = HoverButton(frame, text="-", width=5, height=2, bg="#2A16F7", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="#FEEF02", command=lambda: obtener("-"))
Button_menos.grid(column=3, row=3, padx=2, pady=2)

#fila 4

Button0 = HoverButton(frame, text="0", width=5, height=5, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener(0))
Button0.grid(column=0, rowspan=2, row=4, padx=1, pady=1)

Button_punto = HoverButton(frame, text=".", width=5, height=2, bg="#999AB8", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="aqua", command=lambda: obtener("."))
Button_punto.grid(column=1, row=4, padx=1, pady=1)

Button_division = HoverButton(frame, text="/", width=5, height=2, bg="#2A16F7", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="#FEEF02", command=lambda: obtener("/"))
Button_division.grid(column=2, row=4, padx=1, pady=1)

Button_multiplicacion = HoverButton(frame, text="x", width=5, height=2, bg="#2A16F7", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="#FEEF02", command=lambda: obtener("*"))
Button_multiplicacion.grid(column=3, row=4, padx=2, pady=2)

#fila 5

Button_igual = HoverButton(frame, text="=", width=12, height=2, bg="#2FEC71", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="#16FD03", command=operacion)
Button_igual.grid(column=1, columnspan=2,row=5, padx=1, pady=1)

Button_borrar = HoverButton(frame, text="CE", width=5, height=2, bg="#FD5603", borderwidth=2, font=("Comic sens MC", 12, "bold"), anchor="center", relief="raised", activebackground="red", command=borrar_todo)
Button_borrar.grid(column=3, row=5, padx=2, pady=2)

ventana.mainloop()