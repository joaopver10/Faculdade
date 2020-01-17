from classesListas import *
listaTintas = ListaTintas() #criando um objeto do tipo ListaTinta
listaParedes = ListaParedes()#criando um objeto do tipo ListaParede

while True:
    print('1- Adicionar Tinta')
    print('2- Adicionar Parede')
    print('3- Listar Tintas')
    print('4- Listar Paredes')
    print('5- Começar pintura')
    op = int(input('Digite a opção: '))
    if op == 1:
        listaTintas.addTinta()
        print('Tinta  adicionada com sucesso!')
    elif op == 2:
        listaParedes.addParede()
        print('Parede adicionada com sucesso!')
    elif op == 3:
        listaTintas.imprimeLista()
        ## print('Tinta removida com sucesso!')
    elif op == 4:
        listaParedes.imprimeLista()
        ## print('Parede removida com sucesso!')
    elif op == 5:
        print('Vamos Pintar!')
        break

while True:
    listaTintas.imprimeLista() #chamando o método imprimeLista do objeto ListaTinta
    listaParedes.imprimeLista()#chamando o método imprimeLista do objeto ListaParede
    tinta = int(input('Selecione o número da tinta que deseje usar: '))
    parede = int(input('Selecione o número da parede que deseje pintar: '))
    resta = listaTintas.tintas[tinta-1].pintar(listaParedes.paredes[parede-1])
    #chama o método pintar do objeto do tipo Tinta dentro da lista do objeto do tipo ListaTinta
    if resta == 0:
        listaTintas.removeTinta(listaTintas.tintas[tinta-1])
    continua = input('Deseja continuar pintando? (S para sim, N para não)')
    if(continua in 'Nn'):
        break
print('*'*50)
print('Resultado após a pintura')
listaTintas.imprimeLista() #chamando o método imprimeLista do objeto ListaTinta
listaParedes.imprimeLista()