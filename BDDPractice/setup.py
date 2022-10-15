# from distutils.core import setup
from setuptools import setup, find_packages
setup(name='BDDPractice',
      version='1.0',
      description='Python BDD Practical Examples',
      author='Pradnyan Bhilare',
      author_email='pradnyanbhilare@gmail.com',
      url='https://www.supersqa.com/',
      # packages=[
      #       'BDDCommon',
      #       'BDDCommon.CommonFuncs',
      #       'BDDCommon.CommonSteps',
      #       'BDDCommon.CommonConfigs'
      # ],
      packages=find_packages()
     )

