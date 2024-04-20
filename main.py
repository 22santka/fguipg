from requirementscheck import testRequirements # Imported class from another file
        
def main():
    from maintkinterwindow import MainTkinterWindowSetup # Imported class from another file
    MainTkinterWindowSetup.mainWindow(MainTkinterWindowSetup)

if __name__ == "__main__":
    testRequirements.doRequirementsTest(testRequirements())
    main()