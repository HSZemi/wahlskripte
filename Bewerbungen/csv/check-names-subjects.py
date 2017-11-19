#! /usr/bin/env python3

import csv

lists = {}

with open("kandidatenliste_aus_sos_20162.csv", "r") as f:
	
	skipped = True
	liste = ""
	nr = ""
	
	for line in f:
		
		if(line.strip() == ""):
			skipped = True
		else:
			items = line.split("\t")
			
			if(items[1] == ""):
				liste = items[0]
				lists[liste] = {}
			elif(skipped):
				nr = items[0]
				matnr = items[1]
				nname = items[2]
				vname = items[3].strip()
				lists[liste][nr] = {'matnr':matnr,'vname':vname,'nname':nname,'faecher':set()}
				skipped = False
			else:
				fach = items[3].strip()
				lists[liste][nr]['faecher'].add(fach)

#for liste in lists:
	#for nr in sorted(lists[liste]):
		#print(liste, nr, lists[liste][nr]['matnr'], lists[liste][nr]['vname'], lists[liste][nr]['nname'], " | ".join(lists[liste][nr]['faecher']))

for liste in ('RCDS','JUSOS','LHG','LUST','LISTE','KULT','GHGP','SDS'):
	with open('{}.csv'.format(liste), "r") as f:
		reader = csv.DictReader(f, delimiter="\t")
		for line in reader:
			nr = line['Listenplatz']
			matnr = line['Matrikelnummer']
			vname = line['Vorname']
			nname = line['Nachname'] 
			fach = line['Studienfach']
			
			entry = lists[liste][nr]
			
			if(matnr != entry['matnr']):
				print("{} {} MATRIKELNUMMER: {} <> {}".format(liste, nr, entry['matnr'], matnr))
				
			if(nname != entry['nname']):
				print("{} {} NACHNAME: {} <> {}".format(liste, nr, entry['nname'], nname))
			
			vnameset = set(vname.split(" "))
			if not vnameset.issubset(set(entry['vname'].split(" "))):
				print("{} {} VORNAME: {} <> {}".format(liste, nr, entry['vname'], vname))
				
			fachset = set(fach.split(" | "))
			if not fachset.issubset(entry['faecher']):
				print("{} {} FAECHER: {} <> {}".format(liste, nr, " | ".join(entry['faecher']), fach))
				