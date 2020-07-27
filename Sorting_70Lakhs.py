import random
def CreateFile():
    f=open("my_Sorting.txt","w+")

    for i in  range(70000000):
        f.write('%d ' %random.randint(1,1000))

    f.close()


def ReadFile():
    f=open("my_Sorting.txt","r")
    contents = f.read()
    f.close()
    return contents

def ConvertToList(mystr):

    mystr=mystr.rstrip()
    return [int(i) for i in mystr.split(' ')]

CreateFile()
# a = ReadFile()
# big_list = ConvertToList(a)
#
# big_list.sort()
# print(big_list)
