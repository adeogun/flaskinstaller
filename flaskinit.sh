echo Starting Flask Installer
echo $1
echo $2
python flaskinit.py --dir $1 --projectname $2
cd $1
pip install virtualenv
virtualenv flaskenv
source flaskenv/bin/activate
pip install -r requirements.txt
python run.py
