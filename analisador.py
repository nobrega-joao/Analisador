soma = 0
ivelho = 0
nvelho = 0
cmulher = 0
for c in range(1, 5):
    print('----- {}° Pessoa -----' .format(c))
    nome = str(input('Nome: ')) .strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')) .upper() .strip()
    soma += idade
    if c == 1 and sexo == 'M':
        ivelho = idade
        nvelho = nome
    elif sexo == 'M' and idade > ivelho:
        ivelho = idade
        nvelho = nome
    elif idade < 20 and sexo == 'F':
        cmulher += 1
media = soma / 4
print('A média de idade do grupo é de {:.2f} anos.' .format(media))
print('O homem mais velho tem {} anos e se chama {}.' .format(ivelho, nvelho))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(cmulher))
