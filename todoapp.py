from flask import Flask
import os

app = Flask(__name__)
cf_port = os.getenv("PORT")
#SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://d_C7o-_C3X3d_2Wb:iD-pPTkqgL-8YO8D@10.11.241.31:53062/GJh_WJfpXIqmg2sl'
#app.secret_key = 'i6XSrm4ElT_p2SBo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from views import *


#if __name__ == '__main__':
#   app.run()
    
if __name__ == '__main__':
   if cf_port is None:
#      app.run(host='0.0.0.0', port=5000)
       app.run(host='0.0.0.0',port=int(cf_port),debug=True)
   else:
       app.run(host='0.0.0.0',port=int(cf_port),debug=True) 
