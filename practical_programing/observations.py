observations_file = open('observations.txt')
bird_counts = []
for line in observations_file:
	bird = line.strip()
	found = False
	# find bird in the list of bird counts
	for entry in bird_counts:
		if entry[0] == bird:
			entry[1] +=1
			found = True
	if not found:
		bird_counts.append([bird,1])


observations_file.close()
print(bird_counts)