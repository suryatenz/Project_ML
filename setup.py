from setuptools import find_packages, setup
from typing import List


H_e='-e .'
def get_requiremnts(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","")for req in requirments]
        if H_e in requirments:
            requirments.remove(H_e)
    return requirments

setup(
    name='project',
    version='0.1',
    author='Surya',
    author_email='sprajyesh@gmail.com',
    packages=find_packages(),
    install_requiremnts=get_requiremnts('requirements.txt')
)