


def anagramm(str1, str2):
    if len(str1) != len(str2):

        return 'не анаграмма'
    else:
        str1 = sorted(list(str1.lower()))
        str2 = sorted(list(str2.lower()))
        return 'анаграмма'

l = 'материк'
l2 = 'метрика'
l3 = 'термика'
l4 = 'керамит'
l5 = 'sdfss'

print(f'{l} и {l2} ---{anagramm(l,l2)}')
print(f'{l} и {l3} ---{anagramm(l,l3)}')
print(f'{l} и {l4} ---{anagramm(l,l4)}')
print(f'{l} и {l5} ---{anagramm(l,l5)}')
print(f'{l3} и {l2} --- {anagramm(l3,l2)}')