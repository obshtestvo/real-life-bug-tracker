from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.pymongo import PyMongo

import datetime

app = Flask('gradame')
api = restful.Api(app)
mongo = PyMongo(app)

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
		args = parser.parse_args()
		# Retrieve address
		signal = {
			'type': args['type'],
			'dates': [{'event': 'added', 'date': datetime.datetime.now()}],
			'status': 'new',
			'details': args['details'],
			'picture': '',
			'location': {'latitude': args['lat'], 'longtitude': args['lng'], 'address':'', 'city':'', 'country':'BG'},
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