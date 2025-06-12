get_letter, keyword = 0, []


f = open('messages/Messaggio 2.txt')
text = f.read().strip().lower()

alphabet = "".join(    
    sorted(set(
        list(text)
    ))
)

alpha_len = len(alphabet)
keys = [i for i in range(1, 27)]

print(keys)

for key in keys:

    result = ""
    for i in range(len(text)):
        char = text[i]

            
        result += chr((ord(char) - key - 65) % 26 + 65)
    
    
    print(f"{key}: {result} \n")
    result = ""
