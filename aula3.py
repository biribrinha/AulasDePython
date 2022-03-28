#utilizar dois valores e informar qual valor é maior#

a = int(input('primeiro valor'))
b = int(input('segundo valor'))
c = int(input('terceiro valor'))

#é possível definir o início e fim de um bloco com a identação#
if a > b and a > c:
    print('o maior número é {}' .format(a))
elif b > a and b > c:
    print('o maior número é {}' .format(b))
else:
    print('o maior númro é {}' ,format(c))

print('final do programa') #vai imprimir na tela idependente se A é maior q B#




#transformar em centavos#

a = int(input('transforme qualquer numero em centavos'))
b = 100 #para converter um numero inteiro pra centavos, sempre dividir por 100#

centavo = a / b
centavo = str(centavo)
print(type(centavo))

print('R$' + centavo + ' centavos')
