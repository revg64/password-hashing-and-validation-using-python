import bcrypt

pass_word=b"mypassword" #bytes
#adding salt also
hased=bcrypt.hashpw(pass_word, bcrypt.gensalt()) #it accepts only bytes
print(hased)
entered_pass=input("Enter password to login ")
entered_pass=bytes(entered_pass,encoding='utf-8')

if bcrypt.checkpw(entered_pass,hased):   # return True or False
    print("Login succesfull")
else:
    print("wrong password")