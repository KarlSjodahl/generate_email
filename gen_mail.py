#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# Generate emails and compare them to a list of md5 sums.
# Author: Karl Sjödahl <karl.sjodahl@gmail.com>
###############################################

import random
import hashlib

domains = ["hotmail.com", "gmail.com", "live.com", "yahoo.se", "yahoo.com", "hotmail.se", "live.se", "telia.com", "bredband.se", "bredband.com",
			"swipnet.se","spray.se", "msn.com", "msn.se", "mail.com","sverige.nu","passagen.se","hotbrev.com","hushmail.com","hush.com",
			"home.se","bredband.net","bahnhofbredband.se","mail.ru","rocketmail.com",]

kvinnligt_fornamn = ["Alice", "Elsa", "Julia", "Ella", "Maja", "Ebba", "Emma", "Linnea", 
					"Molly", "Alva", "Wilma", "Agnes", "Klara", "Nellie", "Isabelle", "Olivia", "Alicia",
					"Ellen", "Lilly", "Stella","Freja","Saga","Emilia","Astrid","Ida","Nova","Moa","Isabella",
					"Alma","Vera","Signe","Elin","Ester","Selma","Ellie","Amanda","Sara","Tyra","Tuva","Felicia",
					"Matilda","Elvira","Leah","Sofia","Siri","Hanna","Lovisa","Lova","Nora","Edith","Tilde","Meja",
					"Thea","Ines","Liv","Emelie","Filippa","Nathalie","Elise","Juni","Tilda","Leia","Melissa","Stina",
					"Sigrid","Svea","Ingrid","My","Ronja","Marta","Tindra","Lisa","Jasmine",
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

efternamn = ["Nilsson", "Andersson","Johansson","Olsson", "Ohlsson", "Bengtsson","Karlsson","Eriksson","Larsson","Persson",
			"Svensson","Gustafsson","Pettersson","Jonsson","Jansson","Hansson","Petersson","Carlsson","Lindberg",
			"Magnusson","Gustavsson","Lindstrom","Olofsson","Lindgren","Axelsson","Lundberg","Jakobsson","Bergström",
			"Lundgren","Berg","Berglund","Fredriksson","Mattsson","Sandberg","Henriksson","Sjoberg","Forsberg","Lindqvist",
			"Håkansson","Danielsson","Engström","Lind","Lundin","Eklund","Gunnarsson","Samuelsson","Fransson","Holm","Johnsson",
			"Bergman","Holmberg","Nyström","Lundqvist","Arvidsson","Björk","Isaksson","Nyberg","Söderberg","Mårtensson","Wallin","Nordström",
			"Lundström","Eliasson","Björklund","Berggren","Ström","Nordin","Sandström","Hermansson","Åberg","Holmgren","Ekström",
			"Sundberg","Hedlund","Sjögren","Martinsson","Månsson","Dahlberg","Öberg","Abrahamsson","Strömberg","Hellström",
			"Jonasson","Åkesson","Norberg","Blomqvist","Blom","Andreasson","Sundström","Astrom","Ek","Göransson","Lindholm","Lofgren",
			"Ivarsson","Söderström","Nyman","Jensen","Bergqvist","Falk"];

def get_random_domains():
	return random.choice(domains);

def get_random_kfornamn():
	return random.choice(kvinnligt_fornamn);

def get_random_mfornamn():
	return random.choice(manligt_fornamn);

def get_random_efternamn():
	return random.choice(efternamn);

def get_kfornamn():
	kfornamn = open("kfornamn.txt").readlines();


def get_mfornamn():
	mfornamn = open("mfornamn.txt").readlines();

def get_domain():
	domain = open("doman.txt").readlines();

def get_efternamn():
	efternamn = open("efternamn.txt").readlines();

def get_md5():
	print "get_md5";
	for x in range(0, 100000):
		# build an email and random pick namn.efternamn@domain
		email = get_random_mfornamn() + "." + get_random_efternamn() + "@" + get_random_domains();
		print email;
		m = hashlib.md5();
		m.update(email);
		#What is the md5 sum of the mail?
		hashed_mail = m.hexdigest();
		print hashed_mail;
		number = 0

		#Open the hashed values to compare with
		file = open("emailhash.csv", "r").readlines()
		for l in file:
			md5 = l.replace('"', '');
			number = number+1;
			#If we have a match, save it to a file
			if(md5 == hashed_mail):
				print "FOUND A MATCH!!!! Email: %s md5: %s" % (email,hashed_mail);
				f = open("found_mail.txt", "w");
				f.write(email + " " + hashed_mail);



	f.close();
	print "Number of unmatched md5-sums: %d " %number;

def main():
	get_md5();
	#for x in range(0,10):
	#	gen = generate_md5_from_email();
	#	for l in gen
	#		print l;

	#generate_md5_from_email();


if __name__ == "__main__":
	main()
