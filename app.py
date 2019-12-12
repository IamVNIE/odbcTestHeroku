from flask import Flask
from datetime import datetime
from sqlalchemy import create_engine
import platform
import pyodbc 
app = Flask(__name__)

drivers = [item for item in pyodbc.drivers()]
try:
	driver = drivers[-1]
	print("\n\n\tdriver:{}".format(driver))
except:
	print("\n\n\tdriver:{}".format(drivers))
	
@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %B %Y %I:%M:%S %p")

    return("""
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
	<p>It is running {platform_uname}.</p>
	<p>Pyobdc Driver Name {drive_name}.</p>
	""".format(time=the_time,
				platform_uname=platform.uname(),
				drive_name=drivers))
	
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
	
'''
<p>It is running {platform_uname} {platform_system}.</p>
, platform_uname = platform.uname(),
				platform_system=platform.system()
'''