from setuptools import setup, find_packages

config = {
    'name':'script2package',
    'version': '1.0.2',
    'entry_points':{
        'console_scripts':['script2package=script2package.cli:main']
    },
    'packages':find_packages()
}

setup(**config)
