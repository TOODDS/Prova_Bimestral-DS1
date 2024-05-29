hora = int(input("Digite a hora (entre 0 e 23): "))
if 0 <= hora <12:
    periodo = "Manhã"
elif 12 <= hora <18:
    periodo = "Tarde"
elif 18 <= hora <=23:
    periodo = "Noite"
print(f'O horário é {periodo}')
