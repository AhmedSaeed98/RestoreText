#input="ilikebooks" // "intheshop"
#output="i like books"


"""
    is valid function to validate if input parameter is a valid key or not
"""
def isValid(text):
    keys = ['i','like','books','in','the','shop']
    if text in keys:
        return 1
    else:
        return 0

def restore(text):
    output = ""
    next = 0
    for i in range(len(text)):
        if i < next:
            continue
        list = [('',0)]
        #get all possible keys from current index
        for j in range(i+1,len(text)+1):
            if isValid(text[i:j]) and text[i:j] not in list:
                list.append((text[i:j],str(j)))
        output = output + list[-1][0] + " "
        next = int(list[-1][1])
                
    return output

def main():
    text = 'ilikebooks'
    print(restore(text))

if __name__ == "__main__":
    main()