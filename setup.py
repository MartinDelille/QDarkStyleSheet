#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) <2013-2014> <Colin Duquesnoy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""
QDarkStyle is a darks stylesheet for python qt applications
"""
from setuptools import setup, find_packages

setup(
    name='QDarkStyle',
    version='1.0.1',
    packages=find_packages(),
    package_data={'qdarkstyle': ["*.qss", "*.qrc", "rc/*.png"]},
    url='https://github.com/ColinDuquesnoy/QDarkStyleSheet',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A dark stylesheet for pyside/pyqt applications',
    long_description="""
    This package provides a dark style sheet for PySide/PyQt applications.
    All you have to do is the following::

        import qdarkstyle
        QtGui.QApplication().instance().setStyleSheet(qdarkstyle.load_stylesheet())
    """,
)
