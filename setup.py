from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

# Read the contents of your requirements.txt file
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='SimplePythonProjectStarter',
    version='0.1.0',
    packages=find_packages(),  # Automatically discover all packages and subpackages
    install_requires = get_requirements('requirements.txt'),  # Specify dependencies from requirements.txt
    # entry_points={  # If your project has any command-line interfaces
    #     'console_scripts': [
    #         'your_command_name = your_package.module:function_name',
    #     ],
    # },
    # Metadata
    author='Panos Zafeiropoulos',
    author_email='zzpzaf.se@gmail.com',
    description='Short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zzpzaf-se/SimplePythonProjectStarter1',
    license='MIT',  # License type
    classifiers=[  # Additional metadata
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12.3',
    ],
)