from setuptools import setup

setup(
    name='vcolorpicker',
    version='1.4.1',
    description='Open a visual vcolorpicker from any project.',
    long_description='Open a visual vcolorpicker from any project.\nFor more info visit '
                     'https://github.com/nlfmt/pyqt-colorpicker',
    url='https://github.com/ae92736/pyside-colorpicker',
    author='nlfmt',
    author_email='nlfmt@gmx.de',
    license='MIT',
    packages=['vcolorpicker'],
    install_requires=['PySide2'],
    keywords=["python", "color", "gui", "colorpicker", "visual"],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
