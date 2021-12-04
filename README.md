# Human face recognition from live video using open-cv

## Developer Installation Guide (Windows)

## Prerequisites

- Python 3
- pip 3


## Install

## Virtual Environment

1.  Following command will install python virtual environment library globally.\
    > `python -m pip install virtualenv`

2.  Following command will create virtual environment directory named venv in your projects.\
    > `python -m virtualenv venv`

3.  Following command will activate the virtual environment for your project. \
    >  `.\venv\Scripts\activate`

    After this steps, `(venv)` should be appier at the begning of terninal line, like below which 
    confirms virtual environment is successfully activated. \

### Python Libraries
1.  Upgrade pip\
    (venv) ... > `python -m pip install --upgrade pip`
2.  Following command will install all the library requires for this project in the virtual environment.\
    (venv) ... > `python -m pip install -e .`
3. Redirect to file location
    (venv) ... > `cd .\src\human_face_recognition_app.egg-info\`
4. to run the file and detect human on live cam
    (venv) ... > `python face_detection.py`
5. To terminare the live video
    press `q` for terminate


