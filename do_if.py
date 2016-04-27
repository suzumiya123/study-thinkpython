#!/usr/bin/env python3
# -*'- conding: utf-8 -*-

height = float(input('请输入身高:'))
weight = float(input('请输入体重:'))

bmi = weight/(height * height)

if bmi < 18.5:
	print('过轻 ')
elif bmi > 18.5 and bmi <25:
	print('正常')
elif bmi > 28 and bmi <28:
	print('过重 ')
elif bmi > 28 and bmi < 32:
	print('肥胖')
else:
	print('严重肥胖 ')
pass


