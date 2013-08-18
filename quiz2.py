#-*- coding: utf-8
#把文件打开 然后读取 然后关上
f = file('d:/crossin_class/from.txt')
data = f.read()
print data
f.close()

def En_check(cha):
    x = ord(cha)

    if x >= 97 and x <= 122:
        return True
    elif x >=65 and x <=90:
        return True
    else:  return False

def En_split(data):
    En = []
    En_gather = ""
    flag = True

    for cha in data:
        if not flag and En_check(cha):
            flag = True
        elif not En_check(cha) and flag:
            flag = False
            if En_gather != "":
                En.append(En_gather)
        if flag:
            En_gather += cha
        else:
            En_gather = ""

    if En_gather != "":
        En.append(En_gather)

    return En

print En_split(data)

group = En_split(data)

for word in group:
    print word.decode('utf-8')

group.sort()

print group

out = open('d:/crossin_class/to.txt','w')
for word in group:
	out.write(word)
	out.write(' ')
out.close()
