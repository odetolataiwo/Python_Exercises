#(Regular expression are used for specifying text patterns)

import re  #import regular expressions

#this is to check if phone numbers exits in a block of text.

#block of text
message = 'call me 415-533-5353 tomorrow, or at 412-555-4332'

#\d is the regex for a numeric digit character
#phone number pattern (ddd-ddd-dddd)
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 


num = phoneNumber.search(message) #this searches for the first phone number
numAll = phoneNumber.findall(message) #this searches all occurences of the phone number pattern

print(num)
print(num.group()) #the group object tells you the actual text
print(numAll)


#we can also mark out groups using RE
#let's take out the area code from the phone number. That's the first 3 digits

phoneGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

num2 = phoneGroup.search(message)
print(num2.group())  # or num2.group()
print(num2.group(1)) 
num2.group(2)






#looking for all possible suffixes
BatRegex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = BatRegex.search('Batmobile lost a wheel by Batman')

print(mo.group())

mo1 = BatRegex.findall('Batmobile lost a wheel by Batman')
print(mo1)











