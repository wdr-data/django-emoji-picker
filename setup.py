import os
from setuptools import find_packages, setup

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requirements = [str(r.req) for r in
                parse_requirements('requirements.txt', session=False)]

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='django-emoji-picker',
    version='0.0.6',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    license='MIT License',
    description='Django app providing text input and textarea widgets with emoji picker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wdr-data/django-emoji-picker',
    author='Hacking Studio',
    author_email='hello@hacking.studio',
    keywords='django emoji widget',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_data={
        'emoji_picker': [
            'templates/emoji_picker/*.html',
            'static/emoji_picker/*.js',
            'static/emoji_picker/*.css',
            'static/emoji_picker/*.map'
        ],
    },
)