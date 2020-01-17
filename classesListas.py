from classes import *

class ListaTintas(object):
    def __init__(self):
        self.tintas = list()

    def addTinta(self):
        cor = input('Informe a cor: ')
        for rep in self.tintas:
            if cor == rep.getCor():
                print('Já existe tinta com esta cor')
                return
        litros = int(input('Quantidade em litros: '))

        self.tintas.append(Tinta(cor, litros))
        ultimo = len(self.tintas)-1
        print(self.tintas[ultimo].cor)

    def imprimeLista(self):
        print("Lista de tintas adicionadas:")
        tamanho = len(self.tintas)
        for c in range(tamanho):
            print(self.tintas.index(self.tintas[c])+1," - Cor: ",self.tintas[c].getCor()," ",self.tintas[c].litros," - Lts")

    def removeTinta(self,tinta):
        self.tintas.remove(tinta)


class ListaParedes(object):
    def __init__(self):
        self.paredes = list()

    def addParede(self):
        nome = input('Informe o nome da parede: ')
        for rep in self.paredes:
            if nome == rep.getNome():
                print('Já existe parede com este nome')
                return
        altura = int(input('Informe a altura: '))
        largura = int(input('Informe a largura: '))
        self.paredes.append(Parede(nome,altura, largura))

    def imprimeLista(self):
        print(f'Lista das dimensões das paredes adicionadas:  ')
        for p in self.paredes:
            print('{} - Nome: {} Tamanho: {} X {}'.format(self.paredes.index(p)+1,p.getNome(), p.altura, p.largura))
            if p.areaPintada:
                print('Área Pintada:')
                tamanho = len(p.areaPintada)
                for c in range(tamanho):
                    print('{}m² - cor: {}'.format(p.areaPintada[c], p.corPintada[c]))
            else:
                print('Sem pintura!')
            if p.pintada:
                print('Parede Totalmente pintada!')


'''             
listaTinta = ListaTintas()
listaParede = ListaParedes()
listaTinta.addTinta()
listaParede.addParede()

listaTinta.tintas[0].pintar(listaParede.paredes[0])
listaTinta.addTinta()
listaTinta.addTinta()
listaTinta.imprimeLista() '''