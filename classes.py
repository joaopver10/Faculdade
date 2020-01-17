class Tinta(object):
    def __init__(self, cor, litros):
        self.cor = cor
        self.litros = litros

    def getCor(self): #método que retorna a cor do objeto Tinta
        return self.cor

    def pintar(self, parede): #método que pinta o objeto Parede recebido por parâmetro
        totalPintado = 0 #cria uma variável pra ver se há itens na lista areaPintada
        for cont in parede.areaPintada:
            totalPintado += cont
        if self.litros == 0:# Se o atributo tinta do objeto tinta for zero
            print('Tinta vazia.')
            return self.litros
        elif self.litros * 2 < parede.altura * parede.largura and self.litros * 2 < parede.altura * parede.largura - totalPintado:
            # se a quantidade de tinta for menor que o total de área à ser pintada
            parede.areaPintada.append(self.litros * 2)
            self.litros = 0
            ultimo = len(parede.areaPintada) - 1
            parede.corPintada.append(self.cor)
            print('Área pintada da parede: ', parede.areaPintada[ultimo]," de cor ",parede.corPintada[ultimo])
            return self.litros
        elif self.litros * 2 >= parede.altura * parede.largura - totalPintado: # areatotal-area pintada
            #Se houver mais tinta que área não pintada
            parede.areaPintada.append(parede.altura * parede.largura - totalPintado)
            parede.corPintada.append(self.cor)
            ultimo = len(parede.areaPintada) - 1
            self.litros = self.litros - parede.areaPintada[ultimo] / 2
            print('Parede totalmente pintada. Restaram ', self.litros, 'L de tinta.')
            parede.pintada = True
            return self.litros


class Parede(object):
    def __init__(self, nome,altura, largura): #construtor
        self.nome = nome
        self.altura = altura
        self.largura = largura
        self.pintada = False
        self.areaPintada = list()
        self.corPintada = list()
        print('Parede com ', self.altura * self.largura, 'm²')

    def getNome(self):#retorna o nome da parede
        return self.nome

