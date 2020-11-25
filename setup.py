from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readmeText = f.read()

with open('LICENSE', encoding='utf-8') as f:
    licenseText = f.read()

setup(
    name='net-speed-checker',
    version='0.3',
    author='Radu Petre',
    author_email='Spam@Petre.dev',
    description='Package taking measurements for internet speed.',
    long_description=readmeText,
    long_description_content_type='text/markdown',
    url='https://github.com/radupetre/net-speed-checker',
    download_url='https://github.com/radupetre/net-speed-checker/archive/v0.2.tar.gz',
    license='MIT License',
    packages=find_packages(exclude=('test', 'tests', 'docs')),
    keywords=['SPEEDTEST', 'SPEEDCHECKER', 'SPEED', 'TEST', 'CHECKER'],
    classifiers=[
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
    install_requires=[
      'speedtest-cli',
      'mysql-connector-python',
      'SQLAlchemy',
      'mysqlclient',
    ],
    python_requires='>=3.6',
)