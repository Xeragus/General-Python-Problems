def caesar_encryption(message, shift_string):
	
	# the array in which we will store the encrypted letters
	encrypted_message = [] 

	shift = int(shift_string)

	# two sets of letters
	lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	
	for letter in message:
		if letter in lowercase_letters:
			# the index position in the original message
			original_index = lowercase_letters.index(letter)
			# creating the encrypted index
			encrypted_index = (original_index + shift) % 26
			# getting the encrypted letter from the lowercase array
			encrypted_letter = lowercase_letters[encrypted_index]
			#filling the encrypted message with encrypted letters
			encrypted_message.append(encrypted_letter)
		elif letter in uppercase_letters:
			# the index position in the original message
			original_index = uppercase_letters.index(letter)
			# creating the encrypted index
			encrypted_index = (original_index + shift) % 26
			# getting the encrypted letter from the uppercase array
			encrypted_letter = uppercase_letters[encrypted_index]
			#filling the encrypted message with encrypted letters
			encrypted_message.append(encrypted_letter)
		else:
			encrypted_message.append("***")

	# return the encrypted message
	return encrypted_message

message = input("Enter the message you would like to encrypt: ")
shift = input("Enter the Caesar shift: ")
print(caesar_encryption(message, shift))