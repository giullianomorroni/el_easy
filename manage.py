#!/usr/bin/env python
import os
import sys

#production
sys.path.append('/var/www/el_easy/el_easy')
sys.path.append('/var/www/el_easy/')
#desenv
sys.path.append('/Development/el_easy/')
sys.path.append('/Development/el_easy/el_easy/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "el_easy.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
