from setuptools import setup, find_packages


LONGDESCRIPTION = """
# Database Handler for all AtomicByte projects! 
-----
#### (https://github.com/Atom1cByte)[https://github.com/Atom1cByte]
"""

VERSION = "0.0.1"
DESCRIPTION = "Database Handler"

# Setting up
setup(
    name="db_handler",
    version=VERSION,
    author="AtomicByte",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONGDESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "prisma @ git+https://github.com/RobertCraigie/prisma-client-py@e8dc4ebe44e080a59e4381e02997540bcd3f193c"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)