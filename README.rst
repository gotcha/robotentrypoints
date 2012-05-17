Entry points for Robot Framework
================================

`Robot framework`_ does not have setuptools_ compatible entry points.
This makes it hard to setup Robot with buildout_.

``robotentrypoints`` provides them.

.. _Robot framework: http://pypi.python.org/pypi/robotframework
.. _setuptools: http://pypi.python.org/pypi/setuptools
.. _buildout: http://pypi.python.org/pypi/zc.buildout

With the buildout hereunder, you get 
``bin/pybot`` and ``bin/rebot`` scripts.

::

    [buildout]
    parts = robot
    versions = versions

    [robot]
    recipe = zc.recipe.egg
    eggs = robotsetup

    [versions]
    robotframework = 2.7
