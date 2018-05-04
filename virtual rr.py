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
