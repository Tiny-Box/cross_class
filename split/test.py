#-*- coding:utf-8

def OpenFile():


def split_ch_en(data):
	group = []
	Chi_gather = ""
	Eng_gather = ""
	flag = False
	mark = {"Eng":1, "Chi":2}

	for cha in data:
		if not flag and ch_check(cha):
			flag = True
			if Eng_gather != "":
				group.append([mark["Eng"], Eng_gather])
				Eng_gather = ""
		elif en_check(cha) and flag:
			flag = False
			if Chi_gather != "":
				group.append([mark["Chi"], Chi_gather])
		if flag:
			Chi_gather += cha
		else:
			Eng_gather += cha
			Chi_gather = ""

	if Eng_gather != "":
		group.append([mark["Eng"], Eng_gather])
	elif Chi_gather != "":
		group.append([mark["Chi"], Chi_gather])

	return group

def ch_check(cha):
	x = ord(cha)

	if x >= 0x2e80 and x <= 0x33ff:
		return True

	elif x >= 0xff00 and x <= 0xffef:
		return True

	elif x >= 0x4e00 and x <= 0x9fbb:
		return True
	elif x >= 0xf900 and x <= 0xfad9:
		return True

	elif x >= 0x20000 and x <= 0x2a6d6:
		return True

	elif x >= 0x2f800 and x <= 0x2fa1d:
		return True

	else:
		return False
	
def en_check(cha):
	x = ord(cha)

	if x >= 97 and x <= 122:
		return True
	elif x >= 65 and x <= 90:
		return True
	else: return False

print split_ch_en(data)
