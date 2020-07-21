"""
Projeto validador de CPF
Autor: Thiago Souza
"""

from digito_cpf import calcular_digito

while True:
    # Recebe o cpf do usuário
    cpf = input("Informe o CPF: ").strip()
    if '.' in cpf:
        cpf = cpf.replace('.', '')
    if '-' in cpf:
        cpf = cpf.replace('-', '')

    # Verifica se o CPF contém 11 digitos
    tamanho_cpf = len(cpf)
    if tamanho_cpf != 11 or not cpf.isnumeric():
        print("CPF digitado não está com 11 digitos! Tente novamente...\n")
        continue

    # Verifica se o CPF está com todos os digitos iguais (Condição para CPF inválido)
    if cpf == cpf[0]*11:
        print("CPF inválido!\n")
        continue

    # Obtêm digitos verficadores do CPF informado
    digito1 = int(cpf[9])
    digito2 = int(cpf[10])

    # Obtêm digitos verficadores calculados
    dig1 = calcular_digito(cpf) # Primeiro digito
    dig2 = calcular_digito(cpf, dig1) # Segundo digito

    # Verifica se os digitos verficadores calculados correspodem aos digitos verificadores do CPF informado
    if digito1 == dig1 and digito2 == dig2:
        print("CPF Válido!\n")
    else:
        print("CPF inválido!\n")

    # Verifica se o usuário deseja continuar consultando CPF
    continuar = input("Deseja consultar outro CPF? [s]im ou [n]ão: ").strip().lower()[0]
    while continuar not in 'sn':
        print("Opção inválida, tente novamente!")
        continuar = input("Deseja consultar outro CPF? [s]im ou [n]ão: ").strip().lower()[0]

    if continuar == 'n':
        print("\n\nMuito Obrigado!\n\n")
        break

