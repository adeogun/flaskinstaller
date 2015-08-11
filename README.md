# flaskinstaller 
Basic flask installer that:

* Creates a basic flask web app folder structure
* Creates a hello world app
* Setups up blueprint support
* Installs a virtual environment
* Installs flask and some common modules
* Launches an instance of the flask webserver on the localhost with the hello world app

Requires 
python 2.*
pip

＃ Windows  Usage 

flaskinit.bat [projectdirectory] [projectname]

Example

flaskinit.bat c:\flasktemp flaskapp

# Linux Usage

chmod 755 flaskinit.sh
sudo ./flaskinit.sh [projectdirectory] [projectname]


Example

chmod 755 flaskinit.sh
sudo ./flaskinit.sh /home/user/flasktemp flaskapp

