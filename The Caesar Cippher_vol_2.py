print('Эта программа может шифровать/дешифровать строку шифром "Цезаря"')
print()
print('''Шифр Цезаря, также известный как шифр сдвига, код Цезаря или сдвиг Цезаря — один из самых простых и наиболее
широко известных методов шифрования.''')
print()


def check_str(text):
    count_en = 0
    count_rus = 0
    count = 0
    for alpha in text:
        if alpha.lower() in 'abcdefghijklmnopqrstuvwxyz':
            count_en += 1
        elif alpha in '.,=+-_*№!''?/:;"()" 0123456789':
            count += 1
        elif alpha.lower() in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            count_rus += 1

        if count_en > 0 and count_rus > 0:
            return False

    if count_en + count != len(text) and count + count_rus != len(text):
        return False
    else:
        return True


def check_lang(text):
    count_en = 0
    count_rus = 0
    count = 0
    for alpha in text:
        if alpha.lower() in 'abcdefghijklmnopqrstuvwxyz':
            count_en += 1
        elif alpha in '.,=+-_*№!''?/:;"()" 0123456789':
            count += 1
        elif alpha.lower() in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            count_rus += 1

    if count_en + count == len(text):
        return 'EN'
    elif count_rus + count == len(text):
        return 'RU'


def check_purpose(pur):
    if pur == 'code' or pur == 'decode':
        return True
    else:
        return False


def check_key(k, language):
    if int(k) == 0:
        print('Отлично программа сделает все для вас!')
        return True

    elif language == 'EN':
        if -25 <= int(k) <= 25:
            print()
            print('Число', key, 'принято как шаг сдвига.')
            return True

    elif language == 'RU':
        if -31 <= int(key) <= 31:
            print()
            print('Число', key, 'принято как шаг сдвига.')
            return True
    else:
        return False


def housekeeper(freq):
    max_len = 0
    max_word = ''

    for alpha in alphabet:
        string_l = string.lower()
        if max_len < string_l.count(alpha):
            max_len = string_l.count(alpha)
            max_word = alpha
    print(max_word)
    return ord(freq) - ord(max_word)


def main(k, text):
    alpha_start = ''
    alpha_end = ''
    list_str = text.split(' ')
    list_str_fix = []
    k = int(k)

    for word in list_str:
        word_fix = ''
        for x in range(0, len(word)):
            if word[x].isupper():
                alpha_start, alpha_end = alpha_start_up, alpha_end_up

            elif word[x].islower():
                alpha_start, alpha_end = alpha_start_low, alpha_end_low

            elif word[x] in '.,=+-_*№!''?:;"()" 0123456789':
                word_fix += word[x]

            if alpha_start <= ord(word[x]) <= alpha_end:

                if alpha_start <= ord(word[x]) + k <= alpha_end:
                    word_fix += chr(ord(word[x]) + k)

                elif ord(word[x]) + k > alpha_end:
                    word_fix += chr((alpha_start - 1) + (ord(word[x]) + k) - alpha_end)

                elif alpha_start_low > ord(word[x]) + k:
                    word_fix += chr((alpha_end + 1) - (alpha_start - (ord(word[x]) + k)))

        list_str_fix.append(word_fix)

    return list_str_fix


while True:
    while True:
        print('Введите текст, текст принемается только на русском или только английском языке!')
        print()
        string = input()
        if check_str(string):
            lang = check_lang(string)
            break
        else:
            print()
            print('Ого, что пошло не так! В работу может быть принят только текст на русском или только на английском языке!')
            continue

    while True:
        print()
        print('Что вы хотите сделать? Шифровать или дешифровать? (code / decode)')
        print()
        purpose = input()
        if check_purpose(purpose):
            break
        else:
            print()
            print('Ого, что пошло не так! Выберите еще раз!')
            continue

    while True:
        print()
        print('Хотите выбрать шаг сдвига?')
        print()
        key = input('''Или программе выбрать за вас? (введите число на которое будет сдвинут ряд / если хотите отдать выбор случаю введите "0")''')
        print()
        if check_key(key, lang):
            break
        else:
            print()
            print('''Что-то вы ввели не верно! Попробуем еще раз? Максимальный шаг сдвига для русского это 31 а для английского 25 (введите число сдвига / если хотите отдать выбор случаю введите "0")''')
            continue

    if lang == 'EN':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alpha_start_up = 65
        alpha_end_up = 90
        alpha_start_low = 97
        alpha_end_low = 122
        frequent_alpha = 'etaoinshrdlcumwfgypbvkjxqz'

    elif lang == 'RU':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        alpha_start_up = 1040
        alpha_end_up = 1071
        alpha_start_low = 1072
        alpha_end_low = 1103
        frequent_alpha = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъ'

    if purpose == 'code':
        if key == '0':
            import random

            if lang == 'EN':
                key = random.randint(1, 25)
            elif lang == 'RU':
                key = random.randint(1, 31)

            print(*main(key, string))
            print()
        else:
            print(*main(key, string))
            print()

    else:
        if key == '0':
            for a in frequent_alpha:
                key = housekeeper(a)
                print()
                print(*main(key, string))
                print()
                if input('Если страка расшифрована не верно введите "NO" или "OK" в противном случае.') == 'OK':
                    print()
                    break
                else:
                    continue
        else:    # если пользователь хочет угадать сам
            while True:
                print()
                print(*main(key, string))
                print()
                if input('Если страка расшифрована не верно введите "NO" или "OK" в противном случае.') == 'OK':
                    print()
                    break
                else:
                    key = input('Введите новый ключ.')
                    print()
                    continue

    if input('Если хотите закончить работу введите "STOP"') == 'STOP':
        print()
        print('The End')
        break
    else:
        continue
