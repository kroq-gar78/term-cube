import sys
from pykociemba import search
from time import time

def solve(s):
	errors = {
		'Error 1': 'There is not exactly one facelet of each colour',
		'Error 2': 'Not all 12 edges exist exactly once',
		'Error 3': 'Flip error: One edge has to be flipped',
		'Error 4': 'Not all corners exist exactly once',
		'Error 5': 'Twist error: One corner has to be twisted',
		'Error 6': 'Parity error: Two corners or two edges have to be exchanged',
		'Error 7': 'No solution exists for the given maxDepth',
		'Error 8': 'Timeout, no solution within given time'
	}
	t = time()
	res = search.Search().solution(s, 24, 1000, False).strip()
	if res in errors:
		return res, time() - t
	else:
		return res, time() - t


if __name__=='__main__':
    if len(sys.argv) > 1:
        print(solve(sys.argv[1]))
    else:
        print('Usage: kociemba <cubestring>\nfor example:\nkociemba DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')
