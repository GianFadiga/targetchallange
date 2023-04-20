# Gianlucca Fadiga Rissato
# Target - Teste técnico

# Exercício 1

# indice = 13
# k = 0
# soma = 0
# while k<13:
#     k = k + 1
#     soma = soma + k
# print(soma)

# Portanto, o resultado é 91

# Exercício 2

# valor = int(input("Digite um valor para verificar se ele faz parte da sequencia de Fibonacci: "))

# a = 0
# b = 1
# c = 0

# fibonacci = [0]

# for i in range(valor):
#     c = a + b
#     a = b
#     b = c
    
#     fibonacci.append(a)
#     if a == valor:
#         break
#     else:
#         continue
    
# print(*fibonacci)

# if valor in fibonacci:
#     print("O valor faz parte da sequencia de Fibonacci")
# else:
#     print("O valor não faz parte da sequencia de Fibonacci")

# Exercício 3
# Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___  / Próximo número é 9 como sequência de número ímpar
# b) 2, 4, 8, 16, 32, 64, ____ / Próximo número é 128 como sequência de número potência de 2
# c) 0, 1, 4, 9, 16, 25, 36, ____ / Próximo número é 49 como sequência de número quadrado
# d) 4, 16, 36, 64, ____ / Próximo número é 100 como sequência de número quadrado
# e) 1, 1, 2, 3, 5, 8, ____ / Próximo número é 13 como sequência de número de Fibonacci
# f) 2, 10, 12, 16, 17, 18, 19, ____ / Próximo número é o 200, pois a sequência é de números naturais que começam com a letra "D"

# Exercício 4

# Em uma hora o carro percorre 110km
# O caminhão em uma hora percorre 80km, contudo ele para durante 10 minutos para os dois pedágios,
# logo ele percorre 72km em 60 minutos

# Eles se cruzarão no ponto:
# vCarro * tempo = vCaminhao * tempo + 100
# vCarro = (110 * 3,6)/1 = 396m/s
# vCaminhão = (72 * 3,6)/1 = 259,2m/s
# vCaminhão = 72/1 = 72km/h = 72*3,6 = 259,2m/s
# 396*tempo = 259,2*tempo + 100
# 396*tempo - 259,2*tempo = 100
# 136,8*tempo = 100
# tempo = 100/136,8 = 0,73h = 43,8min
# Logo, eles se cruzarão no ponto 43,8min
# O caminhão percorrerá 72*0,73 = 52,96km
# O carro percorrerá 110*0,73 = 80,3km
# Portanto, o carro estará mais próximo da cidade de Ribeirão Preto do que o caminhão

# Exercício 5

# FORMA SEM USAR FUNÇÃO

# string = input("Digite uma string: ")
# reversed = ""

# for i in range(len(string) -1, -1, -1):
#     reversed += string[i]
# print("A string invertida é: \n", reversed)