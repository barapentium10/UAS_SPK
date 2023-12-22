from http import HTTPStatus

from flask import Flask, request
from flask_restful import Resource, Api 

from models import Phone

app = Flask(__name__)
api = Api(app)        

class Recommendation(Resource):

    def post(self):
        criteria = request.get_json()
        phone = Phone()

        if not criteria:
            return 'criteria is empty', HTTPStatus.BAD_REQUEST.value
        recommendations = phone.get_recs(criteria)

        return {
            'alternatif': recommendations
        }, HTTPStatus.OK.value


api.add_resource(Recommendation, '/recommendation')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
