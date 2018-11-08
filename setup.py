from setuptools import find_packages
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='usard-fido',
      version='0.0.1',
      description='Python application for ordering and downloading USARD (tiled) scenes',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.6',
      ],

      # """
         # Development Status :: 1 - Planning
         # Development Status :: 2 - Pre-Alpha
         # Development Status :: 3 - Alpha
         # Development Status :: 4 - Beta
         # Development Status :: 5 - Production/Stable
         # Development Status :: 6 - Mature
         # Development Status :: 7 - Inactive
      # """

      keywords='usgs lcmap eros',
      url='http://github.com/tonybutzer/usard-fido',
      author='Tony Butzer',
      author_email='tonybutzer@gmail.com',
      license='Unlicense',
      packages=find_packages(),
      install_requires=[
          'numpy',
      ],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[test]
      extras_require={
          'test': ['pytest',
                  ],
          'doc': ['sphinx',
                  'sphinx-autobuild',
                  'sphinx_rtd_theme'],
          'dev': ['jupyter', 'readline'],
      },
      # entry_points={
          #'console_scripts': [''],
      # },
      include_package_data=True,
      zip_safe=False)
