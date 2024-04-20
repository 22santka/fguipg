from maintkinterwindow import MainTkinterWindowSetup # Imported class from another file
from requirementscheck import testRequirements # Imported class from another file
import os
        
def main():
    MainTkinterWindowSetup.mainWindow(MainTkinterWindowSetup)

if __name__ == "__main__":
    testRequirements.doRequirementsTest(testRequirements())
    main()