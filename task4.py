import json
print("welcome")
print("choose what you want")
user=input("choose ,1.login/2.signup:-")
d={}
dict1={}
list=[]
username=input("enter username:-")
pw=input("enter password:-")
if user=="1":
    #username=input("enter username")
    #pw=input("enter password")
    if (pw>="a" and pw<="z") or (pw>="A" and pw<="Z") or (pw<=0 and pw>=9) or (pw=="#",pw=="@",pw=="$",pw=="%"):
        print("strong password")
        d.setdefault(username,pw)
        #print(dict)
        dict1.setdefault("user",d)
        #print(dict1)
        list.append(dict1)
        print(list)
        # x=list
        # with open("task.json","w") as file:
        #     json.dump(x,file,indent=4)
        #     print(x)
        print("congratulation")   
    else:
        pw1=input("enter password:-")
        if pw==pw1:
            print("both are same")
        else:
            print("both are not same")
elif user=="2":
    dict5={}
    list1=[]
    username1=input("enter username:-")
    if username==username1:
        print("already exist")
    else:
        des=input("enter your description:-")
        hobbies=input("enter hobbies:-")
        gender=input("enter gender:-")
        print("congrats")
            
        # with open("pinky.json","a") as file:
        dict1={}
        dict2={}
        dict3={}
        dict3["Description"]=des
        dict3["Hobbies"]=hobbies
        dict3["Gender"]=gender
        dict4={}
        dict4["username"]=username
        dict4["password"]=pw
        dict4["profile"]=dict3
        list1.append(dict4)
        dict5["user"]=list1
            # json.dump(dict5,file,indent=4)
        print(dict5)
        print("congratulation")
        import os
        if os.path.exists("p.json"):
            file=open("p.json","r")
            py=json.load(file)
        # print(py)   
            
            if "user" in py:
                list1=py["user"]
            list1.append(dict4)
            dict5["user"]=list1
            f=open("p.json","w")
            json.dump(dict5,f,indent=5)
            f.close() 
            
        else:
            f=open("p.json","w")
            json.dump(dict5,f,indent=5)
            f.close() 
else:
    print("try again")           

                
            
            
            
            
            