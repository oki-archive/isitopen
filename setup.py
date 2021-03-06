try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys
sys.path.insert(0, '.')

from isitopen import __version__, __description__, __long_description__, __license__


setup(
    name='isitopen',
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    license=__license__,
    author='Rufus Pollock (Open Knowledge Foundation)',
    author_email='',
    url='http://isitopen.ckan.net/',
    install_requires=[
        'WebOb<=1.0.1',
        'Pylons>=0.9.7,<0.9.8',
        # TODO: minor issues with routes >= 1.12
        'Routes<=1.11.99',
        'SQLAlchemy>=0.5,<0.5.99',
        'Genshi>=0.6',
        'FormAlchemy>=1.0',
        # last version to work with SQLA < 0.5
        'sqlalchemy-migrate>=0.5,<0.5.99',
        # for mail tests
        # 'processing',
        'repoze.who<1.99',
        # for web app deployment
        'PasteDeploy',
        ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'isitopen': ['i18n/*/LC_MESSAGES/*.mo']},
    message_extractors = {'isitopen': [
            ('**.py', 'python', None),
            ('templates/**.html', 'genshi', None),
            ('public/**', 'ignore', None)]},
    paster_plugins=[
        'Pylons',
        'WebHelpers',
        'PasteScript',
        ],
    entry_points="""
    [paste.app_factory]
    main = isitopen.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [paste.paster_command]
    db = isitopen.lib.cli:ManageDb
    fixtures = isitopen.lib.cli:Fixtures
    """,
)
