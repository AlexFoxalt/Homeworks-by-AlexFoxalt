MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    code = code.split(' ')
    res = []
    for word in code:
        if word in MORSE:
            res.append(MORSE.get(word))
        else:
            res.append(' ')
    print(res)
    idx = 0
    while idx < len(res) - 1:
        if res[idx] == ' ' == res[idx + 1]:
            res.pop(idx)
        else:
            idx += 1
    return ''.join(res).capitalize()


print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))
