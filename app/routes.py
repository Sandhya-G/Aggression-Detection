from app import app
import pickle
import numpy as np
from pathlib import Path
from flask import render_template

@app.route('/')
@app.route('/home')
def index():
	# Pkl_Filename = Path("model/Pickle_KNN_Model.pkl")
	# with open(Pkl_Filename, 'rb') as file:  
	# 	Pickled_KNN_Model = pickle.load(file)
	# return str(Pickled_KNN_Model)
	 
	return render_template('home.html')
