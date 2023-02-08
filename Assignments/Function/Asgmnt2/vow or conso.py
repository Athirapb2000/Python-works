# 10.define a function which counts vowels and consonant in a word.
def count(ch):
    vow = 0
    con = 0
    for i in range(len(ch)):
        if ch[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vow = vow+1
        else:
            con = con+1
    print('Count of vowels:', vow)
    print('Count of consonants:', con)
result = input('Enter a string: ')
count(result)
