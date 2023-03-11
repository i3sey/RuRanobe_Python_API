from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='RuRanobe_Python_API',
  version='1.0.0',
  author='i3sey',
  author_email='deniskedrovsky1@gmail.com',
  description='Requests-powered API for RuRanobe',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/i3sey/RuRanobe_Python_API',
  packages=find_packages(),
  install_requires=['requests>=2.28.2', 'beautifulsoup4>=4.11.2', 'lxml>=4.9.2'],
  classifiers=[
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='api ranobe ruranobe requests python',
  python_requires='>=3.10'
)