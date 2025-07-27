# a lista onde vamos guardar as tarefas
import os
tarefas = []

# ---nossas funçoes---

# função para adicionar tarefas

def adicionar_tarefa():

# salvar em texto

# pede ao usuario para digitar a tarefa e guarda o texto na variavel

    nova_tarefa =   input("digite o nome da nova tarefa: ") 

    tarefas.append(nova_tarefa)

    print(f"tarefa '{nova_tarefa}' foi adicionada com sucesso!")   
    print('-- DEBUG: estou prestes a chamar a função de salvar')
    salvar_tarefas_em_arquivo()
    
# função para mostrar - listar tarefas

def mostrar_tarefas():
    print("\n--- Suas Tarefas---")
    if not tarefas:
        print("nenhuma tarefa na lista ainda!")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
            print("----------------------")
def salvar_tarefas_em_arquivo():
    with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
        for i, tarefa in enumerate(tarefas, start=1):
            arquivo.write(f'{i}. {tarefa}\n')          
# LOOP
while True:
    print ('\no que voce deseja fazer?')
    print ('1. adicionar uma nova tarefa')
    print ('2. mostrar todas as tarefas')
    print ('3. sair do programa')

    # escolher opção
    escolha = input('digite o numero da sua escolha')

    # escolha de usuario
    if escolha == '1':
        adicionar_tarefa()
    elif escolha == '2':
        mostrar_tarefas()
    elif escolha == '3':
        print('ate logo!')
        break
    else:
        print('opção invalida! por favor escolha uma das opções acima!') 
