from setuptools import setup, Command
import os

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vr ./build ./*.pyc ./*.tgz ./*.egg-info ./Generated_opcodes.py ')

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='ropgenerator',
      version='0.3.2',
      description='ROPGenerator makes ROP exploits easy by finding and chaining gadgets',
      url='https://github.com/Boyan-MILANOV/ropgenerator',
      author='Boyan MILANOV',
      author_email='boyan.milanov@hotmail.fr',
      license='GPLv3',
      classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.7',
      'Topic :: Security',	
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      ],
      packages=['ropgenerator'],
      scripts=['ROPGenerator'],
      install_requires=['ROPGadget', 'prompt_toolkit', 'z3-solver', 'barf==0.4.0', 'enum', 'capstone==3.0.5rc2'],   
      dependency_links=['https://github.com/Z3Prover/z3/tree/master/src/api/python'],
      keywords='ROP generator chain gadget semantic automatic exploit ropchain',  
      zip_safe=False, 
      cmdclass={
        'clean': CleanCommand,
      }
      
    )
      
     
