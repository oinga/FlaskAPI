from flask import Flask, render_template, request
from flask import redirect,jsonify, url_for, flash, abort, current_app
from os import environ
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from dboModel import Base, Patient, Appt
from config.database import db, session_engine, skey
from auth_middleware import token_required


from flask import session as login_session
import random, string

import requests
from functools import wraps
import jwt

import string
import random

app = Flask(__name__)


DBSession = sessionmaker(bind=session_engine.engine)
session = DBSession()

# for cross database queries
cursor = db.cursor()
 

#JSON view patients limit 20 currently
@app.route('/patients')
@token_required
def patients():
    patients = session.query(Patient).limit(20).all()
    return jsonify(patients= [p.serialize for p in patients])


#JSON view patient
@app.route('/patient/<int:pat_id>')
@token_required
def patient(pat_id):
    patient = session.query(Patient).filter_by(id = pat_id).all()
    return jsonify(patient=[p.serialize for p in patient])


#JSON view appts limit 500
@app.route('/appts')
@token_required
def appts():
    appts = session.query(Appt).limit(500)
    return jsonify(appts=[a.serialize for a in appts])

#JSON view appts for physician
@app.route('/appts/<int:npi>')
@token_required
def phy_appt(npi):
    appts = session.query(Appt).filter_by(npi = npi).all()
    return jsonify(appts=[a.serialize for a in appts])


#JSON view patient appt
@app.route('/appt/<int:pat_id>')
@token_required
def appt(pat_id):
    appt = session.query(Appt).filter_by(f_patient_id = pat_id).all()
    return jsonify(Appt=[a.serialize for a in appt])



if __name__ == '__main__':
  app.secret_key = skey
  app.config['SECRET_KEY'] = app.secret_key
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(environ.get('PORT', 5000))
  app.config['DEBUG'] = True
  app.run(host='0.0.0.0', port=port)
