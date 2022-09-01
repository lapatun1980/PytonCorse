alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
yes="yes"
#DECRIP---------------------------
def encrypt(etext):
   for j in range(len_text_list):
     for i in range(26):
        if text_list[j]==alphabet[i]:
            if (i+shift)<26:
                text_list[j]=alphabet[i+shift]
                break
            else:                          
                text_list[j]=alphabet[i+shift-26]
                break
#ENCRIPT--------------------------------
def decryption(text):
   for j in range(len_text_list):
     for i in range(26):
        if text_list[j]==alphabet[i]:
            if (i+shift)<26:
                text_list[j]=alphabet[i-shift]
                break
            else:                          
                text_list[j]=alphabet[i-shift-26]
                break
#end defs------
    
while (yes=="yes"):
    direction=input("Type 'encode' for encoding or type 'dencode' for dencoding ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    text_list=list(text)
    len_text_list=len(text_list) 
    
    if direction=="encode":
        encrypt(text)
    else:
        decryption(text)
    # Printing result
    result=""
    for i in text_list:
        result+=i
    print(result)   
    yes=input("If you whant do repiat tape 'yes', if no 'no'").lower()