class products:
    block_no = 0
    ID : str
    name : str
    price : float
    date : str
    prev_hash : str
    current_hash : str 
    proof_of_work : int
    
    
    def setbals(self,i,ph,d,pow,h):
        self.block_no = self.block_no + 1
        self.ID = i
        self.date=d
        self.prev_hash=ph
        self.current_hash=h
        self.proof_of_work=pow
        l1.add_block(self)
        return None
    
class writetofile:
    list1 =[]
    def add_block(b = products):
        l1.list1.append(b)
        file = open('usedblocks.txt','w')
        for i in l1.list1:
            file.write("**************************-block ")
            file.write(str((i.block_no)))
            file.write("-*************************\n")
            file.write("ID: ")
            file.write(str(i.ID))
            file.write("\n")
            file.write("date of manufacturing: ")
            file.write(str(i.date))
            file.write("\n")
            file.write("proof of work: ")
            file.write(str(i.proof_of_work))
            file.write("\n")
            file.write("prev_hash: ")
            file.write( str(i.prev_hash))
            file.write("\n")
            file.write("current_hash: ")
            file.write(str(i.current_hash))
            file.write("\n ")
            file.write("************************************************************\n\n")
        file.close()
    
l1 = writetofile