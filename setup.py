from setuptools import setup

setup(name="cwlmodel",
      version="0.1",
      url='https://github.com/common-workflow-language/python-cwlmodel',
      install_requires=['jinja2', 'pyyaml', 'schema-salad'],
      entry_points={
          'console_scripts': [
              'cwl-sdk = sdk_generation.cwl_sdk_cli:generate_sdk'
          ]
      },
      packages=[
          'sdk_generation',
          'templates'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
      ],
      include_package_data=True,
      )
