# -*- coding : utf-8 -*-
import re


while True:

	cache = 1

	cmd = input("명령 >> ")

	# 나가기 부분
	p = re.compile("^나가기|^종료|^끝")
	if p.match(cmd) != None:
		print("종료합니다.")
		exit(0)
	


	# 출력 부분
	p = re.compile("^출력")
	if p.match(cmd) != None:
		printString = cmd.partition(' ')[2]
		print(printString)
		#print(cmd.replace("출력 ", "").replace("\"", ""))

		cache -= 1



	# 입력 부분
	p = re.compile("^입력")
	if p.match(cmd) != None:
		print("[%s]입력됨" % input())

		cache -= 1

	if cache == 1:
		print("이해할 수 없는 명령어입니다.")


