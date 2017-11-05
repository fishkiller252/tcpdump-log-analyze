import re
f = open('log.txt')
lines = f.readlines()
f.close()

winall = 0 #winの総和
winave = 0 #winの平均
lengthall = 0 #lengthの総和
lengthave = 0 #lengthの平均
count = 0 #行数
seqs =[] #seqの配列
for line in lines:
    
    word = re.split('[, ]', line)
    print (len(word))#split後の数
    if len(word)==23:#length=0以外の時
        count += 1
        winall +=  int(word[10])
        winave = winall/count
        lengthall +=  int(word[22])
        lengthave= lengthall/count
        seqs.append(word[4])
    print (word)
for seq in seqs:
    print(seq)#seq
print (winall)#winの総和
print (winave)#winの平均
print (lengthall)#lengthの総和
print (lengthave)#lengthの平均
