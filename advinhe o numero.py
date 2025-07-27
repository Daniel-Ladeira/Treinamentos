#jogo de advinhar o numero
import random
def advinhar_numero():
    attempts = 0
    secret_number = random.randint(1, 100)
    print("eu pensei em um numero entre 1 e 100. você tem 5 tentativas para advinhar!")

    while True:
        resposta = int(input('Digite um número: '))
        attempts = attempts +1
        print(f'{attempts} / 7 ')

        

        if attempts >= 7:
            print(f"Você excedeu o número de desafios. O número sorteado era:{secret_number}")
            break
        
        if resposta == secret_number:
            print('"Parabéns!!! Você acertou o número!"')
            break
        
        else:
            print('Putz irmão, tu erro, tenta de novo.')

        if resposta > secret_number:
            print('chute mais baixo')
        else:
            print('chute mais alto')
    

advinhar_numero()

