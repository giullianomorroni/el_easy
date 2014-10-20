import os
import sys
import django.core.handlers.wsgi

#if path not in sys.path:
sys.path.append('/var/www/el_easy/el_easy/')
sys.path.append('/var/www/el_easy/')

os.environ['DJANGO_SETTINGS_MODULE'] 	= 'settings'
os.environ["EL_EASY"] 	             	= "/var/www/el_easy/el_easy"
os.environ["EL_EASY_IMG"] 		        = "/var/www/static/el_easy"

application = django.core.handlers.wsgi.WSGIHandler()
