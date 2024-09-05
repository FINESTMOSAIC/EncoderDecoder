import Encoder
import Decoder

def ch():
    print(''' Greetings\nPlease select\n1 for Encoding the message and\n2 for Decoding the message ''')
    Choice=input()
    if Choice == "1":
        Encoder.encoder()
    
    elif Choice =="2":
        Decoder.decoder()
    else:
        print("Wrong choice entered!! \n Please try again")
        ch()


try:
    
    ch()

except:
    print("An error occured")


