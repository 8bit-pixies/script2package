import os
from os.path import basename, splitext
from shutil import copyfile

def generate_skeleton(script=None, base="package", config={}, setup_cfg=None):
    """Generates a package skeleton within current working directory.

    :param script: file path to the script of interest
    :param base: name of the base folder for package generation
    :param config: setuptools configuration
    :param setup_cfg: path to the setup.cfg file
    :return: this function returns nothing
    """
    if script is None:
        print("Script file must be provided within `generate_skeleton`!")
        raise

    base_script = basename(script)
    name, ext = splitext(base_script)
    if not ext.endswith("py"):
        print("Script file %s does not appear to be a python script!" % script)
        raise

    config['name'] = config.get('name', name)
    config['version'] = config.get('version', '1.0.0')

    # create folder layout
    os.makedirs('{base}/{name}'.format(base=base, name=name))

    # create the setup.py
    with open('{base}/setup.py'.format(base=base), 'w') as f:
        setup_py = """from setuptools import setup

config = {config}

setup(**config)""".format(config=config)
        f.write(setup_py)

    # copy setup_cfg if applicable
    if setup_cfg is not None:
        if os.path.isfile(setup_cfg):
            copyfile(setup_cfg, '{base}/setup.cfg')
        else:
            print("setup.cfg is not a valid file")
            raise

    # create __init__.py
    with open('{base}/{name}/__init__.py'.format(base=base, name=name), 'w') as f:
        f.write("""{script}""".format(script=open(script, 'r').read()))
