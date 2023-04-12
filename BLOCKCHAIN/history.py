class write_file:
    hash : str
    prev_hash:str
    date : str
    proof_of_work : str
    id: str
    val : str

    def __init__(self,hash,prev_hash,date,proof_of_work,id,z):
        self.hash=hash
        self.prev_hash=prev_hash
        self.date=date
        self.proof_of_work = proof_of_work
        self.ID=id
        self.val=z
        w.writeit(self)
        return None
    

class write:
    list= []
    def writeit(a):
        w.list.append(a)
        file = open('history.txt','w')
        for i in w.list:
            file.write("\n")
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
            file.write(str(i.hash))
            file.write("\n ")
            file.write("value:")
            file.write(str(i.val))
            file.write("\n")
        return None
    
    def get_valuse():
        file3 = open("history.txt", 'r')
        values = file3.readlines()
        j=0
        val =""
        for i in values:
            for k in i:
                val= val + k[j]
        print(val)
        return val
    

w= write
