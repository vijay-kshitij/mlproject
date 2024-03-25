# to make my ML Application into a package so it can be used elsewhere too

from setuptools import find_packages, setup
from typing import List

#find_packages() will find the folders which have the file '__init__.py' and 
#treat that folder as a package and that can be imported like python libraries

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #reading the lines from the requirements.txt file
        requirements = [req.replace("\n", "") for req in requirements] #replacing the \n with blank space

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Kshitij',
author_email = 'vijayvergiya.kshitij98@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)