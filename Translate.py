import random

englishpath = './english.txt'

englishlist = []
linelist = []
print("英语单词测试（汉译英）：")
with open(englishpath, "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        try:
            linelist = line.strip().split("\t")
            englishlist.append(linelist)
        except:
            pass
    englishlen = len(englishlist)
    while 1:
        randomnum = random.randint(0,englishlen) 
        englishinput = input(englishlist[randomnum][1] + ':').strip()
        if englishinput == '0':
            break
        if englishinput == englishlist[randomnum][0]:
            print("TRUE!\n")
        else:
            print(englishlist[randomnum][0] + ':' + englishlist[randomnum][1] + '\n')
