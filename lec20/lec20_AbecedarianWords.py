def is_abecedarian(word):
    for i in range(1, len(word)):
        if word[i-1] > word[i]:
            return False 
    return True


f = open("lec20/words.txt", "r")

for line in f:
    word = line.strip()
    if is_abecedarian(word): 
        print(word)

f.close()