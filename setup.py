from setuptools import setup, find_packages

version = '0.1'

long_description = (file('README.rst').read() +
    '\n\n' + file('HISTORY.txt').read())

SCRIPT_NAMES = ['pybot', 'rebot']

console_scripts = ["%s = robotentrypoints.scripts:%s" % (script, script)
        for script in SCRIPT_NAMES]
entry_points = dict(console_scripts=console_scripts)

setup(name='robotentrypoints',
      version=version,
      description="Entry points for Robot Framework",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Godefroid Chapelle',
      author_email='gotcha@bubblenet.be',
      url='https://github.com/gotcha/robotentrypoints',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'robotframework >= 2.7',
      ],
      entry_points=entry_points
      )
