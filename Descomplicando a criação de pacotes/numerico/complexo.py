import math


class complexo():
    def __init__(self, entrada_x, entrada_y):
        self.entrada_x = entrada_x
        self.entrada_y = entrada_y

    def __str__(self):
        if self.entrada_y > 0:
            return f'{self.entrada_x} + {self.entrada_y}j'
        else:
            return f'{self.entrada_x} - {math.fabs(self.entrada_y)}j'

    def modulo(self):
        return (self.entrada_x**2 + self.entrada_y**2)**(1/2)

    def fase(self):
        return math.atan(self.entrada_y/self.entrada_x)

    def parte_real(self):
        return self.entrada_x

    def parte_imaginaria(self):
        return self.entrada_y

    def rad_para_grau(self, angulo=None):
        if angulo == None:
            return self.fase()*180/math.pi
        else:
            angulo*180/math.pi

    def polar(self):
        modulo = self.modulo()
        fase = self.fase()
        return (modulo, fase)


if __name__ == '__main__':
    numero = complexo(3, -4)
    print(numero.__str__())
    print(f'modulo: {numero.modulo()}')
    print(f'fase: {numero.fase()}')
    print(f'parte real: {numero.parte_real()}')
    print(f'parte imaginaria: {numero.parte_imaginaria()}')
    print(f'fase em grau: {numero.rad_para_grau()}')
    print(f'modo polar: {numero.polar()}')
