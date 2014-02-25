from distutils.core import setup
from distutils.extension import Extension

setup(name="darkcoin_subsidys",
    ext_modules=[
        Extension("darkcoin_subsidy", ["darckcoin_GetBlockBaseValue.cpp"],
        libraries = ["boost_python"])
    ])
