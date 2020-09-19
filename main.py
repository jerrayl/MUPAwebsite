#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from flask import Flask, render_template, redirect, request
import jinja2
from google.cloud import ndb, datastore, storage
import csv
#from google.appengine.api import users
#from google.appengine.api import mail

app = Flask(__name__)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# Addresses
mupa_address = "mupa.general@gmail.com" 
mon_address = "sothomas@student.unimelb.edu.au"
wed_address = "sothomas@student.unimelb.edu.au"
fri_address = "sothomas@student.unimelb.edu.au"


# Model

class StudentModel(ndb.Model):

    name = ndb.StringProperty(required=True)
    studentid = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    course = ndb.StringProperty(required=True)
    degree = ndb.StringProperty(required=True)
    locker_floor = ndb.StringProperty(required=True)
    locker_number = ndb.StringProperty()
    day = ndb.StringProperty(required=True)
    assigned = ndb.BooleanProperty(required=True, indexed=True)

# Setup Client
client = ndb.Client()

# Landing Page

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/committee')
def committee():
    return render_template("committee.html")

@app.route('/contact') 
def contact():
    return render_template("contact.html")

@app.route('/information/course') 
def course():
    return render_template("course.html")

@app.route('/information/organizations') 
def organizations():
    data = []
    with open("organizations.csv", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile) 
        for row in reader: 
            data.append(row)
    return render_template("organizations.html", organizations=data)

@app.route('/events') 
def events():
    return render_template("events.html")


""" Temporarily turned off
@app.route('/information/lockers', methods=['GET', 'POST'])
def lockers():
    if request.method == "POST":
        student = StudentModel()
        student.name = self.request.get("name")
        student.studentid = self.request.get("id")
        student.email = self.request.get("email")
        student.phone = self.request.get("phone")
        student.course = self.request.get("course")
        student.degree = self.request.get("degree")
        student.locker_floor = self.request.get("floor")
        student.day = self.request.get("day")
        student.assigned = False
        student.put()

        mail.send_mail(sender=mupa_address, to=mupa_address,
                            subject= "[Locker Request] " + student.name,
                            body='Name: '+ student.name + '\nEmail: ' + student.email + '\nPhone: ' + student.phone + '\nFloor: ' + student.locker_floor + '\nDay: ' + student.day +'\n')
        mail.send_mail(sender=mupa_address, to=student.email,
                            subject= "[Locker Request Confirmation]",
                            body='Dear '+ student.name + ',\n We have received your request for a locker and will be in touch soon. Thank you! \n Best Regards, \n MUPA')
        if student.day == "Monday":
            mail.send_mail(sender=mupa_address, to=mon_address,
                            subject= "[Locker Request] " + student.name,
                            body='Name: '+ student.name + '\nEmail: ' + student.email + '\nPhone: ' + student.phone + '\nFloor: ' + student.locker_floor + '\nDay: ' + student.day +'\n')
        elif student.day == "Wednesday":
            mail.send_mail(sender=mupa_address, to=wed_address,
                            subject= "[Locker Request] " + student.name,
                            body='Name: '+ student.name + '\nEmail: ' + student.email + '\nPhone: ' + student.phone + '\nFloor: ' + student.locker_floor + '\nDay: ' + student.day +'\n')
        else:
            mail.send_mail(sender=mupa_address, to=fri_address,
                            subject= "[Locker Request] " + student.name,
                            body='Name: '+ student.name + '\nEmail: ' + student.email + '\nPhone: ' + student.phone + '\nFloor: ' + student.locker_floor + '\nDay: ' + student.day +'\n')

        return redirect('/information/lockers?submitted=True')

    else:
        return render_template("lockers.html", submitted=request.args.get("submitted"))

       

@app.route('/lockeradmin', methods=['GET', 'POST'])
def admin():

    if request.method == "POST":
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            student = StudentModel.query(StudentModel.studentid == self.request.get("student_id")).fetch()[0]
            student.locker_number = self.request.get("locker_number")
            student.assigned = True
            student.put()
            self.redirect('/lockeradmin')
        else:
            return redirect('/')
    else:
        user = users.get_current_user()
        if user:
            if users.is_current_user_admin():
                user_status = "A"
                user_url = users.create_logout_url('/')
            else:
                user_status = "NA"
                user_url = users.create_logout_url('/')
        else:
            user_status = "NL"
            user_url = users.create_login_url('/lockeradmin')

        data = StudentModel.query().fetch()
        return render_template("lockeradmin.html", status=user_status, url=user_url, students=data)
    """
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)