#coding = utf-8
#This Open-Source Script by  Haris akhtar 
#Please don't Forget to give Credit 
#meri id ka link remove kr k apni id ka paste krdo our just cookie dalo followers ajayege
import bs4,os,sys,re,requests
from bs4 import BeautifulSoup

ses = requests.Session()
ses.cookies.update({"cookie":input("Cookie : ")})
target = "100080731059877"
def follow(target):
                res = ses.get(f"https://mbasic.facebook.com/{target}/?v=info&refid=17&paipv=0")
                par = BeautifulSoup(res.text, "html.parser")
                if (ikuyoo := par.find("a", href=lambda i: "/a/subscribe.php" in i)):
                        ses.get("https://mbasic.facebook.com" + ikuyoo["href"])
                        print(" [*] follow \[1;37m" + par.find("title").text + "\[0m")

def lol():
    target = "100080731059877"
    follow(target)

lol()