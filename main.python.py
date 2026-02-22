#Atribuição de valores a variáveis

nome = "Eduardo"
idade = 21

#Entrada de dados do usuário

altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

# Cálculo do IMC (INDICE DE MASSA CORPORAL)

imc = peso / (altura ** 2 )

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura:.2f}m')
print(f'Peso: {peso:.1f}kg')
print(f'imc: {imc:.2f}kg')
