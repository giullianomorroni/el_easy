import os
import sys
import django.core.handlers.wsgi

#path = '/var/www/casacomigo/new_commerce/new_commerce/'
#if path not in sys.path:
sys.path.append('/var/www/el_easy/el_easy')
sys.path.append('/var/www/el_easy/')

os.environ['DJANGO_SETTINGS_MODULE'] 	= 'settings'
os.environ["CASA_COMIGO"] 		= "/var/www/el_easy/el_easy"
os.environ["CASA_COMIGO_IMG"] 		= "/var/www/static/el_easy"

application = django.core.handlers.wsgi.WSGIHandler()
