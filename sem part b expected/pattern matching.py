#pattern matching
str_input = input("Enter string: ")
pattern = input("Enter pattern: ")

if pattern in str_input:
    print("pattern found at index: ",str_input.index(pattern))
else:
    print("pattern not found")
