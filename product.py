class Customer():
    def __init__(self,name,type,role,branch):
        self.name = name
        self.type = type
        self.role = role
        self.branch = branch

    def info(self):
        print("name : " + self.name.title())
        print("type : " + self.type.title())
        print("role : " + self.role.title() + "\nbranch :" + self.branch.title())


coke = Customer("Coca cola manf.","Manufacturer","manager","main")

coke.info()
