#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys

def main(argv):
	if len(argv) < 2:
		print "Usage %s <fil>" %argv[0];
		sys.exit();

	filein = open(argv[1], "rw");
	fileout = open("outfile.txt", "w");
	
	for l in filein:
		result = ''.join([i for i in l if not i.isdigit()])
		result = result.lower();
		result = result.strip();
		result = result.replace("ö", "o");
		result = result.replace("å", "a");
		result = result.replace("ä", "a");
		print result;
		result = result.strip();
		fileout.write('"' + result + '",');

	filein.close();
	fileout.close();

if __name__ == "__main__":
	main(sys.argv)
