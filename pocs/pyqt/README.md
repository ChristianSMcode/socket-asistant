USAGE:
Create a virtual env on the root of the project called QT, activate it and the install the requirements found
inside the etc folder called QT_REQS.txt

This is just a tool to create UIs easy and fast.
Run 'pyqt5-tools designer' to open an aplication and easily create or modify an app (optionally you can go to python folder installation
and execute designer app under pyqt5-tools library)

Use 'pyuic5' to compile files created from the pyqt designer app into python code
Example:pyuic5 -x .\pocs\pyqt\basicSocketUi.ui -o qt_designer_compiled.py

CONSIDERATIONS:
This might work only in windows since it is where it was designed tho to use it in other OS it would require minimal
changes (graphical changes since pyqt is crossplatform)

References:
https://www.pythonguis.com/installation/install-qt-designer-standalone/
https://www.youtube.com/watch?v=Vde5SH8e1OQ&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj