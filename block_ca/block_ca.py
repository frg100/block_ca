
###### ESSENTIAL DATA ###########
cells_to_config_no = {"0000": 0, "1000" : 1, "0100" : 2, "1100" : 3, "0010" : 4,"1010" : 5,"0110" : 6,"1110" : 7,"0001" : 8,"1001" : 9,"0101" : 10,"1101" : 11,"0011" :12,"1011" :13,"0111": 14,"1111": 15} #Given the cell configuration as the key, has the arbitrary "config number" I assigned
config_no_to_cells = {0: '0000', 1: '1000', 2: '0100', 3: '1100', 4: '0010', 5: '1010', 6: '0110', 7: '1110', 8: '0001', 9: '1001', 10: '0101', 11: '1101', 12: '0011', 13: '1011', 14: '0111', 15: '1111'} #Gives the corresponding cell configuration given the "config number"
###### ESSENTIAL DATA ###########



###### IMPORTING MODULES ########
import numpy as np
from random import randint
from time import sleep
import math
import time
import filecmp
import cProfile
###### IMPORTING MODULES ########


########## FUNCTIONS ############
def rule_list_reversal(forward_rule_list):
    """Reverses the forward rule list for use in the reverse evolution"""
    reverse_rule_list =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in forward_rule_list:
        reverse_rule_list[x] = forward_rule_list.index(x) #reverses the rule_list for use in the reverse evolution
        
    return reverse_rule_list
        
def get_current_config(one, two, three, four):
    """Take in the 4 values as input and decide which of the 16 configurations (0-15) it is"""
    string = str(one) + str(two) + str(three) + str(four)
    return cells_to_config_no[string]

def change_config(current_config,rule_list):
	"""
	Changes the configuration by:
		1. Finding out which config the inputted current_config changes to
		2. Creating a new config string for the new config value
		3. Splitting the string, converting to int, and adding values to values_list
		4. Outputs values_list with the new values
	"""
	changes_to = rule_list[current_config]
	new_config_string = config_no_to_cells[changes_to]
	values_list = []
	for x in new_config_string:
		values_list.append(int(x))
	return values_list
	

def margolus1(rule_list,dish):
    """Does the first part of the evolution, can be customized with the appropiate rule_list for the forward and reverse evollutions"""
    height = len(dish)
    width = len(dish[0])
    for x in range(0,height-2,2):
		for y in (0,width-2,2): #Starts the 2X2 box at 0,0 and then moves onto the next 2X2 box
			square = dish[x:x+2,y:y+2] #Creates a pointer to the 2X2 part of the dish
			#print "Square in Margolus1 = %s" %square
			current_config = get_current_config(square[0,0],square[0,1],square[1,0],square[1,1]) #Gets the current config number
			values = change_config(current_config,rule_list) #Takes the config number and figures out what to change it to based on the rule_list
			square[0,0] = values[0]
			square[0,1] = values[1]
			square[1,0] = values[2]
			square[1,1] = values[3]#Changes the dish to what values it should be based on the rule_list and the current config

def margolus2(rule_list,dish):
    """Does the second part of the evolution, can be customized with the appropiate rule_list for the forward and reverse evollutions"""
    height = len(dish)
    width = len(dish[0])
    for x in range(1,height-2,2):
		for y in range(1,width-2,2): #Starts the 2X2 box at 1,1 (the second pass has a different neighborhood) and then moves onto the next 2X2 box
			square = dish[x:x+2,y:y+2]
			current_config = get_current_config(square[0,0],square[0,1],square[1,0],square[1,1])
			values = change_config(current_config,rule_list)
			square[0,0] = values[0]
			square[0,1] = values[1]
			square[1,0] = values[2]
			square[1,1] = values[3]
			
def forward_evolution(generations, rule_list, dish):
    """Performs the forward evolution of the block cellular automata"""
    
    for x in range(0,generations):
        margolus1(rule_list,dish) #runs margolus 1 and 2 for the specificed number of generations
        margolus2(rule_list,dish)
        
    return dish
    
def reverse_evolution(generations, rule_list, dish):
    """Performs the reverse evolution of the block cellular automata"""
    
    reverse_rule_list = []#initializes the variable
    reverse_rule_list = rule_list_reversal(rule_list)
    
    for x in range(0,generations):
        margolus2(reverse_rule_list,dish)
        margolus1(reverse_rule_list,dish) #runs margolus 1 and 2 for the specificed number of generations
        
    return dish
    
			
def calculate_entropy_of_dish(dish):
    """Calculates the entropy of the dish"""
    bit_string = ""
    for row in dish:
        for cell in row:
            bit_string += str(cell) #creates a continuous string of all the bits in the dish
    byteArr = [int(x, 2) for x in map(''.join, zip(*[iter(bit_string)]*8)) ] #creates a byte array by taking each 8 characters in the bit_string and using int(x,2) to turn the binary string into decimal integers
    
    # calculate the frequency of each byte value in the file
    freqList = []
    fileSize = len(byteArr)
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1#adds one to the frequency of the byte by iterating through each byte in the file
        freqList.append(float(ctr) / fileSize)
    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    return -ent
    
    
def open_file(file_name):
    """Function to open a file and create a dish of all the bits of the file"""
    
    def factors(n):
        """Function to calculate all the factors of a given number n"""
        return sorted( reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)) )
        
    # read the whole file into a byte array
    '''file_name = raw_input("What file would you like to open?: ")'''
    f = open(file_name, "rb")
    print "Opened file %r" %file_name
    byteArr = map(ord, f.read()) #gets byte number from whatever data the file is in
    byteArr = map(lambda x : '{0:08b}'.format(x),byteArr) #takes the byte number and turns it into binary
    f.close()
    factors =  factors(len(byteArr)*8) #gets the factors of the #of bits in the file
    dish_size = [ factors[(len(factors)/2)-1] , factors[(len(factors)/2)] ] #gets the middle two factors (to make the dish as square-like as possible) of a file and uses those as width and height of the file
    height = dish_size[0]
    width = dish_size[1] #makes the dish dimensions equal to the middle factors of the length of the dile
    print "\nDish Height = %s and Dish Width = %s" %(height,width)
    dish = np.zeros((height,width), dtype=np.int) #initializes a dish of all zeros
    bit_sequence = ""
    for row in byteArr:
        for x in row:
            bit_sequence += str(x) #adds the numbers into a bit sequence
    counter = 0
    for x in range(0,len(dish)):
        for y in range(0,len(dish[0])): #iterates through the whole dish
            dish[x,y] = int(bit_sequence[counter]) #goes in order through the whole bit sequence and turns that string into an int to insert to the dish
            counter += 1
    return dish
            
def write_dish_to_file(file_name,dish):
    """Writes the dish back into a file with name = file_name """
    print "\nWriting file %r" %file_name
    bit_sequence = ""
    for row in dish:
        for cell in row:
            bit_sequence += str(cell) #creates a string of all the bits
    byte_list = [bit_sequence[i:i+8] for i in range(0, len(bit_sequence), 8)] #creates a list of strings of binary length 8 bytes
    byte_list = map(lambda x:int(x,2), byte_list) #turns the binary strings into decimal ints
    byte_list = map(chr, byte_list) #turns the ints back to unicode
    
    file = open(file_name,"w") #opens the file
    for i in byte_list:
        file.write(i) #writes the unicode back to file
    print "\nFile written successfully"
########## FUNCTIONS ############