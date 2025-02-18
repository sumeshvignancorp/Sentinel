Here are the steps to download and run the script :

1. Download & Install Python : Install Python on your system if it's not already installed.
   
2. Download PyCharm :  
   Visit [PyCharm Community Edition Download](https://www.jetbrains.com/pycharm/download/?section=windows) and download PyCharm (Community Edition only).

3. Install PyCharm :  
   Install PyCharm Community Edition by selecting the default settings during the installation process.

4. Open the Project :  
   Open the "OnTrack_server" project in PyCharm. At the bottom of the window, ensure the Python interpreter is set to Python. If not, click on "Python 3.12" or add a new interpreter.

5. Add Required Packages :  
   - Go to Main Menu -> Settings -> Project: OnTrack_server** -> Python Interpreter.
   - Click on the "Plus" icon and search for the following packages: PIP, Selenium, webdriver-manager, Pytest, Pytest-html -  Install them.

6. Run the Tests :  
   To run the tests, use any of the following methods:
   - Right-click on the "Smoke_testcase" directory and select Run.
   - Alternatively, right-click on the Smoke_testcase package, open Terminal, and type any of the following commands:  
     - "pytest -v -s"
     - "pytest"
     - "pytest -v"

7.  Generate a Report :  
   To generate a test report, right-click on the Smoke_testcase directory, open Terminal, and type:  
   "pytest --html=report.html".  
   After the execution, a file named "report.html" will appear in the project directory.

8. Run Device Script :  
   Before running the Smoke_testcase, execute the Device1.py script to generate the necessary reports.

9. Important Note :  
   This project is specifically designed for the OnTrack server at 'pg.ajnaview.net'. It will not function with other builds.

10. Take Screenshots :  
    To capture screenshots, right-click on the 1Login_Reset directory and select Run. Repeat the process for other directories like 2Settings and 3Reports. Check the Results&Status folder for the images.