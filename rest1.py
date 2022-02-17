from flask import Flask,request,jsonify
from flask_restful import Resource,Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)

identitas = {}

class Rest1(Resource):
    def get(self):
        return identitas
    
    def post(self):
        dataNama = request.form["nama"]
        dataNip = request.form["nip"]
        identitas["namo"] = dataNama
        identitas["nipi"] = dataNip
        response = ({"msg":"berhasil nih dong"})
        return response

api.add_resource(Rest1,"/api",methods=["GET","POST"])    

if __name__ == '__main__':
    app.run(debug=True,port=5015)
    
    