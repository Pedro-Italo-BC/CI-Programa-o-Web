totalGrades = [input('Coloque a primeira nota do estudante: ')
,input('Coloque a segunda nota do estudante: ')
,input('Coloque a terceira nota do estudante: ')
,input('Coloque a quarta nota do estudante: ')]

total = float(totalGrades[0]) + float(totalGrades[1]) + float(totalGrades[2]) + float(totalGrades[3])

gradesMedia = total / 4

formatedText = 'A media da nota do aluno é de ' + str(gradesMedia) + '.'

print(formatedText)