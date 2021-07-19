
def convert_2_km():
    '''
    Prompts user for a value. Using exception handling in case a
    string or float is entered. If certain conditions are met the
    function prints conversions, error message, or returns to exit function.
    '''
    distance = True
    while distance:
            user = input("Miles (or STOP):")
            try:
                miles = float(user)
                if miles < 0:
                    print("Bad input:" + str(miles))
                if miles >= 0:
                    miles = miles*(1.60934)
                    print("Kilometers:" + str(miles))
            except ValueError:
                try:
                    miles = str(user)
                    if miles != 'STOP':
                        print("Bad input:" + str(miles))
                    if miles == 'STOP':
                        return
                except ValueError:
                    return
        
        

def meal_price(items):
    '''
    The items and price of the meal are initialized.
    for loop created to iterate over the list of items.
    If conditions are met then price is added and the total is returned.
    Or else a statement is printed showing an unkown item. 
    '''
    item = []
    price = 0
    for item in items:
        if item == 'apple':
            price += 0.59
        elif item == 'burger':
            price += 2.50
        elif item == 'drink':
            price += 0.99
        elif item == 'fries':
            price += 1.29
        else:
            print('Unknown item: ' + item)

    return price
            
    


def print_change(row):
    '''
    declared a list with no values. iterate over a range of values
    with an accumalating loop that implements the difference between adjacent values.
    the list is unpacked using star and printed.
    '''
    x = []
    for i in range(1, len(row)):
        x.append(row[i] - row[i-1])
    print(*x, sep=",")
    






def sum_nums(a_list):
    '''
    result is the accumulator
    iterate over the specified list.
    checks for integers only and skips over strings
    returns the result of the sum of the list.
    '''
    result = 0
    for x in a_list:
        if type(x) == int:
            result += x
    return result

       
            
    


# --------------------------------------------
# STOP! Do not change anything below this line
# The code below makes this file 'self-testing'
# --------------------------------------------
def show_file(file_name):
    with open(file_name, 'r') as result_file:
        print(result_file.read())
        
if __name__ == "__main__":
    import doctest
    doctest.testfile('csc401_homework4_test.txt', verbose = True, optionflags=doctest.NORMALIZE_WHITESPACE)
