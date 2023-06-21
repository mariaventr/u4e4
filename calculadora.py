from tkinter import *
from tkinter import ttk, messagebox
from functools import partial

class Imaginario:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return Imaginario(real, imaginario)

    def __sub__(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return Imaginario(real, imaginario)

    def __mul__(self, otro):
        real = (self.real * otro.real) - (self.imaginario * otro.imaginario)
        imaginario = (self.real * otro.imaginario) + (self.imaginario * otro.real)
        return Imaginario(real, imaginario)

    def __truediv__(self, otro):
        denominador = (otro.real ** 2) + (otro.imaginario ** 2)
        real = ((self.real * otro.real) + (self.imaginario * otro.imaginario)) / denominador
        imaginario = ((self.imaginario * otro.real) - (self.real * otro.imaginario)) / denominador
        return Imaginario(real, imaginario)

class CalculadoraImaginarios:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de Números Imaginarios")

        self.__numero1 = StringVar()
        self.__numero2 = StringVar()
        self.__resultado = StringVar()

        self.__ventana.columnconfigure(0, weight=1)
        self.__ventana.columnconfigure(1, weight=1)
        self.__ventana.columnconfigure(2, weight=1)

        ttk.Label(self.__ventana, text="Número Imaginario 1:").grid(column=0, row=0, padx=10, pady=10)
        self.entry1=ttk.Entry(self.__ventana, textvariable=self.__numero1)
        self.entry1.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.__ventana, text="Número Imaginario 2:").grid(column=0, row=1, padx=10, pady=10)
        self.entry2=ttk.Entry(self.__ventana, textvariable=self.__numero2)
        self.entry2.grid(column=1, row=1, padx=10, pady=10)

        ttk.Button(self.__ventana, text='0', command=partial(self.agregar_numero, '0')).grid(column=0, row=4, padx=10, pady=10)
        ttk.Button(self.__ventana, text='1', command=partial(self.agregar_numero, '1')).grid(column=1, row=2, padx=10, pady=10)
        ttk.Button(self.__ventana, text='2', command=partial(self.agregar_numero, '2')).grid(column=2, row=2, padx=10, pady=10)
        ttk.Button(self.__ventana, text='3', command=partial(self.agregar_numero, '3')).grid(column=0, row=3, padx=10, pady=10)
        ttk.Button(self.__ventana, text='4', command=partial(self.agregar_numero, '4')).grid(column=1, row=3, padx=10, pady=10)
        ttk.Button(self.__ventana, text='5', command=partial(self.agregar_numero, '5')).grid(column=2, row=3, padx=10, pady=10)
        ttk.Button(self.__ventana, text='6', command=partial(self.agregar_numero, '6')).grid(column=0, row=4, padx=10, pady=10)
        ttk.Button(self.__ventana, text='7', command=partial(self.agregar_numero, '7')).grid(column=1, row=4, padx=10, pady=10)
        ttk.Button(self.__ventana, text='8', command=partial(self.agregar_numero, '8')).grid(column=2, row=4, padx=10, pady=10)
        ttk.Button(self.__ventana, text='9', command=partial(self.agregar_numero, '9')).grid(column=0, row=5, padx=10, pady=10)

        ttk.Button(self.__ventana, text='+', command=self.sumar).grid(column=1, row=5, padx=10, pady=10)
        ttk.Button(self.__ventana, text='-', command=self.restar).grid(column=2, row=5, padx=10, pady=10)
        ttk.Button(self.__ventana, text='*', command=self.multiplicar).grid(column=0, row=6, padx=10, pady=10)
        ttk.Button(self.__ventana, text='/', command=self.dividir).grid(column=1, row=6, padx=10, pady=10)

        ttk.Label(self.__ventana, text="Resultado:").grid(column=0, row=7, padx=10, pady=10)
        ttk.Label(self.__ventana, textvariable=self.__resultado, relief="solid").grid(column=1, row=7, padx=10, pady=10)

    def agregar_numero(self, numero):
        if self.entry1.focus_get() == self.entry1:
            self.__numero1.set(self.__numero1.get() + numero)
        elif self.entry2.focus_get() == self.entry2:
            self.__numero2.set(self.__numero2.get() + numero)


    def sumar(self, *args):
        try:
            num1 = self.obtener_numero1()
            num2 = self.obtener_numero2()
            resultado = num1 + num2
            self.__resultado.set(str(resultado.real) + "+" + str(resultado.imaginario) + "i")
        except ValueError:
            messagebox.showerror(title="Error de Valor", message="Debe ingresar números válidos.")
    def restar(self):
        try:
            num1 = self.obtener_numero1()
            num2 = self.obtener_numero2()
            resultado = num1 - num2
            self.__resultado.set(str(resultado.real) + "+" + str(resultado.imaginario) + "i")
        except ValueError:
            messagebox.showerror(title="Error de Valor", message="Debe ingresar números válidos.")

    def multiplicar(self):
        try:
            num1 = self.obtener_numero1()
            num2 = self.obtener_numero2()
            resultado = num1 * num2
            self.__resultado.set(str(resultado.real) + "+" + str(resultado.imaginario) + "i")
        except ValueError:
            messagebox.showerror(title="Error de Valor", message="Debe ingresar números válidos.")

    def dividir(self):
        try:
            num1 = self.obtener_numero1()
            num2 = self.obtener_numero2()
            resultado = num1 / num2
            self.__resultado.set(str(resultado.real) + "+" + str(resultado.imaginario) + "i")
        except ValueError:
            messagebox.showerror(title="Error de Valor", message="Debe ingresar números válidos.")
        except ZeroDivisionError:
            messagebox.showerror(title="Error de División", message="No se puede dividir entre cero.")


    def obtener_numero1(self):
        partes = self.__numero1.get().split("+")
        if len(partes) != 2:
            raise ValueError
        try:
            real = float(partes[0])
            imaginario = float(partes[1].replace("i", ""))
        except ValueError:
            raise ValueError
        return Imaginario(real, imaginario)

    def obtener_numero2(self):
        partes = self.__numero2.get().split("+")
        if len(partes) != 2:
            raise ValueError
        try:
            real = float(partes[0])
            imaginario = float(partes[1].replace("i", ""))
        except ValueError:
            raise ValueError
        return Imaginario(real, imaginario)

    def iniciar(self):
        self.__ventana.mainloop()


if __name__ == "__main__":
    calculadora = CalculadoraImaginarios()
    calculadora.iniciar()
