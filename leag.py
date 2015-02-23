import csv

f = open('2000premierleague.csv')
allMatches = csv.reader(f)

#print list(allMatches)[0]

matches = list(allMatches)[1:]

teams = []

for row in matches:
	teams.append(row[1])

teams = set(teams)

weeks = []
weekTemp = {}

for team in teams:
	weekTemp[team] = 0
weeks.append(weekTemp)

for match in matches[0:10]:
	result = match[3]
	home = int(result[0])
	away = int(result[2])
	if home > away:
		weekTemp[match[1]] += 3
	elif home < away:
		weekTemp[match[2]] += 3
	elif home == away:
		weekTemp[match[1]] += 1
		weekTemp[match[2]] += 1

ranking = 1
for element in sorted(weekTemp, key=weekTemp.get, reverse=True):
	print "%d. %s %d" % (ranking, element, weekTemp[element])
	ranking =  ranking + 1 




