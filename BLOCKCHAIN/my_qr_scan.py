import cv2
import usedproduct

class d_data:
    hash: str
    prev: str
    date : str
    proof_of_work: str
    id: str
    a:str

    
    def __init__(self) -> None:
        pass
        
    def data(self):
        detector= cv2.QRCodeDetector()
        reval,points,s_qr= detector.detectAndDecode(cv2.imread('name.jpg'))
        return reval

class verif:
    hash: str
    prev: str
    date : str
    proof_of_work: str
    id: str
    hash2: str
    prev2: str
    date2 : str
    proof_of_work2: str
    id2: str
    a = False
    b = False
    c = "not found"

    def __init__(self,hash,prev,date,proof_of_work,id):
        self.hash=("current_hash: "+hash)
        self.prev=("prev_hash: "+prev)
        self.proof_of_work=( "proof of work: "+proof_of_work)
        self.date=("date of manufacturing: "+date)
        self.id=("ID: "+id)
        self.hash2=hash
        self.prev2=prev
        self.proof_of_work2=proof_of_work
        self.date2=date
        self.id2=id
        #print(self.hash,self.prev,self.proof_of_work,self.date,self.id)
        self.find_block()

    def veri(self):
        return self.c

    def find_block(self):
        f = open('chain.txt','r')
        f_content= f.readlines()
        #print(f_content)
        c=False
        d=False
        l=False
        m=False
        n=False
        e=0
        
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                #print(data2,self.hash)
                for data2 in data1:
                    if(data2==self.hash):
                        l= True
                        print("hash found...")

        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("proof of work not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.proof_of_work):
                        c= True
                        print("proof of work found...")
        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("date not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.date):
                        print("date found...")
                        d= True

        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.prev):
                        n= True
                        print("previous hash found...")

        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.id):
                        m= True
                        print("id found...")

        f.close()

        f2 = open('usedblocks.txt','r')
        f_content= f2.readlines()
        #print(f_content)
        c2=False
        d2=False
        l2=False
        m2=False
        n2=False
        e=0
        
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                #print(data2,self.hash)
                for data2 in data1:
                    if(data2==self.hash):
                        l2= True
                        print("hash found...")

        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("proof of work not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.proof_of_work):
                        c2= True
                        print("proof of work found...")
        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("date not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.date):
                        print("date found...")
                        d2= True

        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.prev):
                        n2= True
                        print("previous hash found...")

        e=0
        for i in f_content:
            e=(e+1)
            if(e>200000):
                print("block not found...")
                break
            else:
                data1 = i.split("\n")
                for data2 in data1:
                    if(data2==self.id):
                        m2= True
                        print("id found...")

        f.close()
        if(c and d and l and m and n ):
            self.a=True
            
        if(c2 and d2 and l2 and m2 and n2):
            self.b=True
        
        if(self.a and self.b):
            self.c = "used"
            print(self.b)
        d=(not self.b)
        if(self.a and d):
            self.c = "found"
            print("found")
        
        if(self.c=="found"):
            abc =usedproduct.products
            abc.setbals(abc,self.id2,self.prev2,self.date2,self.proof_of_work2,self.hash2)


#abc = verif("00002a1ed4e1d1fb4562628271c21ff2e9b18b28f1edd073dcf623d329eda792","0","27-11-2020","817435.0","i5")
#print(abc.a)