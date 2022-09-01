h = float(input('Informe a altura:'))
sexo = input('Informe seu sexo(H ou M):').lower()


if sexo == 'M':
    peso_ideal = (61.1 * h) - 44.7
    print(f'Sua altura é {h} e seu peso ideal é {peso_ideal:.2f}')
else:
    peso_ideal = (72.7 * h) - 58
    print(f'Sua altura é {h} e seu peso ideal é {peso_ideal:.2f}')
