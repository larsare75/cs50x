import validator_collection

inputstreng=input("What's your email address?")

if (validator_collection.is_email(inputstreng)):
    print("Valid")
else:
    print("Invalid")