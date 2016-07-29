Develop a Sample Application Blueprint using Python

Long Term Objectives : Enterprise Grade Security, Cloud/Mobile Ready, Containerized, API Enabled, BigData Realtime Backend 

# Quick Start

### Web/REST Application Blueprint 

### Components
* Database residing in data/user.db
* webapi_server.py is API Server serving data from user.db
* webapp_server.py is Web Server which connects to API Server for data


### Initilize the Environment.

* Install and Activate the python 3.5 environment
	* pyenv install 3.5 env 	
	* source env/bin/activate
* Install the module dependencies
	* pip install -r requirements.txt
* Initialize the database using admin.py
	* python admin.py
 	
### Start WebAPI Server 

* python webapi_server.py 1>logs/webapi_server.log 2>&1 &
   * Note : this command sends the job into background.. 
* Test if the webapi is responding
   * open webbrowser and http://127.0.0.1:5000/api/v1.0/user/list
   	
### Start WebApp Server

* python webapp_server.py 1>logs/webapp_server.log 2>&1 &
* Test if the webapp is responding
   * open webbrowser and http://127.0.0.1:8080/
 	
 	
