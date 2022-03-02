from flask import Flask, url_for, render_template
import yaml
import requests


app=Flask(__name__)

@app.route("/")
def indexPage():
    return render_template("home.html")

@app.route("/team")
def teamPage():
    doc=open("team.yml","r")
    doc=doc.read()
    team=yaml.load(doc, Loader=yaml.Loader)
    print(team)
    def getName(uuid):
        return requests.get("https://sessionserver.mojang.com/session/minecraft/profile/{0}".format(uuid)).json()
    
    return render_template("team.html", team=team, getName=getName)

@app.route("/impressum")
def legalPage():
    return render_template("impressum.html")


if __name__ == "__main__":
    app.run(port=80,host="0.0.0.0",debug=True)