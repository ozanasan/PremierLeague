import csv



f = open('2000premierleague.csv')

out = csv.writer(open("trial.csv","w"), delimiter=',')

allMatches = csv.reader(f)
matches = list(allMatches)[1:]
teams = []
thisWeekTeams = []
weeks = []
weekPoint = {}
weekPlayed = {}
theWeeks = {}

for row in matches:
	teams.append(row[1])

teams = list(set(teams))

#initialize week 0 (start)
for team in teams:
	weekPoint[team] = 0
	weekPlayed[team] = 0
	theWeeks[(team, 0)] = (0,1)

#adding zero week in weeks
weeks.append(weekPoint)

# this is for printing all weeks into console
def printingWeek(point, played, weekc):
	print "WEEK %d" % weekc
	print "-------"
	ranking = 1
	for element in sorted(weekPoint, key=weekPoint.get, reverse=True):
		#print "%d. %s %d played:%d" % (ranking, element, weekPoint[element], weekPlayed[element])
		theWeeks[(element, weekc)] = (weekPoint[element], ranking)
		ranking =  ranking + 1 
		


# this calculates the week given
def weekCalculations(week):
	for match in matches[10*week - 10 : 10*week]:
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
	printingWeek(weekPoint, weekPlayed, week)
	


for i in range(1, 39):
	print "          "
	weekCalculations(i)

print theWeeks['Bradford', 5]
print theWeeks['Bradford', 25]

	

count = 10
week = 1
for row in matches:
	count = count + 1
	if(week < 38):
		week = count/10 
	result = row[3]
	home = int(result[0])
	away = int(result[2])
	
	if home > away:
		result = 1
	elif home < away:
		result = 2
	elif home == away:
		result = 0

	data = [week, theWeeks[(row[1], week-1)][0], theWeeks[(row[1], week-1)][1], theWeeks[(row[2], week-1)][0], theWeeks[(row[2], week-1)][1], result]
	out.writerow(data)
	

#print weeks

#weeks = sorted(weeks, key=weeks.get, reverse=True)
#print weeks
#print weekPoint['Bradford']

#
#r i in range(1,4)]
#