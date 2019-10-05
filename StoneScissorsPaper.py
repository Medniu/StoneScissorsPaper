import hmac
import sys
import random
import secrets
import binascii
import math

amount_of_obj=sys.argv[1:]
print(amount_of_obj)
#Tests
logic=True
if (len(amount_of_obj))<3:
    logic=False
    print("Too few objects for game, unput another amount ")
    raise ValueError()

if (len(amount_of_obj))%2==0:
    logic=False
    print("Amount of object is even, try again with non-even amount")
    raise ValueError()

if (len(set(amount_of_obj)))!= len(amount_of_obj):     
    logic=False
    print("Remove duplicate object(s) and try again")
    raise ValueError()

#Generate the key , show Hmac and computer choice
key= secrets.token_hex(16)
computer = random.randint(0,len(amount_of_obj)-1)
print("Now you can write the HMAC, later we will give you the key to check that Computer dont lie")
proof = hmac.new(binascii.unhexlify(key),amount_of_obj[computer].encode('utf-8'),'sha256')  
digest = proof.hexdigest() 
print(digest) 
#Your turn
print("Computer make choice, now you should to make your own")
i=1
while((i<len(amount_of_obj)+1)):
    print(str(i)+")"+(amount_of_obj[i-1]))
    i=i+1
print("0)Exit")
choice=int(input())
#computer or human
half=(len(amount_of_obj) / 2)
if(choice==0):
    sys.exit()
if((computer+1)==choice):
    print("Draw")
elif ((computer+1)+half>len(amount_of_obj) and ((computer+1) + half) % len(amount_of_obj)>=choice) or ((computer+1)+half <= len(amount_of_obj) and (computer+1)+half >= choice and choice>=(computer+1)):

        print("Computer win")
else:
        print("You win, Gratz!")    
    
if choice<1 and choice>(len(amount_of_obj)):
    print("Try again")
    raise ValueError()
print("Your choice is:" + amount_of_obj[choice-1] )
print("Computer choice is: " + amount_of_obj[computer])

#The key for proof
print("Secret key for checking : " + key)