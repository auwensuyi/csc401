
def process_row(row):
    '''
    Function that parses a string, converts middle element into a float, and returns a tuple. 
    '''
    for string in row:
        row =(row.split(",", 3))
        try:
            if len(row) == 3:
                partone = float(row[1])
        except ValueError:
            partone = "error"
        return (row[0], partone, row[2])
    
    


# This data is not used in any of the code.  It is
# included as a reference.  load_bank_data('customers.csv')
# should produce a dictionary very similar to this one.
bank_map = {
    'Laaibah':  (208.1,   '10/22/2019'), 
    'Arnold':   (380.999, '9/12/2019'), 
    'Sioned':   (327.01,  '1/1/2019'), 
    'Shayaan':  (429.5,   '2/28/2019'), 
    'Renee':    (535.29,  '4/09/2019'), 
    'Conal':    (726.77,  '9/21/2019'), 
    'Katarina': (730.11,  '10/1/2019'), 
    'Theodor':  (637.12,  '10/15/2019'), 
    'Nadia':    (433.33,  '8/29/2019'), 
    'Jia':      ('error', '7/23/2019'), 
    'Sana':     (829.99,  '10/26/2019')
}



def load_bank_data(file_name):
    '''
    Calls the previous function, while reading into csv file that
    was provided. creates, adds results from the previous function
    to the dictionary. the dictionary is returned.
    '''        

    try:
        with open(file_name, mode='r') as infile:
            records = {}
            
            for row in infile:
                data = process_row(row)
                records[data[0]] = data[1:]

                
            return records
        
    except IOError as err:
        return f'File error: {err}'
    except:
        return 'Unknown error'

        
        

        


def sets_exercise():
    '''
    Functions tests whether items belongs to one, the other, or both sets.
    Items are stored in the dictionary using different keys.
    '''
    upstairs = {"beds", "clothes", "toothbrushes","lamps"}
    downstairs = {"couch", "clothes", "chairs","lamps"}

        
    results = {}

    up_only = upstairs - downstairs
    results['up_only'] = up_only

    down_only = downstairs - upstairs
    results['down_only'] = down_only

    both = upstairs & downstairs
    results['both'] = both

    all_items = upstairs | downstairs
    results['all_items'] = all_items

    return results
            
            

    

# --------------------------------------------
# TEST CODE below.  Add all test code in the
# section below.
# --------------------------------------------

if __name__ == "__main__":

    #--- tests for process_row ---
    row = process_row('Laaibah,208.1,10/22/2019')
    row = process_row('Jia,nnn.nnn,7/23/2019')
    assert len(row) == 3, "Should be 3"
    assert process_row('Laaibah,208.1,10/22/2019') == ('Laaibah', 208.1, '10/22/2019'), "Should be ('Laaibah', 208.1, '10/22/2019')"
    assert process_row('Jia,nnn.nnn,7/23/2019') == ('Jia', 'error', '7/23/2019'), "Should be ('Jia', 'error', '7/23/2019')"


    # --- tests for load_bank_data ---
    data = load_bank_data('no such file')
    assert type(data) == str
    

    # --- tests for sets_exercise ---
    results = sets_exercise()
    assert results['up_only'] == {'toothbrushes', 'beds'}
    assert results['down_only'] == {'couch', 'chairs'}
    assert results['both'] == {'clothes', 'lamps'}
    assert results['all_items'] == {'beds', 'clothes', 'toothbrushes', 'lamps', 'couch', 'chairs'}

    
