logfile = [line.split(',') for line in open('logfile.txt')]
hour_and_min = []

#splitting the hour and minutes
for i in range(len(logfile)):
    hour_and_min.append(logfile[i][1].split(':'))
    hour_and_min.append(logfile[i][2].split(':'))


hm_joined = []
#Joining the hour and minutes together
for i in range(len(hour_and_min)):
    hm = str(hour_and_min[i][0]) + str(hour_and_min[i][1])
    hm_joined.append(hm)

all_time_spent = []
#Finding the time spent by each individual
j = 0
while j < 10:
    time_spent = int(hm_joined[j+1]) - int(hm_joined[j]) 
    all_time_spent.append(time_spent)
    j += 2

#Calculating those online for at least an hour
for k in range(len(all_time_spent)):
    if int(all_time_spent[k]) - 40 >= 60:
        print(logfile[k][0], "was online for at least an hour")
    else:
        continue


