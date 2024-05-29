def adicao(x, y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero!"
    else:
        return x / y

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f'A soma desses valores é', adicao(num1, num2))
print(f'A subtração desses valores é', subtracao(num1, num2))
print(f'A multiplicação desses valores é', multiplicacao(num1, num2))
print(f'A divisão desses valores é', divisao(num1, num2))