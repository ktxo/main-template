from os.path import abspath, dirname, join
import setuptools

aboutpath = join(abspath(dirname(__file__)),'ktxo','app', '_about.py')
_about = {}
with open(aboutpath) as fp:
    exec(fp.read(), _about)

setuptools.setup(
    name=_about["__name__"],
    version=_about["__version__"],
    author=_about["__author__"],
    author_email=_about["__author_email__"],
    description=_about["__description_message__"],
    url=_about["__url__"],
    entry_points={'console_scripts': ['main_template = ktxo.app.main_template:main']},
    include_package_data=True,
    license=_about['__license__'],
    packages=setuptools.find_packages(include=['ktxo.*']),
    python_requires='>=3.7',
    install_requires=[],
    classifiers=['Programming Language :: Python :: 3.7'],
    keywords='app template'
)
