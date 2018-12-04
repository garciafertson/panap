from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

exec(open('panapp/version.py').read()) # loads __version__

setup(name='panap-panBGCnaturalproducts',
      version=__version__,
      author='fernando garcia-guevara',
      description='panap let you make pan genomic analysis on BGC of natural products',
      long_description=readme,
      license='GPL3+',
      keywords="",
      packages=find_packages(exclude='docs'),
      install_requires=('biopython >=1.64'),
      #setup_requires=['nose>=1.0'],
      #test_suite='nose.collector',
      url='https://github.com/garciafertson/panap',
      scripts=['bin/panapp.py'],
      #data_files=[
      #    ('share', ['share/18S.hmm']),
      #],
)
