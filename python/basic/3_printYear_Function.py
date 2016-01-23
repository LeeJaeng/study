#!/usr/local/bin/python3


def print_year(start, end, step=1, per_line=10):
	year = start
	count = 1

	while year <= end:
		if count % per_line == 0:
			print(year, end = "\n")
		else:
			print(year, end = "\t")

		count += 1
		year += step




def main():
	print_year(1900, 2000, 5, 5)



if __name__ == '__main__': main()