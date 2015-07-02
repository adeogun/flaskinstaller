set directory=%1
set projectname=%2
echo Starting Flask Installer
echo %directory%
echo %projectname%
python flaskinit.py --dir %directory% --projectname %projectname%
cd %directory%
pip install virtualenv
virtualenv flaskenv
call flaskenv\Scripts\activate
pip install -r requirements.txt
python run.py