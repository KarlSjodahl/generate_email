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

kvinnligt_fornamn = ["alice", "elsa", "julia", "ella", "maja", "ebba", "emma", "linnea", 
					"molly", "alva", "wilma", "agnes", "klara", "nellie", "isabelle", "olivia", "alicia",
					"ellen", "lilly", "stella","freja","saga","emilia","astrid","ida","nova","moa","ssabella",
					"alma","vera","signe","elin","ester","selma","ellie","amanda","sara","tyra","tuva","felicia",
					"matilda","elvira","leah","sofia","siri","hanna","lovisa","lova","nora","edith","tilde","meja",
					"thea","ines","liv","emelie","filippa","nathalie","elise","juni","tilda","leia","melissa","stina",
					"sigrid","svea","ingrid","my","ronja","marta","tindra","lisa","jasmine",
					"livia","minna","cornelia","iris","majken","joline","linn","emmy","hilda","mira","elina","greta",
					"josefin","lykke","vilda","anna","hedvig","tove","lina","annie","hedda","sofie","viktoria"
					"frida","maria","rut", "evelina" ,"novalie"];

manligt_fornamn = ["william","oscar","oskar","lucas","hugo","elias","alexander","liam","charlie","oliver","filip","leo"
					"viktor","vincent","emil","axel","anton","erik","olle","theo","ludvig","isak","arvid","gustav",
					"noah","edvin","melvin","alfred","max","albin","elliot","nils","adam",
					"sixten","leon","wilmer","benjamin","viggo","alvin","theodor","jacob","valter","kevin","melker",
					"felix","simon","adrian","goran","amir","gabbe",
					"casper","noel","jonathan","gabriel","love","malte","jack","mohamed","rasmus","milo","carl",
					"karl","harry","josef","samuel","sebastian","ville","linus","wilhelm","david","august","ebbe",
					"elton","neo","loke","joel","vilgot","hampus","vidar","daniel","elvin","sigge","elis","sam",
					"john","eddie","alex","milton","frank","aron","maximilian","otto","henry","edward","svante",
					"mio","ali","julian","tim","hjalmar","ivar","colin","hannes","tage","levi","matteo", "kalle", "svante"
					"robban", "nisse", "pelle","henke","sebbe","matte","peppe","fredrik","fredde","marcus","markus","mathias",
					"mattias","patrik"];

efternamn = ["nilsson", "andersson","johansson","olsson", "ohlsson", "bengtsson","karlsson","eriksson","larsson","persson",
			"svensson","gustafsson","pettersson","jonsson","jansson","hansson","petersson","carlsson","lindberg",
			"magnusson","gustavsson","lindstrom","olofsson","lindgren","axelsson","lundberg","jakobsson","bergstrom",
			"lundgren","berg","berglund","fredriksson","mattsson","sandberg","henriksson","sjoberg","forsberg","lindqvist",
			"hakansson","danielsson","engstrom","Llind","lundin","eklund","gunnarsson","samuelsson","fransson","holm","johnsson",
			"bergman","holmberg","nystrom","lundqvist","arvidsson","bjork","isaksson","nyberg","soderberg","martensson","wallin","nordstrom",
			"lundstrom","eliasson","bjorklund","berggren","ström","nordin","sandstrom","hermansson","aberg","holmgren","ekstrom",
			"sundberg","hedlund","sjogren","martinsson","mansson","dahlberg","oberg","abrahamsson","stromberg","hellstrom",
			"jonasson","akesson","norberg","blomqvist","blom","andreasson","sundstrom","astrom","ek","goransson","lindholm","lofgren",
			"ivarsson","soderstrom","nyman","jensen","bergqvist","falk"];

def get_random_domains():
	return random.choice(domains);

def get_random_kfornamn():
	return random.choice(kvinnligt_fornamn);

def get_random_mfornamn():
	return random.choice(manligt_fornamn);

def get_random_efternamn():
	return random.choice(efternamn);

def get_random_number():
	number = random.randrange(1,100+1);
	return str(number);

def get_kfornamn():
	kfornamn = open("kfornamn.txt").readlines();

def get_mfornamn():
	mfornamn = open("mfornamn.txt").readlines();

def get_domain():
	domain = open("doman.txt").readlines();

def get_efternamn():
	efternamn = open("efternamn.txt").readlines();

def hash_to_compare(hashed_mail, email):
	#Open the hashed values to compare with
	file = open("emailhash.csv", "r").readlines()
	for l in file:
		md5 = l.replace('"', '');
		#If we have a match, save it to a file
		if(md5 == hashed_mail):
			print "FOUND A MATCH!!!! Email: %s md5: %s" % (email,hashed_mail);
			f = open("found_mail.txt", "a");
			f.write(email + " " + hashed_mail + "\n");
			f.close();

def generate_mfornamn_efternamn_mail():
	email = get_random_mfornamn() + "." + get_random_efternamn() + "@" + get_random_domains();
	print email;
	return email;

def generate_kfornamn_efternamn_mail():
	email = get_random_kfornamn() + "." + get_random_efternamn() + "@" + get_random_domains();
	print email;
	return email;

def generate_mfornamn_efternamn_mail1():
	email = get_random_mfornamn() + "_" + get_random_efternamn() + "@" + get_random_domains();
	print email;
	return email;

def generate_kfornamn_efternamn_mail1():
	email = get_random_kfornamn() + "_" + get_random_efternamn() + "@" + get_random_domains();
	print email;
	return email;

def generate_mfornamn_mail():
	email = get_random_mfornamn() + "@" + get_random_domains();
	print email;
	return email;

def generate_kfornamn_mail():
	email = get_random_kfornamn() + "@" + get_random_domains();
	print email;
	return email;

def generate_mformnamn_number_mail():
	email = get_random_mfornamn() + get_random_number() + "@" + get_random_domains();
	print email;
	return email;

def generate_kformnamn_number_mail():
	email = get_random_kfornamn() + get_random_number() + "@" + get_random_domains();
	print email;
	return email;

def generate_hash(email):
	m = hashlib.md5();
	m.update(email);
	#What is the md5 sum of the mail?
	hashed_mail = m.hexdigest();
	print hashed_mail;
	return hashed_mail;

def main():
	number_mails = 0

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_kfornamn_efternamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_mfornamn_efternamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_kfornamn_efternamn_mail1();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_mfornamn_efternamn_mail1();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_kfornamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_mfornamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_kformnamn_number_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);

	for x in range(0, 100000):
		number_mails = number_mails + 1;
		email = generate_mformnamn_number_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);	

	print "Number of generated mails %s " %number_mails;

if __name__ == "__main__":
	main()
