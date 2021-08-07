list_fix = []
list_str = input().split()
print(list_str)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_start_up = 65
alpha_end_up = 90
alpha_start_low = 97
alpha_end_low = 122
k = 0

for word in list_str:
    word_fix = ''
    for i in word:
        if i.lower() in alphabet:
            k += 1
    print(k)
    for alpha in word:
        if alpha.isupper():
            alpha_start, alpha_end = alpha_start_up, alpha_end_up

        elif alpha.islower():
            alpha_start, alpha_end = alpha_start_low, alpha_end_low

        elif alpha in '.,=+-_*№!''?:;"()" 0123456789':
            word_fix += alpha

        if alpha_start <= ord(alpha) <= alpha_end:

            if alpha_start <= ord(alpha) + k <= alpha_end:
                word_fix += chr(ord(alpha) + k)

            elif ord(alpha) + k > alpha_end:
                word_fix += chr((alpha_start - 1) + (ord(alpha) + k) - alpha_end)

            elif alpha_start_low > ord(alpha) + k:
                word_fix += chr((alpha_end + 1) - (alpha_start - (ord(alpha) + k)))

    list_fix.append(word_fix)
    k = 0


print(*list_fix)
