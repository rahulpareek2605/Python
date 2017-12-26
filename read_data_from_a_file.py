from sys import argv

script, input_file = argv

#####################################################
####Function to print all the content of the file####
#####################################################
def print_all(f):
    print f.read()

##########################################################
######Function to move to starting point of the file######
##########################################################	
def rewind(f):
    f.seek(0)
	
##########################################################
######Function to print file data one line at a time######
##########################################################

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

#printing the whole file
print_all(current_file)

#lets rewind the whole file
rewind(current_file)

#printing the three lines

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)













																																													
