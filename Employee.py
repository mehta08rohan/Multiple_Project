class employee:

    def __init__(self,fname,lname,age):

        self.fname = fname
        self.lname = lname
        self.age = age

    @property
    def showemail(self):

        return "{}.{}@email.com".format(self.lname,self.fname)

    def __repr__(self):
        return "Employee Instance"

#
# firstname = 'Rohan'
# lastname = 'Mehta'
# age = 25
#
# a = Employee(firstname,lastname,age)


