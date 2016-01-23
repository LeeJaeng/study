#!/usr/local/bin/python3
def _range(start, end, step=1):
    result = start
    while result < end:
        yield result
        result += step
def main():
    start = 1800
    end = 2014
    step = 3
    per_line = 5
    year = start
    count = 1
    #for year in range(start, end+1):
    for year in _range(start, end+1):
        if count % per_line == 0:
            print(year, end="\n")
        else :
            print(year, end="\t")
        year += step
        count += 1
if __name__ == '__main__': main()