try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'The program walks through a folder tree and seeks files with certain file extensions (i.e. pdf, jpg).  It then copies these files from where they are in to a new folder.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['os,re'],
	'scripts': [],
	'name': 'Selective File Copy'
}

setup(**config)