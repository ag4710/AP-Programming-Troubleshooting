# 입력된 값을 반대로 출력

def reverse_alphabet(alphabet):
    for i in range(len(alphabet)-1,-1,-1):
        t = alphabet[i]
        print(t, end='')

def recursive_reverse_alphabet(alphabet, len):
    if len < 0:
        return
    print(alphabet[len], end='')
    recursive_reverse_alphabet(alphabet, len-1)

user_alphabet = list(input())
reverse_alphabet(user_alphabet)
print()
len_alphabet = int(len(user_alphabet)) - 1
recursive_reverse_alphabet(user_alphabet, len_alphabet)