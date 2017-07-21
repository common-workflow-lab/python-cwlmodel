from setuptools import setup

setup(name="python-cwlmodel",
      version="0.1",
      url='https://github.com/common-workflow-language/python-cwlmodel',
      install_requires=['jinja2', 'pyyaml'],
      entry_points={
          'console_scripts': [
              'cwl-sdk = sdk-generation.cwl_sdk_cli:generate_sdk'
          ]
      },
      packages=[],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
      ],
      include_package_data=True,
      )
