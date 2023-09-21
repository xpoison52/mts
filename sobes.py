import re
massiv = ['AbCdEfаЦ', 'Pagyra', 'ЦaBcDeЩ', 'pops', 'AbCцЦFg', 'KИlьka', 'sobaka', 'kusaчки'] # массив строк
pattern = re.compile(r'.*[А-ЯЁа-яё].*[А-ЯЁа-яё].*') # регулярное выражение, которое ищет слова с двумя кириллическими символами (если будет больше двух - тоже найдет)
for i in massiv: # цикл
    if not re.match(pattern, i):
        massiv.remove(i) # удаление неподходящих элементов массива
print(massiv) # выведение обновленного массива