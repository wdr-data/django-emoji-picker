import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-emoji-picker',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django Widgets text inputs and textareas with emoji picker',
    url='https://github.com/wdr-data/django-emoji-picker',
    author='Hacking Studio',
    author_email='hello@hacking.studio',
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