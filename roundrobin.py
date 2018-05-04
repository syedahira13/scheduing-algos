array=[]

totall=[]

finish=[]

rburst=[]

total=0


quantum=int (rawinput('TIME QUANTUM: '))
num=int(rawinput('HOW MANY PROCESSES DO YOU WANT TO ENTER: '))



for i in xrange(num):
	array.append([])
	array[i].append(rawinput('NAME THE PROCESS: '))
	array[i].append(int(rawinput('ARRIVAL TIME ')))
	array[i].append(int(rawinput('BURST TIME ')))
	array[i].append(array[i][2]) #remaining burst time
	total+=array[i][2] #total bt
	array[i].append(0) #ft


x=0
current=array[x][1]
while total>0:
	if array[x][3]<quantum and array[x][3]!=0 and array[x][1]<=current:
		total=total-array[x][3]
		current=current+array[x][3]
		array[x][4]=current
		array[x][3]=0
	elif array[x][3]==0:
		array[x][4]=current
	if (x+1)<num:
		x=x+1
	else:
		x=0

print 'Process \t Arrival time \t Burst time \t waiting time'

for i in xrange(num):
	print array[i][0],' \t\t',array[i][1],' \t\t',array[i][2],' \t\t',array[i][4]-array[i][1]-array[i][2]
