import setuptools


def _get_file_content(filename) -> str:
    try:
        with open(filename, 'r') as fh:
            content = str(fh.read())
            fh.close()
    except OSError:
        raise FileNotFoundError('Required file {} not found'.format(filename))

    return content


setuptools.setup(
    name='trading-app',
    version='0.0.1',
    author='Paul Horton',
    author_email='simplyecommerce@gmail.com',
    description='Client/Server Trades Application',
    long_description=_get_file_content('README.md'),
    long_description_content_type='text/markdown',
    url='https://TBC',
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    license=_get_file_content('LICENSE'),
    install_requires=_get_file_content('requirements.txt'),
    data_files=[('', ['LICENSE', 'README.md', 'requirements.txt'])]
)
