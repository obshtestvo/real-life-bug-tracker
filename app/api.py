# coding=UTF-8
import datetime
import os
import werkzeug

from bson.objectid import ObjectId
from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.pymongo import PyMongo


app = Flask('gradame')
api = restful.Api(app)
mongo = PyMongo(app)
UPLOAD_DIR = os.path.dirname(os.path.realpath(__file__)) + '/upload/'
ALLOWED_PHOTO_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_PHOTO_EXTENSIONS

parser = reqparse.RequestParser()
parser.add_argument('limit', type=int)
parser.add_argument('page', type=int)
parser.add_argument('lat', type=float)
parser.add_argument('lng', type=float)
parser.add_argument('type', type=str)
parser.add_argument('status', type=str)
parser.add_argument('nonstrict', type=str)

class Signal(restful.Resource):
	def get(self, signal_id):
		args = parser.parse_args()
		signal = mongo.db.signals.find_one(ObjectId(signal_id))
		return (signal, 200) if signal else {'message':'Not Found.', 'status':404}, 404

	def delete(self, signal_id):
		"""Delete a signal"""
		pass

	def put(self,  signal_id):
		"""Scenarios:
		 - Add duplicate
		 - Mark as solved
		 - Mark as invalid (admin only - most likely to be manual?)
		 - Confirm signal is still existing
		Not Implemented yet!"""
		parser.add_argument('scenario', type=str)
		args = parser.parse_args()
		scenario = args['scenario']
		signal = mongo.db.signals.find_one(ObjectId(signal_id))
		if scenario=='resolution':
			# Adds new event in the “dates” property {event: “solved”, date: “2013-11-14”}
			# and the status is changed to “solved”. Where 2013-11-14 is the current date
			signal.update()
		elif scenario=='duplication':
			#asd
			signal.update()
		elif scenario=='invalidation':
			#asd
			signal.update()
		elif scenario=='affirmation':
			#asd
			signal.update()
		else:
			#normal update
			signal.update()

		return {}, 200


class Signals(restful.Resource):
    def get(self):
        """Retrieve all signals filtered using
        the parameters specified.
        Not Implemented yet!"""
        # ref: http://docs.mongodb.org/manual/reference/operator/query/nearSphere/
        # @todo: db.signals.ensureIndex( { location : "2dsphere" } )
        parser.add_argument('radius', type=int) # in meters
        parser.add_argument('user_id', type=int)

        args = parser.parse_args()
        criteria = {
            "location": {
                "$nearSphere": {
                    "$geometry": {
                        "type": "Point" ,
                        "coordinates": [ args['lat'] , args['lng'] ]
                    },
                    "$maxDistance": args['radius']
            }},
            "status": args['status'],
            "type": args['type'],
            "user_id": args['user_id']
        }
        criteria = dict((k, v) for k, v in criteria.iteritems() if v) # filter empty values
        signals = mongo.db.signals.find(criteria, limit=args['limit'])
        return (signals, 200) if signals else {'message': 'Nothing Found.', 'status':404}, 404


	def post(self):
		"""Create a new signal.
		Not Implemented yet!
		"""
		parser.add_argument('details', type=str)
		parser.add_argument('address', type=str)
		parser.add_argument('city', type=str)
		parser.add_argument('photo', type=werkzeug.datastructures.FileStorage, location='files')
		args = parser.parse_args()

		if not allowed_file(args['photo'].stream.filename):
			return {'message': 'Such image is not allowed.', 'status': 400}, 400

		photo_filename = werkzeug.secure_filename(args['photo'].stream.filename)
		args['photo'].save(UPLOAD_DIR + photo_filename)
		# Retrieve address
		signal = {
			'type': args['type'],
			'dates': [
                {'event': 'added', 'date': datetime.datetime.now()},
                {'event': 'last_updated', 'date': datetime.datetime.now()},
                {'event': 'last_confirmed', 'date': datetime.datetime.now()},
            ],
			'status': args['status'], # could be 'new' or 'duplicate'
			'details': args['details'],
			'photo': photo_filename,
			'location': {
                "type": "Point",
                "coordinates": [args['lat'], args['lng']], # added to comply with GeoJSON
                'latitude': args['lat'],
                'longtitude': args['lng'],
                'address': args['address'],
                'city': args['city'],
                'country':'BG'},
			'user_id': 0
		}
		mongo.db.signals.insert(signal)
		return {'message': 'Successfuly created new signal.'}, 201

	def delete(self):
		"""Mass delete signals based one specific criteria."""
		pass

api.add_resource(Signal, '/signal/<string:signal_id>', endpoint='signal')
api.add_resource(Signals, '/signals', endpoint='signals')

if __name__ == '__main__':
	app.run(debug=True)