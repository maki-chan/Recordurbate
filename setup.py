#!/usr/bin/env python

from distutils.core import setup

setup(name='Recordurbate',
      version='1.2.0',
      description='A Bot to automatically record Chaturbate live streams',
      author='Michael Armbruster',
      author_email='michael@armbrust.me',
      url='https://github.com/maki-chan/Recordurbate',
      license='GPL-3.0',
      packages=['recordurbate'],
      package_dir={'recordurbate': 'src'},
      package_data={'reordurbate': ['configs/youtube-dl.config', 'configs/config.json']},
      scripts=['bin/recordurbate'],
     )
