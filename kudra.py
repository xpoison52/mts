import itertools
# разделим предложение по частям, которые не могут перемешиваться с другими частями
part1 = ['глокая', 'куздра']
part2 = ['штеко', 'будланула', 'бокра']
part3 = ['и']
part4 = ['курдячит', 'бокрёнка']

# перемешаем внутри каждой части
perms_part1 = list(itertools.permutations(part1))
perms_part2 = list(itertools.permutations(part2))
perms_part3 = list(itertools.permutations(part3))
perms_part4 = list(itertools.permutations(part4))


dekart = itertools.product(perms_part1, perms_part2, perms_part3, perms_part4) # Декартово произведение всех перемешанных частей

print(dekart)
# соединим части и пройдёмся циклом по всем возможным положениям групп (учитывая условия положения союза "и") и выведем эти варианты
for perm1, perm2, perm3, perm4 in dekart: 
    sentence1 = ' '.join(itertools.chain.from_iterable([perm1, perm2, perm3, perm4]))
    sentence2 = ' '.join(itertools.chain.from_iterable([perm1, perm4, perm3, perm2]))
    sentence3 = ' '.join(itertools.chain.from_iterable([perm2, perm1, perm3, perm4]))
    sentence4 = ' '.join(itertools.chain.from_iterable([perm4, perm1, perm3, perm2]))
    sentence5 = ' '.join(itertools.chain.from_iterable([perm4, perm3, perm2, perm1]))
    sentence6 = ' '.join(itertools.chain.from_iterable([perm2, perm3, perm4, perm1]))
    print(sentence1.capitalize())
    print(sentence2.capitalize())
    print(sentence3.capitalize())
    print(sentence4.capitalize())
    print(sentence5.capitalize())
    print(sentence6.capitalize())
