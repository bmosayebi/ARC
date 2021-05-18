assembeler_instruction = {'add': '0','sub': '1','multi': '2','xor': '3','move': '4','load': '5','store': '6','jump': '7','halt': '1000'}
register_file={'a': '00','b': '01','c': '10','d': '11'}
register_file_for_with_out_imm = {'a': '0','b': '5','c': 'a','d': 'f'}
result = []
result.append('0000')
t = input()
string_input = []
counter = 0
while t != "halt":
    t = t.split()
    string_input.append(t)
    t = input()
    counter = counter + 1
string_input.append(['halt'])
# for i in string_input:
#     print(i)
def convert_all_instruction_to_hex(item):
    convert_intruction_to_hex = ''
    if item[0] == 'halt':
        result.append('8000')
    elif item[0] == 'jump':
        convert_intruction_to_hex += '70'
        bit_binary_to_hex = hex(int(item[1], 10))
        bit_binary_to_hex = bit_binary_to_hex[2:]
        if len(bit_binary_to_hex) == 1:
            convert_intruction_to_hex += '0'
            convert_intruction_to_hex += bit_binary_to_hex
        else:
            convert_intruction_to_hex += '70'
            convert_intruction_to_hex += bit_binary_to_hex
        result.append(convert_intruction_to_hex)
    else:
        if item[2] == 'a' or item[2] == 'b' or item[2] == 'c' or item[2] == 'd':
            convert_intruction_to_hex += assembeler_instruction[item[0]]
            temp = register_file[item[2]] + register_file[item[1]]
            bit_binary_to_hex = hex(int(temp, 2))
            bit_binary_to_hex = bit_binary_to_hex[2:]
            convert_intruction_to_hex += (bit_binary_to_hex + 'ff')
        else:
            bit_binary_to_hex = hex(int(item[2], 10))
            bit_binary_to_hex = bit_binary_to_hex[2:]
            if len(bit_binary_to_hex) == 1:
                convert_intruction_to_hex += assembeler_instruction[item[0]]
                convert_intruction_to_hex += register_file_for_with_out_imm[item[1]]
                convert_intruction_to_hex += '0'
                convert_intruction_to_hex += bit_binary_to_hex
            else:
                convert_intruction_to_hex += assembeler_instruction[item[0]]
                convert_intruction_to_hex += register_file_for_with_out_imm[item[1]]
                convert_intruction_to_hex += bit_binary_to_hex
        result.append(convert_intruction_to_hex)
for item in string_input:
    convert_all_instruction_to_hex(item)
for i in result:
    print(i,end=' ')


    





