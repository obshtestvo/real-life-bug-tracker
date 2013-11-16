import os
import werkzeug
from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.pymongo import PyMongo

import datetime

app = Flask('gradame')
api = restful.Api(app)
mongo = PyMongo(app)
UPLOAD_DIR = os.path.dirname(os.path.realpath(__file__)) + '/upload/'

parser = reqparse.RequestParser()
parser.add_argument('limit', type=int)
parser.add_argument('page', type=int)
parser.add_argument('lat', type=str)
parser.add_argument('lng', type=str)
parser.add_argument('type', type=str)
parser.add_argument('status', type=str)
parser.add_argument('nonstrict', type=str)

class Signal(restful.Resource):
	def get(self, signal_id):
		args = parser.parse_args()
		signal = mongo.db.signals.find_one(signal_id)
		return (signal, 200) if signal else {'message':'Not Found.', 'status':404}, 404

	def delete(self, signal_id):
		"""Delete a signal"""
		pass


class Signals(restful.Resource):
	def get(self):
		"""Retrieve all signals filtered using
		the parameters specified."""
		pass

	def put(self):
		pass

	def post(self):
		"""Create a new signal.
		Not Implemented yet!
		"""
		parser.add_argument('details', type=str)
		parser.add_argument('address', type=str)
		parser.add_argument('city', type=str)
		parser.add_argument('photo', type=werkzeug.datastructures.FileStorage, location='files')
		args = parser.parse_args()
		photo_filename = werkzeug.secure_filename(args['photo'].filename)
		args['photo'].save(UPLOAD_DIR + photo_filename)
		# Retrieve address
		signal = {
			'type': args['type'],
			'dates': [{'event': 'added', 'date': datetime.datetime.now()}],
			'status': args['status'], # could be 'new' or 'duplicate'
			'details': args['details'],
			'picture': photo_filename,
			'location': {
                'latitude': args['lat'],
                'longtitude': args['lng'],
                'address': args['address'],
                'city': args['city'],
                'country':'BG'},
			'user_id': 0
		}
		return {'message': 'Successfuly created new signal.'}, 201

	def delete(self):
		"""Mass delete signals based one specific criteria."""
		pass

api.add_resource(Signal, '/signal/<string:signal_id>', endpoint='signal')
api.add_resource(Signals, '/signals', endpoint='signals')

if __name__ == '__main__':
	app.run(debug=True)