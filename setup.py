from setuptools import setup, find_packages

with open('README.md') as f:
    readmeText = f.read()

with open('LICENSE') as f:
    licenseText = f.read()

setup(
    name='net-speed-checker',
    version='0.2',
    author='Radu Petre',
    author_email='Spam@Petre.com',
    description='Package taking measurements for internet speed.',
    long_description=readmeText,
    long_description_content_type="text/markdown",
    url='https://github.com/radupetre/net-speed-checker',
    license=licenseText,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
    install_requires=[
      'speedtest-cli',
      'mysql-connector-python',
      'SQLAlchemy',
    ],
    python_requires='>=3.6',
)