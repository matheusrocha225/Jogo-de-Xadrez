linhas = int(input('Quantas linhas? : '))
colunas = int(input('Quantas colunas? : '))

print('\n    |  ',end='')
for i in range(0,colunas):
        if i > 9:
                print(str(i)+' ', end='') #Retirei um espaço para que a posição dos numeros não fique errada
        else:
                print(str(i)+'  ', end='')
#print('|','\n   |'+'-'*3+'-'*((colunas*3)-1)+'|') #Um traço que entre os numeros da coluna
print('|')
for i in range(0,linhas):
        if i >= 10 and i < 100:
                print(i,' |'+'  X'*colunas,' |') #Linhas maiores que 9 e menores que 100 (10-99)
        elif i >= 100:
                print(i,'|'+'  X'*colunas,' |') #Linhas maiores que 9 e menores que 100 (10-99)
        else:
                print(i,'  |'+'  X'*colunas,' |') #Linhas menores que 10

while 1:
        local_c = int(input('\nQual local da coluna? : '))
        if local_c > colunas-1:
                print('local inválido.\n')
                continue
        break

while 1:
        local_l = int(input('Qual local da linha? : '))
        if local_l > linhas-1:
                print('local inválido.\n')
                continue
        break

print('\n    |  ',end='')
for i in range(0,colunas): #Numeros da coluna
        if i > 9:
                print(str(i)+' ', end='') #end='' serve para impedir a quebra de linha "\n"
        else:
                print(str(i)+'  ', end='')
print('|')
for i in range(0,linhas):
        if i == local_l: #Linha que será alterada
                c1 = local_c
                c2 = (colunas-c1)-1
                if i > 9 and i < 100:
                        print(str(i),' |'+'  X'*c1,' P'+'  X'*c2,' |') #Linhas maiores que 9 e menores que 100 (10-99)
                elif i >= 100:
                        print(str(i),'|'+'  X'*c1,' P'+'  X'*c2,' |') #Linhas maiores que 9 e menores que 100 (10-99)
                else:
                        print(i,'  |'+'  X'*c1,' P'+'  X'*c2,' |') #Linhas menores que 10
        elif i >= 10 and i < 100:
                print(i,' |'+'  X'*colunas,' |') #Linhas maiores que 9 e menores que 100 (10-99)
        elif i >= 100:
                print(i,'|'+'  X'*colunas,' |') #Linhas maiores que 99
        else:
                print(str(i),'  |'+'  X'*colunas,' |') #Linhas menores que 10