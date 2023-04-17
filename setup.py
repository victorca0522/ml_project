## Setup.py is centre of all activity in building, distributing, and installing modules using the Distutils. 
## It is intended to create my machine learning application as a package. 

from setuptools import find_packages, setup 
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements
    

setup (
    name = 'mlproject',
    version = '0.0.1',
    author = 'Victor Mao',
    author_email = 'Zhesi.Mao@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)