# This file was auto-generated by Shut. DO NOT EDIT
# For more information about Shut, check out https://pypi.org/project/shut/

from __future__ import print_function
import io
import os
import setuptools
import sys

readme_file = 'README.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = [
  'scapy[basic]',
  'psutil',
  'ouilookup',
]

setuptools.setup(
  name = 'arpwitch',
  version = '0.3.5',
  author = 'Nicholas de Jong',
  author_email = 'contact@nicholasdejong.com',
  description = 'A modern arpwatch replacement with JSON formatted outputs and easy options to exec commands when network changes are observed.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://arpwitch.readthedocs.io/',
  license = 'BSD2',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'tests', 'tests.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = {},
  tests_require = [],
  python_requires = '>=3.6.0,<4.0.0',
  data_files = [],
  entry_points = {
    'console_scripts': [
      'arpwitch = arpwitch.cli.entrypoints:arpwitch',
    ]
  },
  cmdclass = {},
  keywords = ['arpwitch', 'arpwatch', 'arp', 'network', 'security'],
  classifiers = ['Environment :: Console', 'Intended Audience :: System Administrators', 'Intended Audience :: Information Technology', 'Topic :: System :: Networking :: Monitoring', 'Programming Language :: Python :: 3', 'License :: OSI Approved :: BSD License'],
  zip_safe = True,
)
