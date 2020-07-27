import logging as l

l.basicConfig(filename="C:\\Users\\rohan.mehta\\Desktop\\05\\basic.log", level= l.DEBUG ,filemode='w')


logg = l.getLogger()

logg.error("Error")