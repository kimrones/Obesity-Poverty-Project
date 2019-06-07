import pandas as pd
import numpy as np
import sqlite3
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func

#from flask import Flask, jsonify
from flask import Flask, render_template, jsonify
from sqlalchemy.ext.automap import automap_base
# from obesity import OBESITY

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///data/OB_ALL_STATES_2013.sqlite")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data/National_Obesity_By_State.sqlite"

db = SQLAlchemy(app)

# class Obesity(db.Model):
#     __tablename__ = 'Obesity'

#     state = db.Column(db.String, primary_key=True)
#     percent = db.Column(db.Float)
#     shape_area = db.Column(db.Float)
#     shape_length = db.Column(db.Float)

#     def __repr__(self):
#         return '<Obesity %r>' % (self.name)

# @app.before_first_request
# def setup():
#     # Recreate database each time for demo
#     # db.drop_all()
#     db.create_all()

# # reflect an existing database into a new model
Base = automap_base()
# # reflect the tables
Base.prepare(db.engine, reflect=True)

# # Save reference to the table
# print("Base.classes: ")
# print(Base.classes.keys())
# print("\n\n")
obesity_data = Base.classes.ob

# # Create our session (link) from Python to the DB
# session = Session(engine)

# app = Flask(__name__)

# @app.route("/")
# def index():
#     """Return the homepage."""
#     return render_template("index.html")


# @app.route("/states")
# def states():
#     """Return a list of all state names"""
#     # Query all states
#     results = session.query(Obesity.state).all()

#     # Convert list of tuples into normal list
#     all_states = list(np.ravel(results))

#     return jsonify(all_states)

# def get_states(source):
#     states = []
#     for row in source:
#         state = row["State"]
#         states.append(state)
#     return sorted(states)
    # return state

def get_states(source):

    # results = session.query(Obesity.state).group_by
    # results = db.session.query(Obesity.state, Emoji.score).\
    #     order_by(Emoji.score.desc()).\
    #     limit(10).all()


    states = []
    for row in source:
        state = row["State"]
        states.append(state)
    return sorted(states)    

def get_percent(source, state):
    for row in source:
        if state == row["State"]:
            # decode handles accented characters
            percent = row["Percent"]
    return state, percent

@app.route('/')
def index():
    # return '<h1>Go to /awards/</h1>'
    # results = db.session.query(Obesity.state).\
    #     order_by(Obesity.state.desc())
    # #print(results)
    # conn = sqlite3.connect('/data/National_Obesity_By_State.sqlite')
    # cur = conn.cursor()

    # def get_data():
    #     cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    #     conn.commit()
    #     print(cur.fetchall())
    
    # get_data()
    results = db.session.query(obesity_data).all()

    states = {}

    for result in results:
            # Create primaryzip code key
         states[result[0]] = {
            "percent":result[1]
            }
    return jsonify(states) 

    return render_template('index_test.html', states=states)
    # return ('/awards/')

@app.route('/states')
def states():

    # results = db.session.query(Obesity.state).\
    #     order_by(Obesity.state.desc())
    # print (results)
    # return results
    # states = get_states(OBESITY)
    # pass the sorted list of titles to the template
    # return render_template('index_new.html', states=states)

# @app.route('/awards/<title>')
# def state(percent):
    
#     # pass the data for the selected book to the template
#     return render_template('index.html', state=state, percent=percent)
    sel = [
            obesity_data.state,
            obesity_data.percent, 
            obesity_data.shape__Area,
            obesity_data.pe__length
        ]

    results = db.session.query(*sel).all()
    print(results)
        
    states_ob = {}

        # Loop through each result
    for result in results:
            # Create primaryzip code key
        states_ob[result[0]] = {
            "percent":result[1],
            "shape":result[2],
            "length":result[3]

            }

    print(states_ob)
    return jsonify(states_ob)

if __name__ == "__main__":
    app.run(debug=True)