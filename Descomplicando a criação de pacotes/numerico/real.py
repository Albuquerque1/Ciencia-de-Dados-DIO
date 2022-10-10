class real():
    def __init__(self, args):
        self.entrada = args
    
    def raiz(self, indice = 1):
        return float(self.entrada)**(1/indice)
    
    def modulo(self):
        if self.entrada < 0:
            return -float(self.entrada)
        else:
            return float(self.entrada)
    
    def potencia(self, expoente =1):
        return float(self.entrada) ** expoente
    
    def formata(self, numero_decimais = 0 ):
        if numero_decimais == 0:    
            saida = f'{self.entrada:.0f}'.replace('.',',')
            return saida
        elif numero_decimais == 1:    
            saida = f'{self.entrada:.1f}'.replace('.',',')
            return saida
        elif numero_decimais == 2:    
            saida = f'{self.entrada:.2f}'.replace('.',',')
            return saida
        elif numero_decimais == 3:    
            saida = f'{self.entrada:.3f}'.replace('.',',')
            return saida
        elif numero_decimais == 4:    
            saida = f'{self.entrada:.4f}'.replace('.',',')
            return saida
        elif numero_decimais == 5:    
            saida = f'{self.entrada:.5f}'.replace('.',',')
            return saida
        elif numero_decimais == 6:    
            saida = f'{self.entrada:.6f}'.replace('.',',')
            return saida
        elif numero_decimais == 7:    
            saida = f'{self.entrada:.7f}'.replace('.',',')
            return saida
        elif numero_decimais == 8:    
            saida = f'{self.entrada:.8f}'.replace('.',',')
            return saida
        elif numero_decimais == 9:    
            saida = f'{self.entrada:.9f}'.replace('.',',')
            return saida
        else:
            return 'Especifique um número de casas decimais entre 0 e 9 inclusive.'


if __name__ == '__main__':
    numero = real(3)
    print(f'numero: {numero.entrada}') 
    print(f'raiz quadrada: {numero.raiz(2)}')
    print(f'raiz de {numero.entrada} com 2 casas: {real(numero.raiz(2)).formata(2)}')
    
    numero2 = real(-5.659239678)
    print(f'Numero {numero2.entrada} com 5 casas decimais: {numero2.formata(5)}')
    print(f'Modulo de {numero2.entrada}: {numero2.modulo()}')
    print(f'{numero2.formata(0)} elevado a 2: {real(numero2.formata(0)).potencia(2)}')
    