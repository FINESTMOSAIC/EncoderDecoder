def decoder():
    print("DECODER")
    print("Select the format in which you have to encode:")
    print("\n 1) ASCII \n 2) Caesar Cipher \n 3) Base64 \n 4) UTF-32 \n 5) UTF-16 \n 6) UTF-8")
    ch=input()
    message=input("Enter the encoded text:\n-->")
    if ch=="1":
        print(ASCII(message))
    elif ch=="2":
        S=int(input("Select the shift\n"))
        if S==None:
            S=3

        print(ceaser(message,S))
        
        
    elif ch=="3":
      
        print(base64en(message))

    elif ch=="4":
      
        print(utf32(message))

    elif ch=="5":
      
        print(utf16(message))

    elif ch=="6":
      
        print(utf8(message))
        
    else:
            print("Wrong choice entered!! \n Please try again")
            decoder()



#text
def end_Text():
    print("Encoded text:\n-->",end=" ")



#Caesar Cipher Technique
def ceaser(text,s):
    end_Text()
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

#base64
def base64en(data):
    end_Text()
    byte_data = data.encode('utf-8')
    encoded_data = base64.b64encode(byte_data)
    return encoded_data


#ASCII
def ASCII(string):
    end_Text()
    encodedString=''
    for i in string:
        encodedString=encodedString+str(ord(i))
    return encodedString


def utf32(data):
    end_Text()
    str_encoded= data.decode('utf_32','replace')
    return str_encoded


def utf16(data):
    end_Text()
    str_encoded= data.decode('utf-16','replace')
    return str_encoded

def utf8(data):
    end_Text()
    str_encoded= data.decode('utf-8','replace')
    return str_encoded

