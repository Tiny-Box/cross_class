#-*- coding:utf-8
#当然 这个是C++判断回文数的法子 学C、C++的基本功→ 。→
def check_C(number):
	b = 0
    #基本的回文数的数字判断 其实还可以只用一个变量
	while (number):
		a = number % 10
		b = b * 10 + a
		number /= 10

	return b

#这个是python的法子 我擦 列表的内置函数好好用！！！
def check_python(number):
	#先转换成字符串才能转成列表 直接用int转会报错
	number = str(number)

	#将数字的每一位数字转成列表的元素 然后用列表的函数反转
	num_list = list(number)
	num_list.reverse()

	#将反转了的列表连起来
	newnum = ''.join(num_list)

	#这个时候newnum其实还是字符串 所以用已转成字符串的number比对
	if number == newnum:
		return True

for i in range (1, 200+1):
	if (i*i == check_C(i*i)):
		print i

for i in range (1, 200+1):
	if check_python(i*i):
		print i

