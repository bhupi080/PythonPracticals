str = input("Enter any String : ")

l = str.split()
l2 = []

for word in l:
    word_len = len(word)
    word_new = ""
    for i in range(0,word_len):
        if i == 0 or i == word_len-1:
            word_new += word[i].upper()
        else:
            word_new += word[i].lower()
    l2.append(word_new)

new_str = " ".join(l2)
print(new_str)
