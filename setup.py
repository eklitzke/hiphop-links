from setuptools import setup, find_packages


setup(name='hiphop',
      version='1.0',
      author='Evan Klitzke',
      author_email='evan@eklitzke.org',
      description='my blog',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'hiphop-generate = hiphop.hiphop:main'
          ]})
