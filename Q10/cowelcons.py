filename = input("Enter file name: ")

try:
    infile = open(filename, "r")
    text = infile.read()
    infile.close()
    
    vowels = set("AEIOUaeiou")
    cons = set("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz")

    countv = 0
    countc = 0
    for char in text:
        if char.lower() in vowels:
            countv += 1
        elif char.lower() in cons:
            countc += 1

    print("The number of vowels is", countv)
    print("The number of consonants is", countc)

except FileNotFoundError:
    print("File not found or cannot be opened.")
