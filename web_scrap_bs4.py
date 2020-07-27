from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as openurl

my_url = "http://www.newegg.com/global/in-en/p/pl?d=iphone"

response = openurl(my_url)
html_body = response.read()

response.close()

my_soup = soup(html_body,"html.parser")

products = my_soup.findAll("a",{"class":"item-title"})

filename="products.csv"
f = open(filename,"w")

f.write("brand,Link\n") # works as header


for product in products:
    a=product.text
    b= product["href"]
    #print("Product Name is {} and Click Link {} ".format(a.strip(),product["href"]))

    f.write(a.strip() + "," + b.replace(",","|") + "\n")

f.close()




