#Algoritimo gerador de CPF


import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

lista_numeros_1 = list(nove_digitos)
primeiro_digito = 0

for digito in range(10,1,-1):
    primeiro_digito += int(lista_numeros_1[10-digito]) * digito
primeiro_digito = (primeiro_digito*10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

lista_numeros_2 = list(nove_digitos + str(primeiro_digito))
segundo_digito = 0

for digito in range(11,1,-1):
    segundo_digito += int(lista_numeros_2[11-digito]) * digito
segundo_digito = (segundo_digito*10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
print(novo_cpf)


