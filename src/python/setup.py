#!/usr/bin/env python

from distutils.core import setup

setup(name='ESxSNMP',
        version='0.9a1',
        description='ESnet eXtensible SNMP system.',
        author='Jon M. Dugan',
        author_email='jdugan@es.net',
        url='http://code.google.com/p/esxsnmp/',
        packages=['esxsnmp'],
        install_requires=['tsdb', 'SQLAlchemy==0.5.2', 'web.py'],
        entry_points = {
            'console_scripts': [
                'espolld = esxsnmp.poll:espolld',
                'espoll = esxsnmp.poll:espoll',
                'esdbd = esxsnmp.db:esdbd',
                'espersistd = esxsnmp.persist:espersistd',
                'esfetch = esxsnmp.fetch:esfetch',
                'esnewdb = esxsnmp.newdb:esdb_standalone',
                'gen_ma_storefile = esxsnmp.perfsonar:gen_ma_storefile_http',
            ]
        }
    )
