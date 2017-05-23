try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Clone of tank game shell shock',
    'author': 'Mohamed Lansari',
    'url': 'lol',
    'download_url': 'lol',
    'author_email': 'mohamed.ml.me@gmail.com',
    'version': '0.1',
    'install_requires': ['pygame'],
    'packages': ['ShellShockClone'],
    'scripts': [],
    'name': 'Shell Shock Clone'
}

setup(**config)