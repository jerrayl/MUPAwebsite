# MUPAwebsite Development setup

1. Download Python 3 from https://www.python.org/ and install, making sure to add python to PATH
2. Download an IDE (VS Code is recommended)
3. Download google cloud sdk
4. Clone/Download this repository 
5. In command prompt, navigate to the location of the website source files
6. Set credentials with ```set GOOGLE_APPLICATION_CREDENTIALS=MUPAwebsite-9653fbff31db.json```
7. To test locally, run ```python main.py``` in the console
8. Login with ```gcloud auth login```
9. Set project with  ```gcloud config set project mupawebsite```
10. Deploy project with ```gcloud app deploy```
