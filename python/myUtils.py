# coding=utf-8

demo = ["File","Edit","View","Search","Document","Project","Tools","Browser","Emmet","Windows","Help"
,['zhaoht','zht','jarod','zhao','ht_z',['a','b','c','d',['金水区','检察院']]]]


# 简单递归
def printItem(items):
	for item in items:
		if isinstance(item, list):
			printItem(item)
		else:
			print(item)

# 返回列表中的某个值,根据索引
def getItem(data,i):
	return data[i]
