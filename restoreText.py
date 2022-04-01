#input="ilikebooks" // "intheshop"
#output="i like books"


"""
    isValid a function gets a text and validate wether it is found in our keys or not
"""
def isValid(text):
    keys = ['i','like','books','in','the','shop']
    if text in keys:
        return 1
    else:
        return 0

"""
    restore is the main function that finds all possible keys and the valid key the desired output string
"""
def restore(text):
    output = ""
    next = 0
    for i in range(len(text)):
        #move to the next keyword directly
        if i < next:
            continue
        #define a list to hold a tuple of all found possible keys
        list = [('',0)]

        #get all possible keys from current index
        for j in range(i+1,len(text)+1):
            if isValid(text[i:j]) and text[i:j] not in list:
                list.append((text[i:j],str(j)))

        #add the last and longest found key starting from indext i to the main desired output text
        output = output + list[-1][0] + " "
        next = int(list[-1][1])
                
    return output

def main():
    text = 'ilikebooks'
    print(restore(text))

if __name__ == "__main__":
    main()