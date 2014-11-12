#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import random
import hashlib

def main():
	i = 0;
	f = open("saol.txt", "r");
	for l in f:
		if(l[0] == 's'):
			if len(l) == 14:
					# create email
					email = l + "@gmail.com";
					print email;
					#print l
					i += 1;

	print i

if __name__ == "__main__":
	main()
