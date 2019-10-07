# -*- coding: utf-8 -*-
#==============================================================================
#title           :json_diffs.py
#description     :This script compares each object of two JSON files
#author          :Patrick Alves (cpatrickalves@gmail.com)
#creation date   :10-07-2019
#python_version  :3.7
#==============================================================================

import json
import sys
 
# The main function
def compare_object(j1,j2):
    ''' Compares two JSON objects

    Parameters
    ----------
    j1, j2 : JSON objects
    
    
    Returns
    -------    
    bool
        Indicates whether j1 and j2 are equal
    '''
    
    if type(j1) != type (j2):
        print(f"The object type of {j1} and {j2} is different")
        return False
    
    elif type(j1) is dict:      
        return compare_dict(j1,j2)   
    
    elif type(j1) is list:
        return compare_list(j1,j2)
    
    else:      
        return j1 == j2
 

def compare_dict(d1,d2):
    ''' Compares each key and value in input dictionaries

    Parameters
    ----------
    d1, d2 : Input dictionaries
    
    
    Returns
    -------    
    are_equal : bool
        Indicates whether d1 and d2 are equal
    '''
    
    # Default value
    are_equal = True
    
    # Compare the lenghts
    if len(d1) != len(d2):      
        print(f"The lenghts of {d1} and {d2} are different")
        return False
        
    else:
        # Compare the keys and values
        for k,v in d1.items():            
            if not k in d2:
                print(f"The key {k} was not found in {d2}")
                return False                     
            else:
                # Compare the objects
                if not compare_object(v, d2[k]):
                    # Print only values
                    if type(v) is not dict:
                        if type(v) is list and type(v[0]) is dict:
                            pass
                        else:
                            print(f"The values in object {k} are different: {v} != {d2[k]}")
                        
                    are_equal = False
                    
    return are_equal



def compare_list(l1,l2):
    ''' Compares two lists

    Parameters
    ----------
    l1, l2 : Input lists
    
    
    Returns
    -------    
    are_equal : bool
        Indicates whether l1 and l2 are equal
    '''
    
    # Default value
    are_equal = True
    
    # Compare the lenghts
    if len(l1) != len(l2):
        print(f"The lenghts of {l1} and {l2} are different")
        return False
    
    else:
        # Compare each element/object of the list
        for i in range(len(l1)):         
            if not compare_object(l1[i], l2[i]):            
                are_equal = False   
            
    return are_equal
 
    
def main():
    
    # Json files
    json_f1 = None
    json_f2 = None

    # Each if there are input files in arguments
    if len(sys.argv) < 3:
        print(f"Error: Two input files required")
        print(f"<usage>: python json_diffs.py file01.json file02.json")
        sys.exit()
    
    # Try to load the files
    try:        
        with open(sys.argv[1]) as json_file:
            json_f1 = json.load(json_file)        
        with open(sys.argv[2]) as json_file:
            json_f2 = json.load(json_file)
        
    except Exception as exc:        
        print(str(exc))
        sys.exit()    
    
    result = compare_object(json_f1, json_f2)
    
    if result:
        print("The data in JSON files are equal")
    else:
        print("The data in JSON files are different")
    

# Running the script
if __name__ == "__main__":
    main()