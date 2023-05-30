# person = {
#     'name':'john',
#     'age':23,
#     'school':'cyclobold',
#     'class':'beginner_python'
# }
# sample = open('user.txt', 'w')
# sample.write(str(person)+'\n')
# sample.write('john is a student of cyclobold \n')
# sample.write('he is in the beginner section ')
# sample.write('he is not feeling too well')
# sample.close()
user = input('what is your name?')
store = {}
saved = open('user.txt', 'w')
if(saved.write("username: " + user + '\n')):
    store['name'] = user
    password = input('enter your pin')
    store['password'] = password
    saved.write("password: "+password + "\n")
    saved.write("person = "+str(store))
    print(store)
else:
    print('unable to create a text file')
saved.close()