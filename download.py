import math
arquivo = float(input('Tamanho do arquivo(MB):'))
velocidade = float(input('Velocidade do link de internet (Mbps):'))
velocidade_Mbs = velocidade/8
segundos = arquivo/velocidade_Mbs

print('Tempo aproximado do download', math.ceil(segundos/60), 'min')