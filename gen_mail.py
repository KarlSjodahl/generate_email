#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# Generate emails and compare them to a list of md5 sums.
# Author: Karl Sjödahl
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


efternamn = ["abrahamsson","adamsson","adolfsson","af","ahlberg","ahlén","ahlgren","ahlin","ahlqvist","ahlstrand","ahlstrom",
			"ahl","albertsson","albinsson","alexandersson","alfredsson","algotsson","almén","almgren","almqvist","almstrom","alm","anderberg",
			"andersen","andersson","andreasson","andrén","andré","antonsson","appelgren","appelqvist","arnesson","aronsson","arvidsson",
			"ask","asplund","asp","assarsson","augustsson","axelsson","axén","backlund","backman","backstrom","back","bark","beckman",
			"bengtsson","benjaminsson","bergdahl","bergendahl","berger","berggren","bergh","bergkvist","berglind","berglin","berglund",
			"bergman","bergmark","bergquist","bergqvist","bergstedt","bergsten","bergstrand","bergstrom","bergvall","berg","berlin",
			"berndtsson","bernhardsson","berntsson","bertilsson","birgersson","bjurstrom","bjorck","bjorklund","bjorkman","bjorkqvist",
			"bjork","bjorling","bjornberg","bjornsson","bjorn","bladh","blad","blixt","blomberg","blomdahl","blomgren","blomkvist",
			"blomquist","blomqvist","blom","boberg","bodén","bodin","bogren","bohlin","bohman","bolin","boman","bondesson","borgstrom",
			"borg","bostrom","brandt","bratt","brink","broberg","brodén","brodin","brolin","broman","brorsson","brostrom","bruhn","brundin",
			"bryngelsson","brandstrom","brannstrom","burman","burstrom","bylund","bystrom","backlund","backman","backstrom","back",
			"borjesson","carlberg","carlén","carlson","carlsson","carlstrom","cederberg","cedergren","cederholm","cederlund","ceder",
			"christensen","christensson","christiansson","claesson","classon","collin","dahlberg","dahlén","dahlgren","dahlin",
			"dahlman","dahlqvist","dahlstrom","dahl","damberg","danielsson","davidsson","degerman","de","edberg","edgren","edholm",
			"edin","edlund","edman","edstrom","edvardsson","edvinsson","ehn","einarsson","ekberg","ekblad","ekblom","ekdahl",
			"ekelund","ekholm","eklund","eklof","ekman","ekstedt","ekstrand","ekstrom","ekvall","ek","elfstrom","elfving","elg",
			"eliasson","elofsson","emanuelsson","emilsson","enberg","engberg","engblom","engdahl","englund","engman","engqvist",
			"engstrand","engstrom","engvall","eng","enqvist","enstrom","ericson","ericsson","eriksson","erlandsson","ersson",
			"esbjornsson","eskilsson","evertsson","fagerberg","fagerlund","fagerstrom","fahlén","fahlgren","fahlstrom","falck",
			"falk","fast","ferm","fernstrom","filipsson","flink","flodin","fogelberg","folkesson","forsberg","forsell","forsgren",
			"forslund","forsman","forsmark","forsstrom","forss","fors","frank","fransén","fransson","franzén","fredin","fredlund",
			"fredriksson","freij","friberg","frick","fridell","fridén","fridh","fridlund","frid","friman","frisk","fritz","from",
			"froberg","frojd","falt","gabrielsson","gerdin","gidlund","gillberg","glad","glans","gradin","grahn","granath","granat",
			"granberg","grankvist","granlund","granqvist","granstrom","gran","green","gren","grip","grundstrom","gronberg",
			"gronlund","gronqvist","gronvall","gudmundsson","gullberg","gummesson","gunnarsson","gustafsson","gustavsson",
			"goransson","haag","hagberg","hagelin","haglund","hagman","hagstrom","hallberg","halldén","halldin","hallén",
			"hallgren","hallin","hallman","hallqvist","hallstrom","hall","halvarsson","hamberg","hammarberg","hammarlund",
			"hammarstrom","hammar","hamrin","hansen","hansson","haraldsson","harrysson","hedberg","hedblom","hedén","hedin",
			"hedlund","hedman","hedqvist","hedstrom","hedvall","hed","helander","helgesson","helin","hellberg","hellgren",
			"hellman","hellqvist","hellsten","hellstrand","hellstrom","helmersson","hemmingsson","henningsson","henning",
			"henriksson","hermansson","hilmersson","hjalmarsson","hjelm","hjerpe","hjorth","hjort","holgersson","holmberg",
			"holmén","holmer","holmgren","holmkvist","holmlund","holmquist","holmqvist","holmstedt","holmstrom","holm",
			"holst","hugosson","hultberg","hultén","hultgren","hultin","hultman","hultqvist","hult","hurtig","hakansson",
			"hard","hagglund","haggstrom","hagg","hallgren","hallstrom","hall","hogberg","hoglund","hogman","hogstrom",
			"horberg","ingemarsson","ingvarsson","isaksson","isberg","israelsson","ivarsson","jacobsson","jakobsson",
			"jansson","jarl","jensen","jeppsson","jernberg","joelsson","johannesson","johannisson","johansen","johansson",
			"johnson","johnsson","jonasson","jonsson","josefsson","juhlin","julin","jonsson","jorgensen","kallin","karlberg",
			"karlen","karlsson","karlstrom","kempe","kihlberg","kihlstrom","kjellberg","kjellgren","kjellin","kjellman",
			"kjellstrom","kjell","klaesson","klang","klasson","klingberg","kling","klint","knutsson","konradsson","kraft",
			"krantz","kristensson","kristiansson","kristoffersson","kron","krook","kroon","kruse","kullberg","kvarnstrom",
			"kvist","kack","kallberg","kallgren","kallman","kallstrom","kall","kampe","kohler","lagergren","lagerqvist",
			"lagerstrom","lager","landberg","landén","landgren","landin","landstrom","lans","lantz","larsen","larsson",
			"leandersson","leander","ledin","leijon","lejon","lennartsson","levin","lidberg","lidén","lidman","lidstrom",
			"lif","lilja","liljedahl","liljegren","liljekvist","lindahl","lindberg","lindblad","lindblom","lindbom","lindborg",
			"lindback","lindeberg","lindell","lindén","linderoth","linder","linde","lindfors","lindgren","lindholm","lindh",
			"lindkvist","lindman","lindmark","lindquist","lindqvist","lindroth","lindskog","lindstedt","lindstrand","lindstrom",
			"lindvall","lind","ling","ljungberg","ljungdahl","ljunggren","ljungkvist","ljungqvist","ljungstrom","ljung","lorentzon",
			"lovén","ludvigsson","lundahl","lundberg","lundblad","lundborg","lundback","lundell","lundén","lundgren","lundholm",
			"lundh","lundin","lundkvist","lundmark","lundquist","lundqvist","lundstedt","lundstrom","lundvall","lund","langstrom",
			"lang","lofberg","lofdahl","lofgren","lofqvist","lofstedt","lofstrand","lofstrom","lof","lonnberg","lonnqvist","lonn",
			"lovgren","loof","magnusson","malmberg","malmborg","malmgren","malmkvist","malmqvist","malmros","malmsten","malmstrom",
			"malm","marklund","markstrom","markusson","martinsson","matsson","mattiasson","mattisson","mattsson","medin","meijer",
			"melander","melin","mellberg","mellgren","mikaelsson","moberg","modig","modin","molander","molin","morén","morin","mossberg",
			"müller","mansson","martensson","moller","mork","nelson","nielsen","niemi","niklasson","nilsson","norberg","nordahl",
			"nordberg","nordell","nordén","nordgren","nordh","nordin","nordkvist","nordlander","nordling","nordlund","nordmark",
			"nordquist","nordqvist","nordstrand","nordstrom","nordvall","nord","norell","norén","norgren","norin","norlander",
			"norling","norlin","norman","norrby","norrman","norstrom","nyberg","nygren","nyholm","nykvist","nylander","nylén",
			"nylund","nyman","nyqvist","nyrén","nystedt","nystrom","naslund","nasman","nasstrom","ohlsson","olander","olausson",
			"olin","olofsson","olovsson","olsen","olsén","olsson","oscarsson","oskarsson","ottosson","palmér","palmgren","palmqvist",
			"palm","paulsson","pedersen","pehrsson","persson","petersen","peterson","petersson","pettersson","pihl","palsson",
			"qvarnstrom","qvist","ragnarsson","rahm","ramberg","ramstrom","rapp","rask","rasmussen","rasmusson","rehn","reinholdsson",
			"renberg","renstrom","rickardsson","ringdahl","ringstrom","ring","risberg","robertsson","rodin","roos","rosander",
			"rosberg","rosell","rosenberg","rosendahl","rosengren","rosenkvist","rosenqvist","rosén","roslund","rosvall","ros",
			"roth","rundberg","rundgren","rundqvist","rutgersson","ryberg","rydberg","rydell","rydén","rydstrom","ryd","rylander",
			"ronnberg","ronnback","ronnqvist","ronn","sahlberg","sahlén","sahlin","sahlstrom","salomonsson","samuelsson","sandahl",
			"sandberg","sandell","sandén","sander","sandgren","sandin","sandqvist","sandstrom","sand","schmidt","schroder","schultz",
			"schon","seger","selander","selberg","selin","sigfridsson","simonsson","sjunnesson","sjoberg","sjoblom","sjodahl","sjodin",
			"sjogren","sjoholm","sjokvist","sjolander","sjolin","sjolund","sjoqvist","sjostedt","sjosten","sjostrand","sjostrom","sjoo",
			"skoglund","skog","skoog","skold","smedberg","smith","sonesson","spangberg","staaf","stark","steen","stefansson","stenberg",
			"stenlund","stenman","stenmark","stenqvist","stensson","stenstrom","stenvall","sten","sterner","stolpe","stoltz","stolt",
			"storm","strandberg","strand","stridh","strid","stromberg","stromback","stromgren","stromqvist","strom","sturesson","stahl",
			"stalberg","stalnacke","stal","sundberg","sundelin","sundell","sundén","sundgren","sundin","sundkvist","sundman","sundquist",
			"sundqvist","sundstrom","sundvall","sund","sunesson","svahn","svanberg","svanstrom","svantesson","svan","svedberg","svedin",
			"svedlund","svenningsson","svensk","svensson","svard","safstrom","sall","soderberg","soderblom","sodergren","soderholm",
			"soderkvist","soderlind","soderlund","soderman","soderqvist","soderstrom","soder","sorensen","sorensson","sorman","tapper",
			"tell","thelander","thelin","thomasson","thorell","thorén","thorsell","thorsson","thor","thulin","thunberg","thuresson",
			"thorn","tillberg","tillman","tjernstrom","tornberg","torstensson","trulsson","trygg","tufvesson","turesson","tuvesson",
			"tornberg","tornblom","torngren","tornkvist","tornqvist","ulander","vahlberg","valfridsson","vallgren","vallin","vall",
			"van","vedin","velander","vennberg","vernersson","vestberg","vesterberg","vestergren","vesterlund","vestin","vestling",
			"vestlund","vestman","viberg","vidén","vigren","vikberg","viklund","vikman","vikstrom","viktorsson","vik","vilhelmsson",
			"vinberg","von","wahlberg","wahlgren","wahlqvist","wahlstrom","wallberg","wallén","wallgren","wallin","wallman","wallstrom",
			"wall","wedin","welander","welin","wendel","wennberg","wennerberg","wennerstrom","wennstrom","werner","wessman","westberg",
			"westerberg","westergren","westerlund","wester","westin","westling","westlund","westman","wiberg","wickman","wickstrom",
			"widell","widén","widlund","wihlborg","wiklund","wikman","wikstrom","wik","wilhelmsson","wiman","winberg","wirén",
			"zachrisson","zackrisson","zakrisson","zander","zetterberg","zetterlund","zetterstrom","aberg","agren","ahlander",
			"ahlén","ahlin","ahman","ahs","akerberg","akerblom","akerlind","akerlund","akerman","akerstrom","akesson","alander",
			"alund","aman","asberg","aslund","astrand","astrom","oberg","odman","ogren","ohlin","ohlund","ohman","ohrn","olund","oman",
			"oqvist","orn","ostberg","osterberg","ostergren","osterlund","osterman","oster","ostling","ostlund","ostman","ostrom","ost"];

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

def main(argv):
	number_mails = 0
	if(len(argv) < 2):
		f = open("generated_emails.txt", "a");
		print "Using generated_emails.txt";
	else:
		f = open(argv[1],"a");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_kfornamn_efternamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_mfornamn_efternamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_kfornamn_efternamn_mail1();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_mfornamn_efternamn_mail1();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_kfornamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_mfornamn_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_kformnamn_number_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	for x in range(0, 10):
		number_mails = number_mails + 1;
		email = generate_mformnamn_number_mail();
		hash1 = generate_hash(email);
		hash_to_compare(hash1, email);
		f.write(email + " " + hash1 + "\n");

	f.close();		

	print "Number of generated mails %s " %number_mails;

if __name__ == "__main__":
	main(sys.argv)
