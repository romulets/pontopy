from setuptools import setup

setup(name='pontopy',
      packages=['pontopy'],
      entry_points={
          'console_scripts': ['pontopy = pontopy.__main__:main']
      },
      version='1.0.0',
      description='Aplicação em linha de comando em Python para registrar o ponto',
      author='Juliano Rodrigues da Silva',
      author_email='julianorodrigues@outlook.com',
      install_requires=[
            'requests'
      ])
