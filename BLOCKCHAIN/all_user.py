import QR_gen
import secrets


class users:
    user_name: str
    pass_word : str
    id: int
    key='ff5877'
    key2= str

    def __init__(self,username:str,password:str, key:str):
        if(self.key==key):
            self.user_name=username
            self.pass_word= password
            self.key2 = secrets.token_hex(6)
            u.add_user(self)
            self.id=users.user_ID()
            QR_gen.user_qr(username,password,self.id,self.key2)

    def get_key2(self):
        return self.key2
        
        
    def user_ID():
        return (u.id)

class list_of_users:

    user = []
    id = len(user)
    
    def add_user(user=users):
        u.user.append(user)
        file = open('users.txt','w')
        j= 0
        for i in u.user:
            j=(j+1)
            file.write("user id:")
            file.write(str(j))
            file.write("\n")
            file.write("user name:")
            file.write(i.user_name)
            file.write("\n")
            file.write("password:")
            file.write(i.pass_word)
            file.write("\n")
            file.write("secret key 2:")
            file.write(i.key2)
            file.write("\n")
        file.close()

    def verify_user(id,user_name,password,key):
        f = open('users.txt','r')
        f_content= f.readlines()
        a= ("user name:"+user_name)
        b=("password:"+password)
        k=("secret key 2:"+key)
        c=False
        d=False
        l=False
        e=0
        
        for i in f_content:
            e=(e+1)
            if(e>100):
                print("user not found...")
                break
            else:
                g=i.split("\n")
                print(g)
                for h in g:
                    if(h==k):
                        l= True
                        print("secret key found...")


        for i in f_content:
            e=(e+1)
            if(e>100):
                print("user not found...")
                break
            else:
                g=i.split("\n")
                print(g)
                for h in g:
                    if(h==a):
                        c= True
                        print("username found...")
        e=0
        for i in f_content:
            e=(e+1)
            if(e>100):
                print("user not found...")
                break
            else:
                g=i.split("\n")
                #print(g)
                for h in g:
                    if(h==b):
                        print("password found...")
                        d= True
                
        f.close()
        if(c and d and l):
            return True
        else:
            False


u = list_of_users
#u1 = users("ASH","1234","ff5877")
#u.verify_user(1,"ASH","1234")
