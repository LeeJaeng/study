#!/usr/local/bin/python3
# 맨 위의 줄은 shebang line이라고 해서
# python 파일을 chmod +x dummy.py
# 이렇게 선언을 하면 dummy.py가 실행을 할 수 있는 상태가 된다.
# 그 때 맨 위의 Shebang라인에 적힌 것을 이용하여 실행한다.

import sys
def main():
	"""program entry point
	"""
	print(sys.platform + ": Hello world")
if __name__ == '__main__':
	main()
