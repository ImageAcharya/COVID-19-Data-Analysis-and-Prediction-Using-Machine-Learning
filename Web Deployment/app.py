from flask import Flask, render_template
import requests, json
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as po

#Running the Flask web server
app = Flask(__name__)

"""#### Overview Page"""

#Getting worldwide cases from a API
wcases = requests.get("https://disease.sh/v3/covid-19/all").text
wcases = json.loads(wcases)
tcases = wcases["cases"]
tdeaths = wcases["deaths"]
trecovered = wcases["recovered"]
tactive = wcases["active"]

#Function to generate respective data of each country from API
def funct(data):
    Cdata = requests.get("https://disease.sh/v3/covid-19/countries?sort="+data).text
    Cdata = json.loads(Cdata)
    dataList = []
    for i in range(0,221):
        dataList.append([Cdata[i]["country"], Cdata[i][data]])
    return dataList

#Getting total cases of each country from a single API
CcasesList = funct("cases")
#Getting total deaths of each country from a single API
CdeathsList = funct("deaths")
#Getting total recovered of each country from a single API
CrecoveredList = funct("recovered")
#Getting total active cases of each country from a single API
CactiveList = funct("active")

#World Map Visualization
dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)
fig = px.choropleth(df, locations="Country", locationmode="country names", color="Confirmed", animation_frame="Date")
fig.update_layout(title_text="COVID-19 Global Map")
outputHTML = po.plot(fig, include_plotlyjs=False, output_type="div")


#Defining the webpage routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/overview")
def overview():
    return render_template("overview.html", Total_Cases=tcases, Total_Active_Cases=tactive, Total_Deaths=tdeaths, Total_Recovered=trecovered, CcasesList=CcasesList, CdeathsList=CdeathsList, CrecoveredList=CrecoveredList, CactiveList=CactiveList, worldMap=outputHTML)

@app.route("/visualization")
def visualtion():
    return render_template("visualization.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(port=80, host="127.0.0.1")

