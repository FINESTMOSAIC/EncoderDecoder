import base64

class Encoder:
    def ceaser(data,s):
        result = ""
    
        # traverse data
        for i in range(len(data)):
            char = data[i]
    
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
    
        return result

    #base64
    def base64en(data):
        byte_data = data.encode('utf-8')
        encoded_data = base64.b64encode(byte_data)
        return encoded_data


    #ASCII
    def ASCII(data):
        encodeddata=''
        for i in data:
            encodeddata=encodeddata+str(ord(i))
        return encodeddata

    def utf(data,utf_type):
        utf_type='utf-'+utf_type
        str_encoded= data.encode(utf_type,'replace')
        return str_encoded
    
    def encode(Type,string):
        




    