# Desafio Normalizador de Dados 


def normalizar_telefone(telefone_bruto):
    
    telefone_limpo = telefone_bruto
    caracteres_a_remover = ['-', '(', ')', ' ', '.']
    for caractere in caracteres_a_remover:
        telefone_limpo = telefone_limpo.replace(caractere, '')
        
    return telefone_limpo

print(f"Entrada: '35988887777'      -> saida: {normalizar_telefone('35988887777')}")
print(f"Entrada: ' 35.91234.5678 '  -> saida: {normalizar_telefone(' 35.91234.5678 ')}")
print(f"entrada: '(35)99999.9999' -> saida: {normalizar_telefone('(35)99999.9999' )}")
   