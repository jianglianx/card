#coding:utf-8
print '#'*50
print '                   名片管理系统'
print '                 1.添加一个名片'
print '                 2.删除一个名片'
print '                 3.修改一个名片'
print '                 4.查看所有名片'
print '                 5.查找名片'
print '                 6.退出系统'
print '#'*50

card_infor=[]
while True:
	num = input ('请输入序号：')

	if num==1:
		new_name =raw_input('请输入新的名字；')
		new_QQ = raw_input('请输入新的QQ；')
		new_weixin = raw_input('请输入新的微信；')

		new_infor={}
		new_infor['name']=new_name
		new_infor['QQ']=new_QQ
		new_infor['weixin']=new_weixin

		card_infor.append(new_infor)
#		print card_infor


	elif num==2:
		pass
	elif num==3:
		pass
	elif num==4:
		print '姓名\tQQ\t微信'
		for temp in card_infor:
			print '%s\t%s\t%s'%(temp['name'],temp['QQ'],temp['weixin'])

	
	elif num==5:
		flag = 0
		find_name = raw_input('请输入你要查找的名字：')
		for temp in card_infor:
			if find_name==temp['name']:
				print '%s\t%s\t%s'%(temp['name'],temp['QQ'],temp['weixin'])
				flag = 1
				break
		if flag == 0:
			print '没有此人信息。。。。'
	elif num==6:
		break
	else:
		print ('输入有误')

	print ' '	
