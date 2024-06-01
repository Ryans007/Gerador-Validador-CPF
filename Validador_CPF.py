import re
import sys

entrada = input('Digite o seu CPF:')

CPF = re.sub(r'[^0-9]','',entrada)

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Você enviou dados sequenciais!')
    sys.exit()

cpf_digitos_1 = CPF[:9]
cpf_digitos_2 = CPF[:10]
lista_numeros_1 = list(cpf_digitos_1)
lista_numeros_2 = list(cpf_digitos_2)

primeiro_digito = 0
segundo_digito = 0

for digito in range(10,1,-1):
    primeiro_digito += int(lista_numeros_1[10-digito]) * digito
primeiro_digito = (primeiro_digito*10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

for digito in range(11,1,-1):
    segundo_digito += int(lista_numeros_2[11-digito]) * digito
segundo_digito = (segundo_digito*10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

novo_cpf = f'{cpf_digitos_1}{primeiro_digito}{segundo_digito}'

validacao_cpf = print('CPF válido') if novo_cpf == CPF else print('CPF inválido')