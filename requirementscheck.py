import unittest
from pathlib import Path
import pkg_resources

_REQUIREMENTS_PATH = Path(__file__).parent.with_name("requirements.txt")

def doRequirementsTest(self):
    requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
    
    # Use a loop to check and download each requirement in the requirements.txt file, using a subtest for each one independantly
    for requirement in requirements:
        requirement = str(requirement)
        print(requirement)
        with self.subTest(requirement=requirement):
            pkg_resources.require(requirement)
            print(requirement)