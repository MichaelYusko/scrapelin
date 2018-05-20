from importlib.machinery import SourceFileLoader as load_source
from os import path

VERSION = load_source('version', path.join('.', 'scrapelin', 'version.py')).load_module()
VERSION = VERSION.__version__
