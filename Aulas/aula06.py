#teste base para programa

mh = float(input ('Qual valor atual do mh: '))
mh1 = float(input ('Qual valor do antigo mh: '))

tolerency = 0.20

diferenca = abs(mh - mh1)

if diferenca <= tolerency:
    print(f'Ok. Result -> {diferenca:.2f}')
else:
    print (f'Atenção, valor à {diferenca:.2f} de diferença.')


