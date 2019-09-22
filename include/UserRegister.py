from app import app
from flask import Flask,request,flash
import json
import DbOperation

app = Flask(__name__)

db= DbOperation.DbOperation

@app.route('/')
def index():
	response={"Error":False,"Message":"Index Function"}
	return json.dumps(response)

@app.route('/UserRegister',methods=['POST'])
def UserRegister():
	try:
		response={}
		username=request.form['inputUsername']
		password=request.form['inputPassword']
		email=request.form['inputEmail']
		contact=request.form['inputContact']

		#here check wether user exits of not
		res=db.UserExitOrNot(email)
		if res:

			response ={"Error":True,"Message":"User Already Registered"}
		else:

			result=db.InsertUser(username,password,email,contact)
			print(json.dumps(result))
			if result == True:
				response ={"Error":True,"Message":"User Registered Successfully"}

			elif result ==False:
				response ={"Error":False,"Message":"Error While Registering User"}

	except Exception as e:
		print(e)

	return json.dumps(response)

if __name__ == "__main__":
    app.run(debug=True)
