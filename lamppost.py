#   For API
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
#   For Update lamp post csv
import threading
import time
import schedule
import requests
import os

app = Flask(__name__)
api = Api(app)


class LampPost(Resource):

    def get(self):      
        data = pd.read_csv('lamppost_en.csv', index_col=0, header=0)  # read local CSV
        args = request.args

        if("q" in args):                #   query (example: http://127.0.0.1:5000/lp?q=BE1240)
            return data.loc[args["q"]].to_dict(), 200     

        elif("update" in args):
            if (time.time() - os.path.getmtime('lamppost_en.csv') > (1 * 30 * 24 * 60 * 60)):   #   older than  3 months - (3 * 30 * 24 * 60 * 60) seconds
                print("File older than 1 month, updating...")
                updateCSV()
            else:
                print("File up to date")

        else:return 200
    

#   === CSV File updates
def updateCSV():
    url = "http://218.253.203.24/datagovhk/plis/lamppost_en.csv"    #   From https://data.gov.hk/en-data/dataset/hk-hyd-plis-lamppostdata
    lamppostFile = requests.get(url, allow_redirects=True)
    open('lamppost_en.csv', 'wb').write(lamppostFile.content)
    print("Downloaded")
#   === CSV File updates


api.add_resource(LampPost, '/lp')  # add endpoints
if __name__ == '__main__':
    app.run()  # run our Flask app
    
