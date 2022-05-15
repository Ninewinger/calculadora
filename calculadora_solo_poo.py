#calculadora con poo

class Calculadora():
    def __init__(self):
        self.resultado = 0

    def sumar(self, num1, num2):
        self.resultado = num1 + num2
        return self.resultado

    def restar(self, num1, num2):
        self.resultado = num1 - num2
        return self.resultado

    def multiplicar(self, num1, num2):
        self.resultado = num1 * num2
        return self.resultado

    def dividir(self, num1, num2):
        self.resultado = num1 / num2
        return self.resultado