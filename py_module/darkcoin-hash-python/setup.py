from distutils.core import setup, Extension

dark_hash_module = Extension('dark_hash',
                               sources = ['darkmodule.c',
                                          'dark.c',
					  'sha3/blake.c',
					  'sha3/bmw.c',
					  'sha3/groestl.c',
					  'sha3/jh.c',
					  'sha3/keccak.c',
                                          'sha3/skein.c',
                                          'sha3/simd.c',
                                          'sha3/luffa.c',
                                          'sha3/shavite.c',
                                          'sha3/echo.c',
                                          'sha3/cubehash.c',
                                          'sha3/aes_helper.c'
                                          ],
                               include_dirs=['.', './sha3'])

setup (name = 'dark_hashs',
       version = '1.0',
       description = 'Bindings for scrypt proof of work used by Quarkcoin',
       ext_modules = [dark_hash_module])
