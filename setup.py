# This file is part of django-popularity.
#
# django-popularity: A generic view- and popularity tracking pluggable for Django.
# Copyright (C) 2008-2010 Mathijs de Bruin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

try:
    README = open('README.rst').read()
except:
    README = None

setup(
    name = 'django-popularity',
    version = "0.1.7",
    description = 'A generic view- and popularity tracking pluggable for Django.',
    long_description = README,
    author = 'Mathijs de Bruin',
    author_email = 'drbob@dokterbob.net',
    url = 'http://github.com/dokterbob/django-popularity',
    packages = ['popularity', 'popularity.templatetags',],
    include_package_data = True,
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
