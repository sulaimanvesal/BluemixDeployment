# Application Deployment in Bluemix
This is a sample application showing how to deploy a simple hello world app using Cloud Foundry https://github.com/cloudfoundry/cli#downloads and the Python. The concept is similar to @IBM-Blumix.

# Step 1:
Download and install the Cloud Foundry CLI tool:

Mac OSX:

	$ brew tap cloudfoundry/tap
	$ brew install cf-cli
Ubuntu based Linux distributions:

	$ wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | sudo apt-key add -
	$ echo "deb http://packages.cloudfoundry.org/debian stable main" | sudo tee /etc/apt/sources.list.d/cloudfoundry-cli.list
	$ sudo apt-get update
	$ sudo apt-get install cf-cli
# Step 2
    $ cf login -a api.[my-cloudfoundry].com'
    API endpoint: https://api.[my-cloudfoundry].com
	
    Email> [my-email]
    Password> [my-password]
    Authenticating...
    OK
	
	$ cd [my-app-directory]
  	$ cf push
# Sample App

Clone the Hello Word app to your local environment from your terminal using the following command:

	$ git clone https://github.com/IBM-Bluemix/python-hello-world-flask.git
	cd into this newly created directory

Connect to Bluemix in the command line tool and follow the prompts to log in.

	$ cf api https://api.ng.bluemix.net
	$ cf login
	Push the app to Bluemix.

	$ cf push

#Run the app locally

If you have not already, download Python and install it on your local machine. 

Clone the app to your local environment from your terminal using the following command:

	$ git clone https://github.com/IBM-Bluemix/python-hello-world-flask.git
	cd into this newly created directory

Create a new virtual environment with virtualenv and activate

	$ virtualenv venv
	$ source venv/bin/activate
	Install the dependencies with pip

	$ pip install -r requirements.txt
Start your app locally with the following command

	$ python hello.py
This command will create a new Flask app and start your application. 
When your app has started, your console will print that your Running on http://0.0.0.0:8080/ (Press CTRL+C to quit).

You can write your own code the same as above format. This is for python code and you can also add other code with different languages.

# Some useful links

https://github.com/IBM-Bluemix/python-hello-world-flask 
	
https://github.com/cloudfoundry/cli 
	
https://www.ibm.com/watson/developercloud/doc/getting_started/gs-cf.shtml

Webinar on how to deploy your application: https://www.youtube.com/watch?v=9M86BfL9KX0

Coursera: https://www.coursera.org/learn/developer-iot/lecture/fQSGf/deploying-an-application-to-bluemix-part-1

# Extra:

I have uploaded a simple object recognition which has been written in Python and it used object recognition services by IBM Watson. You need to create a service and from there copy the API-Key and replace it with the one which is in the code:
	
	1: Download watson_developer_cloud
	2: You need to install json2html package because it maps the json file to web html file.
	3: copy the code to your environment
	4: copy the API-Key from object-recognition services to the code
	 visual_recognition = VisualRecognitionV3('2016-05-20', api_key='a725a8b083d84215e86fa74ef64cc824dbe1090e')
	5: run the code.
