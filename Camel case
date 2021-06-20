integer = (input())
mapping = list(map(int,integer))
add = []

dic = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 0:'zero'}
for i in mapping:
    if i in dic:
        add.append(dic[i])

for i in add:
    print(i)


output = ''.join(x.capitalize() for x in add if x.isalnum())
print(output[0].lower() + output[1:])
