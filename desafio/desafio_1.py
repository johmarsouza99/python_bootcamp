#Solicita o nome
nome= input(str('Qual o seu nome? '))
#Solicita o salário
salario= int(input('Qual o seu salário? '))
#Solicita o bonus
bonus = float(input('Qual a taxa do bônus que você recebeu? '))
#Cálculo do Bônus
valor_bonus = 1000
#Cálculo do salário total
salario_total = salario*bonus + valor_bonus
#Imprime o salário total
print(f'Olá {nome}! Seu salário total é R${salario_total} Reais')