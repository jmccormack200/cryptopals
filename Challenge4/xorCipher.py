import binascii, sys

keywords = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']


def inc_key(key):
	int_key = int(key, 16)
	int_key = int_key + 1
	hex_key = hex(int_key)[2:] #removes the 0x
	return hex_key

def decrypt(data, key):
	xor = lambda x,y :int(x, 16)^int(y,16)
	ans = ""
	for temp in [data[a:a+2] for a in range(0, len(data)-2,2)]:
		ans = ans + chr(xor(temp, key))
	
	return ans

def body(data):

	key = "00"

	for a in range(0,255):
		ans = decrypt(data, key)
		for word in keywords:
			word = " " + word + " "
			if word in ans or word + " " in ans or " " + word in ans or " " + word + " " in ans:
				print "[*]Encrypted data: " + data
				print "[*]Decrypted data: " + ans
				print "[*]key : 0x" + (key)
				break
		key=inc_key(key)



	
	


if __name__ == "__main__":
	file = open('4.txt', 'r')
	for line in file:
		body(line)
