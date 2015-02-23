import csv

f = open('2000premierleague.csv')

allMatches = csv.reader(f)
matches = list(allMatches)[1:]
teams = []
thisWeekTeams = []
weeks = []
weekPoint = {}
weekPlayed = {}

for row in matches:
	teams.append(row[1])

teams = list(set(teams))

#initialize week 0 (start)
for team in teams:
	weekPoint[team] = 0
	weekPlayed[team] = 0

#adding zero week in weeks
weeks.append(weekPoint)

# this is for printing all weeks into console
def printingWeek(point, played):
	print " "
	print "WEEK"
	ranking = 1
	for element in sorted(weekPoint, key=weekPoint.get, reverse=True):
		print "%d. %s %d played:%d" % (ranking, element, weekPoint[element], weekPlayed[element])
		ranking =  ranking + 1 

# this calculates the week given
def weekCalculations(week):
	print "WEEK %d " % week
	print "--------"
	for match in matches[10*i - 10 : 10*i]:
		result = match[3]
		home = int(result[0])
		away = int(result[2])

		weekPlayed[match[1]] = weekPlayed[match[1]] + 1
		weekPlayed[match[2]] = weekPlayed[match[2]] + 1
	
		if home > away:
			weekPoint[match[1]] = 3 + weekPoint[match[1]]
		elif home < away:
			weekPoint[match[2]] = 3 + weekPoint[match[2]]
		elif home == away:
			weekPoint[match[1]] = 1 + weekPoint[match[1]]
			weekPoint[match[2]] = 1 + weekPoint[match[2]]
	weeks.append(weekPoint)
	printingWeek(weekPoint, weekPlayed)


for i in range(1, 39):
	print "          "
	weekCalculations(i)








