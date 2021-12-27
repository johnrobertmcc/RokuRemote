from setuptools import setup, find_packages

setup(
    name="Roku by JR",
    entry_points={
        'console_scripts': ['roku=remote.main:main'],
    },
    description='Roku Remote for Linux. Might work with other OS. Unsure. Let me know tho please :raised_hands:',
    author='J.R. McCann',
    version='1.0',
    author_email='john.robert.mcc@gmail.com',
    install_requires=[],
)
