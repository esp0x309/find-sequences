import string

# Find specific sequences of lower and upper characters in text.
# Key is combinacion of lower and upper characters who are found in text.
# Ex. we have text= "HEllo WOrld!" and key= "ZZz"
#     The combination found is: HEl WOr
# Notice! key: ZZz == AAa == BBb == CDe == JLi etc.

i = j = k = 0  

text = "HEllo WOrld" # element of text in i
key  = "AAa" # element of key in j

found = "" # here is found key (sequences) in text

print("In the text: {}".format(text))
print("we are looking for a sequence: {}".format(key))
print("Founded: ", end = "")

for x in range(i, len(text)):
    k = i 

    for j in key: # we compare every char (k) in text with char (j) in key 
        if (text[k].islower() and j.islower() or
            text[k].isupper() and j.isupper()):
            found += text[k] # if the same then we append him to "found"

            if (len(key) == len(found)): # when we found all sequences we print it
                print(found, end = " ")
                break

        else: # if the char is different that we clear "found" and break
            found = ""
            break
    
        if (k < len(text)-1): # increase k - get to next char
            k += 1
        else:
            break

    if (i < len(text)):
        i += 1
    else:
        break 





