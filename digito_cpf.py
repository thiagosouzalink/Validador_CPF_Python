"""
Projeto validador de CPF
Autor: Thiago Souza
"""


def calcular_digito(cpf, dig=-1):
    """ Função para calcular digito verificador de CPF.
    :param => cpf, digito(opcional)
    :return digito calculado
    O Segundo parâmetro é opcional, apenas caso o digitado a ser calculado seja o segundo digito verificador
    """
    num = 10 if dig < 0 else 11 # Condição para calcular primeiro ou segundo digito
    # Calcula o somatório do digito verficador
    soma = 0
    for i in range(9):
        soma = soma + int(cpf[i]) * num
        num -= 1

    if dig > 0:
        soma = soma + dig * num

    # Obtêm o digito verificador
    valor = soma % 11
    if valor < 2:
        digito = 0
    else:
        digito = 11 - valor

    return digito