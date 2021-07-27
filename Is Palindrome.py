word = input()
size = int(len(word))
output = True
for i in range (0, int(size/2)):
    if(word[i] != word[size-i-1]):
        output=False

if(output==False):
    print('No')
else:
    print('Yes')