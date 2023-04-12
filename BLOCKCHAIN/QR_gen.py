import qrcode
import shutil
import os

class QR_co:
    block_no : str
    path_1 : str
    d : str
    def __init__(self,proof_of_work,id,date,name,prev_hash,hash,block_no):
        features = qrcode.QRCode(version=1, box_size=10, border=3)
        a= (f" proof of work: {proof_of_work}\ndate: {date}\n hash: {hash}\n prev_hash: {prev_hash}\n id: {id}")
        features.add_data(a)
        features.make_image(fit=True)
        b = features.make_image(fill_color = "black", back_color = "white")
        c= ("BLOCK-"+str(block_no)+".jpg")
        b.save(c)
        shutil.move(c, "C:/Users/vaz/Desktop/Project/BLOCKCHAIN/qrcodesImgs/")
        self.d=c
        

    def get_ad(self):
        self.c = ("C:/Users/vaz/Desktop/Project/BLOCKCHAIN/qrcodesImgs/"+self.d)
        return self.c

    def get_name(self):
        return self.d

class user_qr:
    def __init__(self,u_n,id,password,key) -> None:
        features = qrcode.QRCode(version=1, box_size=10, border=3)
        a= (f"user name: {u_n}\n ID: {id}\n password: {password}\n key: {key}")
        features.add_data(a)
        features.make_image(fit=True)
        b = features.make_image(fill_color = "black", back_color = "white")
        c= ("USER-"+str(u_n)+key+".jpg")
        b.save(c)
        shutil.move(c, "C:/Users/vaz/Desktop/Project/BLOCKCHAIN/user_qr/")
        self.block_no=c
        self.path_1= ("C:/Users/vaz/Desktop/Project/BLOCKCHAIN/user_qr/"+str(c))
    
    def get_path(self):
        return self.path_1