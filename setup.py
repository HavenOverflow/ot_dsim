from setuptools import setup

setup(
    name='ot_dsim',
    version='0.1.3',
    packages=['ot_dsim', 'ot_dsim.bignum_lib'],
    package_dir={'ot_dsim': '.'},
    install_requires=[
        'pycryptodome',
        'tabulate',
    ],
    build_with_nuitka=True,
)
