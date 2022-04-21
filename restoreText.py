#input="ilikebooks" // "intheshop" // "ineedashoppingcart" 
#output="i like books"
  
result = ""
prevValidSentence = ""
text = 'ineedashoppingcart'
 
"""
    isValid a function gets a text and validate wether it is found in list of keys or not
"""
def isValid(text):
    keys = ['i','like','books','in','the','shop','need','shopping','cart','a','shop','ping']
    if text in keys:
        return 1
    else:
        return 0
 
"""
    restore is the main function that finds all possible solutions and validate the the correct solution 
"""
def restore(idx, cur_word):
    global prevValidSentence
    global result
 
    #base case when i reach the end  of the input string // complete the solution and stop recursing 
    if(idx >= len(text)):
        if(isValid(cur_word)):
            result = prevValidSentence + " " + cur_word
            
        return
 
    cur_word += text[idx]
 
    if(isValid(cur_word)):
        prevSentence = prevValidSentence
        prevValidSentence = prevValidSentence + " " + cur_word
        #complete the current solution
        restore(idx + 1, "")
 
        prevValidSentence = prevSentence
    
    restore(idx + 1, cur_word)
 
 
 
def main():
    restore(0, "")
    print(result)

if __name__ == "__main__":
    main()