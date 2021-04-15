import random
while True:
    phrases=['sadasdasd','dasdasdasd','asdasdasdasd','dadasdasdsadasdasdasd','dasdasdasdasdasdasdasd',\
             'asdasdasdasdasdasd','sdasddsa','sadsadasd','sadsadasdsa','dasdasdasd','dsadsadsadasdad',
             'sadsadasdasd','sadsadsadasdasd','asdasdasdasdasd','asdasdasdasdasd','dasdasdasdasdasd',\
             'asdasdasdasdasd','asdasdasdasdasda','asdasdasdas','dasdasdasd','asdasdasdasd']
    fraza=(input())
    if fraza=='Скажи мудрость':
        print(phrases[random.randint(0,15)])
    elif fraza == 'Знать ничего не хочу':
       print('OK')
    elif fraza=='Выйти':
        continue
    else:
        print('Неверный ввод')
