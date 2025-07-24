API = 'python', 'java', 'javascript', 'github', 'c#', 'c++'

def count_API (list):
    pontuação = {}
    vencedor = []

    if len(list) < 2:
        return 'deve haver pelo menos dois candidatos'

    for API in list:
        if not API in pontuação:
            pontuação[API] = 0

        if API in pontuação:
            pontuação[API] += 1

    if pontuação:
        max_votos = max(pontuação.values())

    for API, votos in pontuação.items():
        if votos == max_votos:
            vencedor.append(API)

    if len(vencedor) > 1:
        return print (f'E os vencedores são:{vencedor}! com um empate unico de {max_votos} votos!')
    else:
        return print (f'o vencedor foi {vencedor}! com uma pontuação de {max_votos}!')
count_API(API)