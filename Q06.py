nome = input("Bem vindo ao site do Governo Federal, primeiramente digite o seu nome: ")
idade = int(input("Agora digite a sua idade: "))
if idade >=16:
    print(f'{nome}, você pode emitir o seu título de eleitor!')
else:
    print(f'{nome}, você ainda não pode emitir o seu título de eleitor!')
