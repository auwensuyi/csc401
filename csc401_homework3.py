
sample_data = [
    'Laaibah,208.10,10',
    'Arnold,380.999,9',
    'Sioned,327.01,1',
    'Shayaan,429.50,2',
    'Renee,535.29,4'
]

def print_columns(data):

    print('Name                Cost    Items  Total')
    for words in data:
        word = words.split(",")
        print('{:20}{:6.2f} {:6}  {:6.2f}'.format(words[0:4], float(word[1]), int(word[2]),float(word[1])*int(word[2])))






def scan_for(file_name, word):
    '''print the number of occurences of a target
       word in specified file.'''
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    text = str.maketrans('.!?', 3*' ')
    content = content.translate(text)
    content = content.split()
    
    print(f'The word {word} appears {content.count(word)} times in {file_name}')
    


def calc_tax(in_file_name, out_file_name):
    with open(in_file_name, 'r') as infile, open(out_file_name, 'w') as outfile:
        lines = infile.readlines()
        for line in lines:
            tax_amount ='{:6.2f}'.format((float(line.split()[1]))*(float(line.split()[2])))
            
            
            outfile.write(str(tax_amount)+"\n")
            


# --------------------------------------------
# STOP! Do not change anything below this line
# The code below makes this file 'self-testing'
# --------------------------------------------
def show_file(file_name):
    with open(file_name, 'r') as result_file:
        print(result_file.read())
        
if __name__ == "__main__":
    import doctest
    doctest.testfile('csc401_homework3_test.txt', verbose = True, optionflags=doctest.NORMALIZE_WHITESPACE)

