#! /usr/bin/env python3

import csv

wvz = {}

with open("wvz.csv", "r") as f:
	reader = csv.DictReader(f, delimiter="\t")
	for line in reader:
		lfdnr = line['Lfd.Nr.'].strip()
		vname = line['Vorname'].strip()
		nname = line['Nachname'].strip()
		matnr = line['Matrikelnummer'].strip()
		
		wvz[matnr] = line

with open("data.csv", "r") as f:
	reader = csv.DictReader(f, delimiter="\t")
	for line in reader:
		platz = line['Listenplatz'].strip()
		vname = line['Vorname'].strip()
		nname = line['Nachname'].strip()
		matnr = line['Matrikelnummer'].strip()
		
		if matnr not in wvz:
			print("Nicht gefunden: {} {} {} {}".format(platz, vname, nname, matnr))
		else:
			if(vname != wvz[matnr]['Vorname']):
				if vname not in wvz[matnr]['Vorname'].split(" "):
					print("VORNAME	{}	{}	{}	{}	{}	{}".format(platz, vname, nname, matnr, wvz[matnr]['Vorname'], wvz[matnr]['Nachname']))
			if(nname != wvz[matnr]['Nachname']):
				print("NACHNAME	{}	{}	{}	{}	{}	{}".format(platz, vname, nname, matnr, wvz[matnr]['Vorname'], wvz[matnr]['Nachname']))