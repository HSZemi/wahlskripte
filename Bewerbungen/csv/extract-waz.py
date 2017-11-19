import csv


for liste in ('RCDS','JUSOS','LHG','LUST','GHGP','SDS','LISTE','KULT'):
	with open('{}.csv'.format(liste), "r") as f, open('WAZ-{}.csv'.format(liste), "w") as o:
		print(liste)
		reader = csv.DictReader(f, delimiter="\t")
		for line in reader:
			print(line['Listenplatz'])
			print("{0}\t{1} {2}\t{3}".format(line['Listenplatz'], line['Vorname'], line['Nachname'], line['Studienfach']), file=o)