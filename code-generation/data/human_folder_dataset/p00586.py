def run(infile,outfile):
	for line in infile.readlines():
		print >> outfile,sum(map(int,line.rstrip().split()))

if __name__ == "__main__":
	import sys
	run(sys.stdin, sys.stdout)