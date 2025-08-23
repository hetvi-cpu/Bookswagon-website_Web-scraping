#Bookswagon-Website-Web-Scraping


# using Beauifulsoup,requests,panda
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    books=soup.find_all("div",class_="card align-items-center")
    #print(books)
    data=[]


    for book in books:
        item={}
        item["title"]=book.find("img",class_="card-img-top").attrs["alt"]
        item["image"]=book.find("img",class_="card-img-top bklazy").attrs["data-src"]
        item["price"]=book.find("span",class_="actualprice").text[1:]
        print("book=",book.text)
        data.append(item)
        print("--------")
    return data

def export_data(data):
     df=pd.DataFrame(data)
     df.to_excel("books1.xlsx")
     print("exprt to excel")
     df.to_csv("books.csv")
     
if __name__=='__main__':
    data=get_data("https://www.bookswagon.com/")
    print(data)
    export_data(data)
    print("done")
    

        
        


