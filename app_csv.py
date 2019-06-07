from flask import Flask, render_template
from flask import request

app = Flask(__name__)
import csv

def comments():
    with open('data\\OB_ALL_STATES_2013.csv', 'r') as inFile: 
        reader = csv.reader(inFile)
        commentsList = [row for row in reader]
        