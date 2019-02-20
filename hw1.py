import pylab as pl

def words(data,x = 26):

	words = {}
	result = []
	ite = 0

	for line in data:
		
		words_list = line[1:-1].split(" ")
		words_set = set(words_list)
		for word in words_set:
			try:
				words[word] += 1
			except:
				words[word] = 1
		ite += 1

	for w in words.keys():
		if words[w] >= x:
			result.append(w)

	return result

def feature_vector(email,words):
	
	result = []
	email_list = email.split(" ")
	email_set = set(email_list)
	for i in range(len(words)):
		if words[i] in email_set:
			result.append(1)
		else:
			result.append(0)

	return result

def perceptron_train(data, words):
	
	w = []
	for i in range(len(words)):
		w.append(0)
	
	k = 0
	iteration = 0
	error = -1
	features = []
	result = []
	for line in data:
		result.append(int(line[0]))
		features.append(feature_vector(line[1:-1],words))
	while (error != 0 and iteration < 25):

		error = 0
		for i in range (len(result)):

			y_train = 0
			for j in range(len(w)):
				y_train += w[j]*features[i][j]
			if result[i] == 1:
				y = 1
			else:
				y = -1
			if y * y_train <= 0:
				for j in range(len(w)):
					w[j] += y * features[i][j]
				error += 1

		k += error
		iteration += 1
		#print(error,iteration)

	return w,k,iteration

def perceptron_error(w,data,words):

	total_email = 0
	error_email = 0
	ite = 0
	for line in data:

		result = int(line[0])
		if result == 1:
			true = 1
		else:
			true = -1
		feature = feature_vector(line[1:-1],words)
		train = 0
		for i in range(len(w)):
			train += w[i] * feature[i]
		if true * train <= 0:
			error_email += 1
		total_email += 1
		ite += 1

	return error_email / total_email 


if __name__=="__main__":

	train = open("train.txt","r")
	word_list = words(train)
	word_list.remove(word_list[0])
	print(len(word_list))
	train = open("train.txt","r")
	w,k,iteration = perceptron_train(train, word_list)
	valid = open("valid.txt","r")
	validate_error = perceptron_error(w, valid, word_list)
	print("for 4000 training samples")
	print(validate_error,iteration)

	positive_words = []
	negative_words = []
	word_copy = word_list[:]
	weight_copy = w[:]
	for i in range(12):
		max = -9999
		index = -1
		for j in range(len(word_copy)):
			if weight_copy[j] > max:
				index = j
				max = weight_copy[j]
		positive_words.append(word_copy[index])
		word_copy.remove(word_copy[index])
		weight_copy.remove(weight_copy[index])
	word_copy = word_list[:]
	weight_copy = w[:]
	for i in range(12):
		min = 9999
		index = -1
		for j in range(len(word_copy)):
			if weight_copy[j] < min:
				index = j
				min = weight_copy[j]
		negative_words.append(word_copy[index])
		word_copy.remove(word_copy[index])
		weight_copy.remove(weight_copy[index])

	print(positive_words)
	print(negative_words)

	test = open("spam_test.txt","r")
	print("test result")
	print(perceptron_error(w, test, word_list))

	train_200 = open("train_200.txt","r")
	w,k,iteration = perceptron_train(train_200,word_list)
	valid = open("valid.txt","r")
	validate_error = perceptron_error(w, valid, word_list)
	print("for 200 training samples")
	print(validate_error,iteration)

	train_600 = open("train_600.txt","r")
	w,k,iteration = perceptron_train(train_600,word_list)
	valid = open("valid.txt","r")
	validate_error = perceptron_error(w, valid, word_list)
	print("for 600 training samples")
	print(validate_error,iteration)

	train_1200 = open("train_1200.txt","r")
	w,k,iteration = perceptron_train(train_1200,word_list)
	valid = open("valid.txt","r")
	validate_error = perceptron_error(w, valid, word_list)
	print("for 1200 training samples")
	print(validate_error,iteration)

	train_2400 = open("train_2400.txt","r")
	w,k,iteration = perceptron_train(train_2400,word_list)
	valid = open("valid.txt","r")
	validate_error = perceptron_error(w, valid, word_list)
	print("for 2400 training samples")
	print(validate_error,iteration)

	input_file=open("spam_train.txt","r")
	word_list = words(input_file)
	input_file=open("spam_train.txt","r")
	w,k,iteration = perceptron_train(input_file, word_list)
	test_file=open("spam_test.txt","r")
	error_rate = perceptron_error(w,test_file,word_list)
	print("using 5000 training samles")
	print(error_rate,iteration)




