# 단어의 길이가 18보다 긴 모든 영어 단어 출력
f = open("lec20/words.txt", "r")
for line in f:
    word = line.strip()
    if len(word) > 18: 
        print(word)
f.close()

print()

# 글자 ‘e’가 포함되지 않은 단어의 수
f = open("lec20/words.txt", "r")
count = 0
for line in f:
    word = line.strip()
if not "e" in word: 
    count += 1
    print("%d words have no 'e'" % count)
f.close()