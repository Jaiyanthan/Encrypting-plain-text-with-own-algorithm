import base64

# initial text value to genrate a set of random data
key = "This is a secret key"

# getting the plain text
print("Enter the message to be encrypted")
message = input()

# empty list of encrypted data
encrypt = []

for i in range(len(message)):
    # creating a set of numbers from the text
    key2 = key[i % len(key)]
    # appending the generated randomly jumbled data to the array
    encrypt.append(chr((ord(message[i]) + ord(key2)) % 567))
# encrypted data    
encryption = base64.urlsafe_b64encode("".join(encrypt).encode()).decode()
print(encryption)
 

decrypt = []
# getting the encrypted data
input = input()
message = base64.urlsafe_b64decode(input).decode()
# reversing the process
for i in range(len(message)):
    key2 = key[i % len(key)]
    decrypt.append(chr((567 + ord(message[i]) - ord(key2)) % 567))
# getting the decrypted data    
print("".join(decrypt))
