"""
WSGI config for chat_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project directory to the Python path
path = '/home/Karan137/90North-assignment/chat_project'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'chat_project.chat_project.settings'

# Manually activate the virtual environment
activate_env = '/home/Karan137/90North-assignment/chat_project/myenv/bin/activate_this.py'
if os.path.exists(activate_env):
    with open(activate_env) as f:
        exec(f.read(), {'__file__': activate_env})
else:
    # Fallback: Add the virtual environment's site-packages to the Python path
    venv_path = '/home/Karan137/90North-assignment/chat_project/myenv'
    site_packages = os.path.join(venv_path, 'lib', f'python{sys.version_info.major}.{sys.version_info.minor}', 'site-packages')
    sys.path.insert(0, site_packages)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

application = get_wsgi_application()
