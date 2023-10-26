def create_dictionary():
    dictionary = {}
    n = int(input("Enter the number of key-value pairs: "))
    
    for i in range(n):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dictionary[key] = value
    return dictionary

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = create_dictionary()
dict2 = create_dictionary()

merged_dict = merge_dictionaries(dict1, dict2)

print("\nFirst Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict) 





    


    
        



        
    
