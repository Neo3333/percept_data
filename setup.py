if __name__=="__main__":

	file = open("spam_train.txt","r")
	content = []
	for line in file:
		content.append(line)
	file.close()
	file_train = open("train.txt","w")
	file_train_200 = open("train_200.txt","w")
	file_train_600 = open("train_600.txt","w")
	file_train_1200 = open("train_1200.txt","w")
	file_train_2400 = open("train_2400.txt","w")
	file_validation = open("valid.txt","w")

	for i in range(1000):
		'''
		if i == 1107:
			print (content[i])
		else:
			file_train.write(content[i])
		'''
		file_validation.write(content[i])

	for i in range(1000,5000):
		if i == 4184 or i == 4682 or i == 1107:
			continue
		file_train.write(content[i])

	for i in range(1000,1200):
		if i == 1107:
			continue
		file_train_200.write(content[i])

	for i in range(1000,1600):
		if i == 1107:
			continue
		file_train_600.write(content[i])

	for i in range(1000,2200):
		if i == 1107:
			continue
		file_train_1200.write(content[i])
		
	for i in range(1000,3400):
		if i == 1107:
			continue
		file_train_2400.write(content[i])
		
	file_train.close()
	file_validation.close()
	file_train_200.close()
	file_train_600.close()
	file_train_1200.close()
	file_train_2400.close()