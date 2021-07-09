import datetime
from pprint import pprint
# from wtforms import Form, SelectField, form, StringField
from flask import Flask, render_template, request, Response, jsonify
import flask
import json
from flask.json import dump
from google.auth.environment_vars import PROJECT
from google.cloud import datastore
from google.cloud.datastore import entity
from werkzeug.utils import redirect
# from wtforms.fields.core import StringField
import pdb

from werkzeug.wrappers import response

datastore_client = datastore.Client()


def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)


def delete_time(dt):
    # print(f'the id is {dt}')
    # datastore_client = datastore.Client()
    # entity = datastore.Entity(key=datastore_client.key('visit'))
    key = datastore_client.key('visit', int(dt))
    result = datastore_client.delete(key=key)
    print(result)

    # print(f'Key dir {dir(key)}')
    # print(f'Key type {type(key)}')
    # print(f'Key id {key}')

    # entity = datastore_client.get(key)

    # print(entity)


    # datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)
    # for time in times:
    #   print(time)
    return list(times)


app = Flask(__name__)

# class MyForm(Form):
#   timestamp = StringField('timestamp')

@app.route('/', methods=['POST','GET'])
def root():
    # Store the current access time in Datastore.
    store_time(datetime.datetime.now())
    # form = MyForm()

    # Fetch the most recent 10 access times from Datastore.
    times = fetch_times(100)

    return render_template(
        'index.html', times=times)


@app.route('/view', methods=['POST', 'GET'])
def view():
    times = fetch_times(10)
    return render_template(
        'index.html', times=times)


@app.route('/add', methods=['POST'])
def add():
  if request.form.get('new_item'):
    item = request.form['new_item']
    store_time(item)
    resp = jsonify(success=True)
    return resp


@app.route('/remove/<int:id>/', methods=['POST','GET'])
@app.route('/remove', methods=['POST'])
def remove(id=None):
    if id:
        id_list = [id]
    else:
        id_list = request.form.getlist('key')
    for key in id_list:
      pprint(key)
      delete_time(key)
    return redirect('/view',code=302)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
