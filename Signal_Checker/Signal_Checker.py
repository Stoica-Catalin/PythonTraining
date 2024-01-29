hexa_sequence='60 20 45 6C FE 3D 4B AA'
#hexa_sequence='40 12 6C AF 05 78 4A 04'
bytes=[0,1,2,3,4,5,6,7]
binary=[]
index=0
scale = 16
num_of_bits = 8

bytes_sequence=hexa_sequence.split()
for i_byte in bytes_sequence:   
    value_in_binary=(bin(int(i_byte, scale))[2:].zfill(num_of_bits)) 
    binary.insert(index,value_in_binary)
    index+=1
    
map_of_bytes = dict(zip(bytes, binary))
print(map_of_bytes)

def signal_check(byte_pos, bit_pos, size):
    searched_byte=map_of_bytes[byte_pos]
    searched_seq=''
    start_index=abs(7 - bit_pos)
    for i in range(0 , size):
        searched_seq=searched_seq + searched_byte[i + start_index]        
    print("Signal searched: "+searched_seq)

# PassengerSeatMemoRequest
signal_check(0,7,3)

#ClimFPrightBlowingRequest
signal_check(5,7,4)

#TimeFormatDisplay
signal_check(5,3,1)
