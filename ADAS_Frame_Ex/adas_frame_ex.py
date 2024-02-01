
f = open("ADAS_Frame_Ex_input.txt", "r")
frame=f.readline()
f.close()
split_frame = frame.split()

def create_pdu_dict():
    
    pdu_list = []
    payload_list = []
    payload = []
    pdu = []
    index = 0
    counter = 0

    while len(pdu_list) <= 2:
        stop_bytes = split_frame[counter]
        header_bytes = split_frame[counter+1]+' '+split_frame[counter+2]
        dlc_bytes = split_frame[counter+3]
        pdu = stop_bytes+' '+header_bytes+' '+dlc_bytes+' '
        counter = counter+4
        for dlc_byte in range(0, int(dlc_bytes)):
            payload.insert(dlc_byte, split_frame[counter])
            counter += 1
        payload_list.insert(index, payload)
        pdu_list.insert(index, pdu)
        index += 1
        payload = []
        pdu = []
    pdu_dict = dict(zip(pdu_list, payload_list))
    return pdu_dict, counter


def create_input_dict():
    
    input_dict = {}
    with open('ADAS_Frame_Ex_input.txt', 'r') as file:
        index = 1
        next(file)
        for line in file:
            parts = line.split()
            if len(parts) >= 1:
                values = [int(value) for value in parts]
                input_dict[index] = values
                index += 1
    return input_dict

def create_new_frame():

    input_dict = create_input_dict()
    pdu_dict, counter = create_pdu_dict()

    index = 1
    new_frame = ''
    for pdu in pdu_dict:
        byte_pos = input_dict[index][0]
        bit_pos = input_dict[index][1]
        size = input_dict[index][2]
        value = input_dict[index][3]
        index += 1
        new_payload = modify_payload(
            pdu_dict[pdu], byte_pos, bit_pos, size, value)
        new_frame = new_frame+' ' + pdu + ' '+new_payload

    unused_frame = split_frame[counter:]
    unused_frame_string = ' '.join(unused_frame)
    new_frame += unused_frame_string
    return new_frame


def modify_payload(pdu, byte_pos, bit_pos, size, value):

    bin_list = hex_to_bin(pdu)
    start_index = abs(7 - bit_pos)
    value_to_be_transformed = bin(value)[2:]
    new_binary_value = bin_list[byte_pos][:start_index] + \
        value_to_be_transformed + bin_list[byte_pos][start_index+size:]
    bin_list[byte_pos] = new_binary_value
    hex_value = bin_to_hex(bin_list)
    new_payload = ' '.join(hex_value)
    return new_payload


def hex_to_bin(seq):
    
    bin_list = []
    index = 0
    scale = 16
    num_of_bits = 8
    for i_byte in seq:
        value_in_binary = (bin(int(i_byte, scale))[2:].zfill(num_of_bits))
        bin_list.insert(index, value_in_binary)
        index += 1
    return bin_list

def bin_to_hex(binary_seq): 
    
    hex_list = [hex(int(binary_value, 2))[2:].zfill(2)
                for binary_value in binary_seq]
    return hex_list

def main():

    new_frame=create_new_frame()
    f = open("ADAS_Frame_Ex_output.txt", "w")
    f.write("new frame:")
    f.write(new_frame)
    print("DONE !")

if __name__ == "__main__":
    main()
