import sys, os

INTERP = "/home/seedch/venvSeedCorp/bin/python3.9"
#INTERP is present twice so that the new python interpreter 
#knows the actual executable path 
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/pisosarquitectonicos')  #You must add your project here

sys.path.insert(0,'/home/siamco/envSiamco/bin')
sys.path.insert(0,cwd+'/home/siamco/envSiamco/lib/python3.9/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "pisosarquitectonicos.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

