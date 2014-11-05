#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# Run with:
# python test_md5.py text_file_that_contains_email.txt
# Author: Karl Sjödahl <karl.sjodahl@gmail.com>

import hashlib
import sys

def main(argv):
	if len(argv) < 2:
		print "Usage %s <text-file with emails>" %argv[0];
		sys.exit();

	file = open(argv[1], "r");
	for l in file:
		m = hashlib.md5();
		m.update(l);
		newhash = m.hexdigest();
 		print "Email: %s md5: %s " %(l, newhash);
		if(hash == newhash):
			print "Match!";

if __name__ == "__main__":
	main(sys.argv)
