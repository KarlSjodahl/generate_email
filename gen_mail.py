#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import random
import hashlib

domains = ["hotmail.com", "gmail.com", "live.com"]

kvinnligt_fornamn = ["Alice", "Elsa", "Julia", "Ella", "Maja", "Ebba", "Emma", "Linnea", 
					"Molly", "Alva", "Wilma", "Agnes", "Klara", "Nellie", "Isabelle", "Olivia", "Alicia",
					"Ellen", "Lilly", "Stella","Freja","Saga","Emilia","Astrid","Ida","Nova","Moa","Isabella",
					"Alma","Vera","Signe","Elin","Ester","Selma","Ellie","Amanda","Sara","Tyra","Tuva","Felicia",
					"Matilda","Elvira","Leah","Sofia","Siri","Hanna","Lovisa","Lova","Nora","Edith","Tilde","Meja",
					"Thea","Ines","Liv","Emelie","Filippa","Nathalie","Elise","Juni","Tilda","Leia","Melissa","Stina",
					"Sigrid","Svea","Ingrid","My","Ronja","Märta","Tindra","Lisa","Jasmine",
					"Livia","Minna","Cornelia","Iris","Majken","Joline","Linn","Emmy","Hilda","Mira","Elina","Greta",
					"Josefin","Lykke","Vilda","Anna","Hedvig","Tove","Lina","Annie","Hedda","Sofie","Viktoria"
					"Frida","Maria","Rut", "Evelina" ,"Novalie"];

manligt_fornamn = ["William","Oscar","Oskar","Lucas","Hugo","Elias","Alexander","Liam","Charlie","Oliver","Filip","Leo"
					"Viktor","Vincent","Emil","Axel","Anton","Erik","Olle","Theo","Ludvig","Isak","Arvid","Gustav",
					"Noah","Edvin","Melvin","Alfred","Max","Albin","Elliot","Nils","Adam",
					"Sixten","Leon","Wilmer","Benjamin","Viggo","Alvin","Theodor","Jacob","Valter","Kevin","Melker",
					"Felix","Simon","Adrian",
					"Casper","Noel","Jonathan","Gabriel","Love","Malte","Jack","Mohamed","Rasmus","Milo","Carl",
					"Karl","Harry","Josef","Samuel","Sebastian","Ville","Linus","Wilhelm","David","August","Ebbe",
					"Elton","Neo","Loke","Joel","Vilgot","Hampus","Vidar","Daniel","Elvin","Sigge","Elis","Sam",
					"John","Eddie","Alex","Milton","Frank","Aron","Maximilian","Otto","Henry","Edward","Svante",
					"Mio","Ali","Julian","Tim","Hjalmar","Ivar","Colin","Hannes","Tage","Levi","Matteo"];

efternamn = ["Nilsson", "Andersson","Johansson","Olsson", "Ohlsson", "Bengtsson"];

#letters = string.ascii_lowercase[:20]

def get_random_domains():
	return random.choice(domains);

def get_random_kfornamn():
	return random.choice(kvinnligt_fornamn);

def get_random_mfornamn():
	return random.choice(manligt_fornamn);

def get_random_efternamn():
	return random.choice(efternamn);

def generate_md5_from_email():
	print "generate_md5_from_email";
	email = get_random_mfornamn() + "." + get_random_efternamn() + "@" + get_random_domains();
	print email;
	m = hashlib.md5();
	m.update(email);
	print m.hexdigest();
	if 

def get_md5():
	number = 0
	file = open("emailhash.csv", "r");
	for l in file:
		md5 = l.replace('"', '');
		number = number+1;
		#print md5;

	print "Number of unmatched md5-sums: %d " %number;

def main():
	#get_random_domains();
	#get_random_kfornamn();
	#get_random_mfornamn();
	#get_md5();
	generate_md5_from_email();


if __name__ == "__main__":
	main()
