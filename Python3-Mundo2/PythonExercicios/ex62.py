a1 = float(input('Digite o primeiro termo de sua PA(Progressão aritmética): '))
r = float(input('Digite a razão de sua PA: '))
i = 1
c = 1
while i <= 10:
    print('{}º termo da PA: {:.2f}'.format(i, a1))
    a1 = a1 + r
    i += 1
while c != 0:
    print('Você quer ver mais quantos termos de sua PA? ')
    print('Digite 0 para finalizar')
    c = int(input('Sua escolha: '))
    if c != 0:
        while c > 0:
            print('{}º termo da PA: {:.2f}'.format(i, a1))
            a1 = a1 + r
            i += 1
            c -= 1
        c = 1    
print('Sua progressão foi finalizada com {} termos'.format(i - 1))
