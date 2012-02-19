from setuptools import setup
if __name__=='__main__':
    setup(
        name='reprtools',
        description="utilities for nice object reprs",
        py_modules=[
            'reprtools',
        ],
        get_version_from_hg=True,
        setup_requires=[
            'hgdistver',
        ],
    )
