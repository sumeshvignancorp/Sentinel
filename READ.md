Here are the steps to download and run the script :

1. Download & Install Python : Install Python on your system if it's not already installed.
   
2. Download PyCharm :
   Visit [PyCharm Community Edition Download](https://www.jetbrains.com/pycharm/download/?section=windows) and download PyCharm (Community Edition only).

3. Install PyCharm :
   Install PyCharm Community Edition by selecting the default settings during the installation process.

4. Open the Project :
   Open the "Sentinel" project in PyCharm. At the bottom of the window, ensure the Python interpreter is set to Python. If not, click on "Python 3.12" or add a new interpreter.(You can see this at bottom right side as Python 3.12 click on it & set)

5. Add Required Packages :
   - Go to Main Menu -> Settings -> Project: Sentinel -> Python Interpreter.
   - Click on the "Plus" icon and search for the following packages: PIP, Selenium, webdriver-manager, Pytest, Pytest-html, allure-pytest -  Install them.

6. Run project in Existing browser :
   - Go to Chrome Application path in C drive - C:\Program Files\Google\Chrome\Application
   - Create a new folder in D-Drive or any as "Pytest"
   - Find path of our Chrome browser profile path in C-Drive or Enter this in Chrome browser "chrome://version/" - (You will get chrome profile path)
   - as C:\Users\sumes\AppData\Local\Google\Chrome\User Data\Profile 1 - This path is from system
   - Copy the Profile 1 folder or default file path & Paste it in Created folder "pytest"
  Note -> chrome://version/ by entering this into Chrome you will get Chrome profile path and version

7. Open Command prompt to start the Chrome browser in Existing profile :
   - Step 1 > cd C:\Program Files\Google\Chrome\Application
   - Step > chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\pytest\Profile 2"
   Note - After opening browser login with Sentinel credentials & Don't close opened browser.

8. Run the Tests :
   To run the tests, use any of the following methods:
   - Right-click on the "smoke_testcase" directory and select Run. 
   - Alternatively, right-click on the "smoke_testcase" package, open Terminal, and type any of the following commands:  
     - "pytest -v -s"
     - "pytest"
     - "pytest -v"

9. Generate an HTML Report :
   To generate a test report, right-click on the "smoke_testcase" directory, open Terminal, and type:  
   "pytest --html=report.html".  
   After the execution, a file named "report.html" will appear in the project directory.

10. Generate an Allure report()
    Step 1 - Enter this in Terminal - pip install allure-pytest
    Step 2 - Download Zip file of Allure-2.32.2.zip - https://github.com/allure-framework/allure2/releases/tag/2.32.2
    Step 3 - To Environment variables - System variables - In Path set your extracted files path till bin
    In Terminal > To generate allure report >> pytest --alluredir=allure-results
    After running the above commands wait till execution completion and Run this command to view report >> allure serve allure-results - It will generate allure report

11. Run Device Script :
    Before running the smoke_testcase, execute the Device1.py script to generate the necessary reports.

Note -
1. While running script don't use any browser because scripts will fail

Login Credentials 
Email - sumeshhiremath13@gmail.com
Password - Ajnaview@31
