#5-8
names=['Tom',"jaden",'ADMIN','WILLIAM','li hua']
#names2=names[:]
if names:
    for name in names:
        if name.lower() == 'admin':
            print('Hello admin,would you like to see a status report?')
        else:
            print(f"Hello {name.title()},thank you for logging in again")

        #names2.remove(name)
        names.remove(name)
        #print(names2)
    #names=[]
    print("")
elif names:
    print("We need to find some users!")


names=['Tom','Jadon','ADMIN','William','Li hua']
print(len(names))
print(list(range(0,len(names))))
if names:
    for x in list(range(0, len(names))):
        print(x)
        if names[x] == 'admin':
            print('Hello admin,would you like to see a status report?')
        else:
            print(f"Hello {names[x].title()},thank you for logging in again")

        print(names)
else:
    print("We need to find some users!")



#5-9
names=[]
if names:
    for name in names:
        if name.lower() == 'admin':
            print('Hello admin,would you like to see a status report?')
        else:
            print(f"Hello {name.title()},thank you for logging in again")
else:
    print("We need to find some users!",'\n')

#5-10
current_users=['Gsl','Mzy','mzt','xtz','nn'] #建立一个列表
current_users2=[]
for current_user in current_users:
    current_user=current_user.lower() #把元素变成小写
    current_users2.append(current_user) #把小写的元素加入新建立的空列表
print(current_users2)
new_uers=['xtz','William guo','mzy','gulugulu','makabaka']
for new_usr in new_uers:
    if new_usr in current_users2:
        print(f"Pity!{new_usr.title()}!This name has been used!")
    else:
        print(f"Congratulations,{new_usr.title()}!Register completed!")
print("")

for x in list(range(1,10)):
    if x == 1:
        print(f"{x}st")
    elif x == 2:
        print(f"{x}nd")
    else:
        print(f"{x}th")







