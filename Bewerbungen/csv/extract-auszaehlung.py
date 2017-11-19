import csv

nr = 0
for liste in ('RCDS','JUSOS','LHG','LUST','LISTE','KULT','GHGP','SDS'):
	with open('{}.csv'.format(liste), "r") as f:
		nr += 1
		print('<liste kuerzel="{short}" name="FOO" nummer="{nr}">'.format(short=liste, nr=nr))
		reader = csv.DictReader(f, delimiter="\t")
		print('<kandidaten>')
		for line in reader:
			print('<kandidat name="{vorname} {nachname}" nummer="{nr}"/>'.format(nr=line['Listenplatz'], vorname=line['Vorname'], nachname=line['Nachname']))
		print('</kandidaten>')
		print('</liste>')