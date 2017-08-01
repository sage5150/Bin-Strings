""" This program detects any strings in a binary
Version 0.1 July 22 2017"""
import sys, string

def options():
    # This function will pars
    print("Test")

def help():
    print("This will print a help message\n")
    sys.exit()


def openfile(name):

    #try: # This simply trys to open and read the file
    fd = open(name, "rb")
    data = fd.read().decode("utf-8", "ignore")
    fd.close()
    #except:
        #print("There was an error opening that file\n")
        #sys.exit()

    findstrings(data)


def findstrings(thedata):
    count = 0 # This keeps track of consecutive printable characters
    charslist = [] # Place to keep characters
    printable = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/\.,1234567890!@#$%^&*(){}[]"
    for character in thedata:
        if character in printable:
            charslist.append(character)
            count += 1
        else:
            if count >= 4:
                print(''.join(charslist[-count:]))
                count = 0
    if count >= 4:
        print(''.join(charslist[-count:]))
        
        
                
        
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage = " + sys.argv[0] + " filename\n")
        sys.exit()
        print("Test\n")
    if sys.argv[1] == '-h':
        help()
    filename = sys.argv[1]
    print(filename)
    openfile(filename)
