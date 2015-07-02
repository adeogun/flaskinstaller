import optparse
import cmd
import os

def setup(directory, project_name):
    models = 'models'
    templates = 'templates'
    tests = 'tests'
    views = 'views'
    static = 'static'
    init_file = '__init__.py'
    
    try:
                                    
        project_directory = os.path.join(directory,project_name)
        if not os.path.exists(directory):
            os.makedirs(directory)            
        
        print('Directory Created ' + directory)
        os.makedirs(project_directory)
        print('Directory Created ' +  project_directory)            
        os.makedirs(os.path.join(project_directory, models))
        print('Directory Created ' + os.path.join(project_directory, models))
        os.makedirs(os.path.join(project_directory, templates))
        print('Directory Created ' + os.path.join(project_directory, templates))
        os.makedirs(os.path.join(project_directory, tests))
        print('Directory Created ' + os.path.join(project_directory, tests))
        os.makedirs(os.path.join(project_directory, views))
        print('Directory Created ' + os.path.join(project_directory, views))
        os.makedirs(os.path.join(project_directory, static))
        print('Directory Created ' + os.path.join(project_directory, static))
        
        f = open(os.path.join(directory, 'config.py'),'w')
        f.close()
        print('File Created ' + os.path.join(directory, 'config.py'))
        
        f = open(os.path.join(directory, 'run.py'),'w')
        f.write('from %s import app\n' % project_name)
        f.write('app.run(debug=True)')        
        f.close()
        print('File Created ' + os.path.join(directory, 'run.py'))
        
        f = open(os.path.join(directory, 'requirements.txt'), 'w')
        f.write('Flask==0.10.1\n')
        f.write('alembic==0.7.6\n')
        f.write('Flask-Bootstrap==3.0.3.1\n')
        f.write('Flask-Login==0.2.11\n')
        f.write('Flask-Migrate==1.1.0\n')
        f.write('Flask-Script==2.0.5\n')
        f.write('Flask-SQLAlchemy==2.0\n')
        f.write('Flask-WTF==0.9.4\n')
        f.write('itsdangerous==0.24\n')
        f.write('Jinja2==2.7.1\n')
        f.write('Mako==1.0.1\n')
        f.write('MarkupSafe==0.23\n')
        f.write('SQLAlchemy==1.0.6\n')
        f.write('Werkzeug==0.10.4\n')
        f.write('wheel==0.24.0\n')
        f.write('WTForms==1.0.5\n')
        f.close()
        print('File Created ' + os.path.join(directory, 'requirements.txt'))
        
        f = open(os.path.join(project_directory, init_file), 'w')
        f.write('from flask import Flask\n')
        f.write('app = Flask(__name__)\n')
        f.write('\n')
        f.write('@app.route(\'/\')\n')
        f.write('def hello_world():\n')
        f.write('   return \'Hello World!\' ')
        f.close()
        print('File Created ' + os.path.join(project_directory, init_file))
        
        f = open(os.path.join(project_directory, models, init_file), 'w')
        f.close()
        print('File Created ' + os.path.join(project_directory, models, init_file))
        
        f = open(os.path.join(project_directory, views, init_file), 'w')
        f.close()
        print('File Created ' + os.path.join(project_directory, views, init_file))
        
        f = open(os.path.join(project_directory, tests, init_file), 'w')
        f.close()
        print('File Created ' + os.path.join(project_directory, tests, init_file))
        
    except OSError as exception:            
        print(exception) 

parser = optparse.OptionParser()

parser.add_option('-d', '--dir')
parser.add_option('-p', '--projectname')

options, args = parser.parse_args()

directory = options.dir
project_name = options.projectname

setup(directory, project_name)
