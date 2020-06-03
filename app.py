from flask import Flask, render_template, request, jsonify
import json
import requests
import sqlite3
import string
import datetime
import csv
import random
import yagmail
import re 
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/getdata",methods = ["POST"])
def get_data():
    url = "https://wikipedia.org/wiki/Apple_Inc."
    rPage = requests.get(url)
    soup = BeautifulSoup(rPage.content, "html.parser")
    tables = soup.find("div", {"class": "mw-parser-output"})
    tables.table.decompose()
    for span in tables.find_all("span",{'class':'mw-editsection'}):
        span.decompose()
    for image in tables.find_all("img"):
        image.decompose()
    soup.find('span', id="coordinates").decompose()
    tables1 = tables.find("div",{"class":"toc"})
    tables1.decompose()
    for a in soup.findAll('a'):
        if(a.has_attr("href")):
            a['href'] = a['href'].replace("/wiki", "https://wikipedia.org/wiki")
            a['href'] = a['href'].replace("/w/", "https://wikipedia.org/w/")
    return tables.prettify()

@app.route("/getdata2",methods = ["POST"])
def get_data2():
    url = "https://www.investopedia.com/news/apple-now-bigger-these-5-things/"
    rPage = requests.get(url)
    soup = BeautifulSoup(rPage.content, "html.parser")
    soup = soup.find("div", {"class": "comp article-body-content mntl-sc-page mntl-block"})
    for iframe in soup.find_all("iframe"):
        iframe.decompose()
    return soup.prettify()

@app.route("/getproducts",methods = ["POST"])
def getproducts():
    products = ""
    with open('database.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile,delimiter = ";")
        count = 0
        l = []
        for row in csvReader:
            l.append(row[1])
        # print(l)
        # print(set(l))
        # print(len(l))
        # print(len(set(l)))
        for row in set(l):
            # print(row[1])
            if(count != 0):
                products +=  "," + row
            else:
                products +=  row
            count+=1
    # print(products)
    return jsonify({"data":str(products)})

@app.route("/getproductdetails",methods = ["POST"])
def getproductdetails():
    productname = request.json["productname"]
    print(productname)
    with open('database.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile,delimiter = ";")
        dictionary = {}
        for row in csvReader:
            dictionary[row[1]] = row[0]
    if(productname in dictionary):
        url = dictionary[productname]
        # url = "https://en.wikipedia.org/wiki/Disk_II"
        rPage = requests.get(url)
        soup = BeautifulSoup(rPage.content, "html.parser")
        tables = soup.find("div", {"class": "mw-parser-output"})
        tables.table.decompose()
        for span in tables.find_all("span",{'class':'mw-editsection'}):
            span.decompose()
        for image in tables.find_all("img"):
            image.decompose()
        # tables1 = tables.find("div",{"class":"toc"})
        # tables1.decompose()
        # soup.find('span', id="coordinates").decompose()
        for a in soup.findAll('a'):
            if(a.has_attr("href")):
                a['href'] = a['href'].replace("/wiki", "https://wikipedia.org/wiki")
                a['href'] = a['href'].replace("/w/", "https://wikipedia.org/w/")
        return tables.prettify()
    else:
        return jsonify(),400

@app.route("/getcriticism",methods = ["POST"])
def get_criticism():
    url = "https://en.wikipedia.org/wiki/Criticism_of_Apple_Inc."
    rPage = requests.get(url)
    soup = BeautifulSoup(rPage.content, "html.parser")
    tables = soup.find("div", {"class": "mw-parser-output"})
    tables.table.decompose()
    for span in tables.find_all("span",{'class':'mw-editsection'}):
        span.decompose()
    for image in tables.find_all("img"):
        image.decompose()
    tables1 = tables.find("div",{"class":"toc"})
    tables1.decompose()
    # soup.find('span', id="coordinates").decompose()
    for a in soup.findAll('a'):
        if(a.has_attr("href")):
            a['href'] = a['href'].replace("/wiki", "https://wikipedia.org/wiki")
            a['href'] = a['href'].replace("/w/", "https://wikipedia.org/w/")
    return tables.prettify()

@app.route("/getnews",methods = ["POST"])
def get_news():
    url = "https://www.bing.com/news/search?q=apple&FORM=HDRSC6"
    rPage = requests.get(url)
    soup = BeautifulSoup(rPage.content, "html.parser")
    soup = soup.find("div",{"class":"newscontainer scroll-body"})
    soup = soup.find("div",{"class":"main-container"})
    for image in soup.find_all("img"):
        image.decompose()
    return soup.prettify()


if __name__ == '__main__':
    app.run(debug=True)