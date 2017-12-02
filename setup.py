from setuptools import setup, find_packages

setup(name='WorkshopExample',
      version='0.0.1',
      description='Random example project for coding workshop',
      url='http://github.com/mattcraigie/WorkshopExample',
      author='Matt Craigie',
      author_email='matthewcraigie1@gmail.com',
      license='MIT',
      install_requires=['numpy'],
      packages=find_packages(exclude=('tests', 'doc', 'data'))
      )
