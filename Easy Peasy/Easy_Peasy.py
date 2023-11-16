from pwn import *

KEY_LEN = 50000

r=remote("mercury.picoctf.net",20266)
r.recvuntil("This is the encrypted flag!\n")

hex_flag_encrypted=r.recvline()
print("hex enc flag : " ,hex_flag_encrypted) 

# AS the flag file contain text ascci when it will be opened it's return will be in byte format(ascii caractere)
#  
# AS we see also the result of each encrypted caracter is return in to it's hexadicimal format into tow bytes => so the the flag and the encrypted flag are at same length

byte_string = bytes.fromhex(str(hex_flag_encrypted, encoding='utf-8')) 
flag_encrypted = byte_string.decode("ASCII")  
print(" enc flag : " ,flag_encrypted) 
len_flag=len(flag_encrypted)

# According to this instruction (flow because made the decryption possible of n pad every 50000 encrypted text) "stop = stop % KEY_LEN" stop will be 0 if the previous stop variable is 50000. 

reste_to_rest_key=KEY_LEN-len_flag
r.sendlineafter("What data would you like to encrypt? ", "A" * reste_to_rest_key)
unuseful_data=r.recv()
print("unusful : ", unuseful_data) 


msg_to_send="A" * len_flag
r.sendlineafter("What data would you like to encrypt? ", msg_to_send)
r.recvline()
hex_data_encrypted=r.recvline()
print("The encrypted sent data in format byte hex is :  ", hex_data_encrypted)
byte_string = bytes.fromhex(str(hex_data_encrypted, encoding='utf-8')) 
encrepted_data = byte_string.decode("ASCII")  
print("The encrypted sent data is :  ", encrepted_data)


key_list = list(map(lambda p, k: ord(p) ^ ord(k), [x for x in encrepted_data],  [y for y in msg_to_send] ))
print("The key of the encryption in code ascii code equivalent is :  ", key_list)

# As we now xor is associative and transitive means that "enc_flag ⊕ flag = key" so enc_A  ⊕  A = key
list_flag_encrypted=list(e for e in flag_encrypted)
flag = list(map(lambda p, k: "{:02x}".format(p ^ ord(k)), key_list,  [y for y in flag_encrypted] ))

print ( "The falg is in format str byte : {}".format(unhex("".join(flag))))


