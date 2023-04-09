from flask import Flask, render_template

import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", h2="た〜びっと")

@app.route("/member")
def member():
    return render_template("member.html", title="メンバ〜", h2="メンバ〜")

@app.route("/album")
def album():
    return render_template("album.html", title="旅行記録", h2="旅行記録")

@app.route("/roulette")
def roulette():
    df = pd.read_csv("./tarbitte/static/csv/pref_data.csv")
    df = df.to_numpy().tolist()
    return render_template("roulette.html", title="る〜れっと", h2="る〜れっと", df=df)

@app.route("/info/<int:id>")
def info(id):
    id = id-1
    df = pd.read_csv("./tarbitte/static/csv/pref_data.csv")
    df = df.to_numpy().tolist()
    return render_template("info.html", title="都道府県情報", h2=f"{df[id][1]}の情報", id=df[int(id)])