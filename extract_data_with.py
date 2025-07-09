import re
phoneNumberRange=re.compile(r'd/d/d/d/d/d/d/d/d/d/d')
example ="1234567890"
result = phoneNumberRange.search(example)
if result:
    print("Valid phone number found:", result.group())  
    print("Phone number:", result.group())