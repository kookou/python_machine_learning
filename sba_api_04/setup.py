import setuptools


with open("README.md" , "r") as fh:
    long_description = fh.read()


setuptools.setup(
      name='com_bita',
      version='1.0',
      description='Python Distribution Utilities',
      author='parkhyejung',
      author_email='nnaangee@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=setuptools.find_packages(),
     )