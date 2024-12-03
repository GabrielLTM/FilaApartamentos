from Apartamento import *
from FilaEspera import FilaEspera
from Torre import Torre

# Menu interativo
def menu():
    fila = FilaEspera()
    
    
    while True:
        print(' 1 - Cadastrar apartamento e torre')
        print(' 2 - Adicionar na fila de espera')
        print(' 3 - Retirar apartamento da fila')
        print(' 4 - Imprimir fila')
        print(' 5 - Sair do sistema')


        escolha = input( 'Qual opção você quer? ')
        if escolha == '1':
            nome = input('Digite o nome da Torre: ')
            endereco = input('Digite o endereco da Torre: ')
            numero = input('Digite o número do Ap: ')
            vaga = int(input('Digite a vaga do Ap: '))
            cad = Apartamento(nome, endereco, numero, vaga)
            print(cad.cadastrar())
        
        if escolha == '2':
            
            numero = int(input("Número da vaga que deseja adicionar na Fila: "))
            vaga_encontrada = False  

            for cada in apartamentos_cad:
                if cada.vaga == numero:
                    fila.add(cada)
                    vaga_encontrada = True
                    break  

            if not vaga_encontrada:
                print("Vaga não encontrada")
            
            
        if escolha == '3':
            fila.remover()
        
        if escolha == '4':
            fila.imprimir()
           

menu()