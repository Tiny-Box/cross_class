#-*- coding:utf-8

#全局变量 作为字典检索标志
mark = {"Eng":1, "Chi":2}

#打开文件
def OpenFile():
	address = raw_input("Please input the source txt's address, eg: D:/abc.txt\n")
	File = file(address)
	data = File.read()
	File.close()
	return data

#分词器
def split_ch_en(data):
	#总列表
	group = []
	#中英文单词收录
	Chi_gather = ""
	Eng_gather = ""
	#判断中英文模式转换标志
	flag = False

	for cha in data:
		#判断为英文
		if not flag and ch_check(cha):
			#模式转换
			flag = True
			if Eng_gather != "":
				#将收录的单词放入总列表
				group.append([mark["Eng"], Eng_gather])
				Eng_gather = ""
		#判断为中文
		elif en_check(cha) and flag:
			#模式转换
			flag = False
			if Chi_gather != "":
				#将收录的单词放入总列表
				group.append([mark["Chi"], Chi_gather])
		#将每个判断过的字符放入相应的字符串中
		if flag:
			Chi_gather += cha
		else:
			Eng_gather += cha
			Chi_gather = ""
	
	#最后一个字符录入
	if Eng_gather != "":
		group.append([mark["Eng"], Eng_gather])
	elif Chi_gather != "":
		group.append([mark["Chi"], Chi_gather])

	return group

def ch_check(cha):
	#将字符转换成unicode码
	x = ord(cha)

	#这部分的UNICODE码可以自行去查unicode表
	#部首和标点 
	if x >= 0x2e80 and x <= 0x33ff:
		return True

	#半形和全型
	elif x >= 0xff00 and x <= 0xffef:
		return True

	#CJK统一表意符号
	elif x >= 0x4e00 and x <= 0x9fbb:
		return True
	#CJK兼容象形文字
	elif x >= 0xf900 and x <= 0xfad9:
		return True

	#CJK统一表意符号B
	elif x >= 0x20000 and x <= 0x2a6d6:
		return True

	#CJK表意文字补充
	elif x >= 0x2f800 and x <= 0x2fa1d:
		return True

	else:
		return False
	
def en_check(cha):
	x = ord(cha)

	#这个是小写字母
	if x >= 97 and x <= 122:
		return True
	#这个是大写
	elif x >= 65 and x <= 90:
		return True
	else: return False

def Save(group):

	add_ch = raw_input("Please input the address you want to save the chinese txt. eg: D:/abc.txt\n")
	add_en = raw_input("Please input the address you want to save the english txt. eg: D:/abc.txt\n")

	out_chi = open(add_ch, 'w')
	out_eng = open(add_en, 'w')

	for word in group:
		#如果是英文 写入add_eng中	
		if word[0] == mark["Eng"]:
			out_eng.write(word[1])
			out_eng.write(' ')
		#反之写入add_chi中
		else :
			out_chi.write(word[1].encode("utf-8"))
			out_chi.write(' ')

data = OpenFile()
#将所有从txt中的文字转换成unicode码
data = unicode(data, "utf-8")
group = split_ch_en(data)
Save(group)
