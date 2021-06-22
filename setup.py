from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and (not line.startswith("#") and not line.startswith("-"))]


_REPO_URL = 'https://github.com/michael-sobczak/rpi-os-tools'

_LONG_DESCRIPTION = open('README.md', 'r').read()

setup(
    name='rpios_tools',
    version='0.2.1',
    url=_REPO_URL,
    download_url='',
    license='MIT',
    author='Michael Sobczak',
    author_email='86268116+michael-sobczak@users.noreply.github.com',
    description='Automated tools for working with raspberry pi image development',
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['rpios_tools'],
    keywords=['raspberry pi', 'raspbian', 'iot', 'rpi'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points = {
        'console_scripts': ['rpios-dl=rpios_tools.download:main'],
    }
)