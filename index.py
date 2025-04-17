import requests
from bs4 import BeautifulSoup

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>李宥萱Python網頁(時間+8,work)</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=yohsuan&work=pu>傳送使用者暱稱</a><br>"
    homepage += "<a href=/account>網頁表單傳值</a><br>"
    homepage += "<a href=/about>yo hsuan簡介網頁</a><br>"
    homepage += "<br><a href=/read>讀取Firestore資料</a><br>"
    homepage += "<br><a href=/spider>爬取開眼即將上幕的電影,存到資料庫</a><br>"
    return homepage


@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    return render_template("rwd.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    w = request.values.get("work")
    return render_template("welcome.html", name=user,work=w)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/read")
def read():
    Result = ""
    db = firestore.client()
    collection_ref = db.collection("靜宜資管")    
    docs = collection_ref.order_by("mail").get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result

app.route("/spider")
def spider():
    db=firestore.client()

    url = "https://www.atmovies.com.tw/movie/next/"
    Data = requests.get(url)
    Data.encoding = "utf-8"

    sp = BeautifulSoup(Data.text, "html.parser")
    result=sp.select(".filmListAllX li")

    for item in result:
        img= item.find("img")
        #print("片名:",img.get("alt"))
        #print("海報",img.get("src"))
        a = item.find("a")
        #print("介紹", "https://www.atmovies.com.tw"+ a.get("href"))
        #print("編號", a.get("href")[7:19])
        div = item.find(class_="runtime")
       #print("日期:", div.text[5:15])
        
        if div.text.find("片長: ")>0:
            FilmLen = div.text[21:]
            #print("片長:",div.text[21:])
        else:
            FilmLen = "無"
            #print("目前無片長資訊")
            #print()

        doc = {
            "title": img.get("alt"),
            "hyperlink": "https://www.atmovies.com.tw"+a.get("href"),
            "picture": img.get("src"),
            "showDate":div.text[5:15],
            "showLength":FilmLen
        }

        doc_ref=db.collection("李宥萱").document(a.get("href")[7:19])
        doc_ref.set(doc)
    return"資料庫已更新"

if __name__ == "__main__":
    app.run()

