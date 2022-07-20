T = int(input())
word_list = []
group_cnt =0

for i in range(T):
    word = input()
    error =0
    for k in range(len(word)-1):
        if word[k] != word[k+1]:
            new_word = word[k+1:]
            if new_word.count(word[k]) >0:
                error +=1
    if error ==0:
        group_cnt += 1
print(group_cnt)