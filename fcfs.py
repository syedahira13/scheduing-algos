array=[]

total=[]

total=0

starttime=0

num=int(rawinput('HOW MANY PROCESSES DO YOU WANT TO ENTER: '))



for i in xrange(num):
	array.append([])
	array[i].append(rawinput('NAME THE PROCESS: '))
	array[i].append(int(rawinput('BURST TIME: ')))
	array[i].append(int(rawinput('ARRIVAL TIME: ')))
	
	total.append([])
	total[i].append(int(starttime-array[i][1]))
	starttime=starttime+array[i][2]

array.sort(key=lambda array:array[1])
print 'Process \t  Burst time \t Arrival time \t waiting time'

for i in xrange(num):
	print array[i][0],' \t\t',array[i][2],' \t\t',array[i][1],' \t\t',total[i]

