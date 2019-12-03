# IK-AUTOFILL
a tiny script to fill [https://www.ikco.ir](https://www.ikco.ir/fa/) forms automatically using `python` and `selenium`.

## installation

### requirements
- [virtualenv](https://github.com/pypa/virtualenv)
- [urllib3](https://github.com/urllib3/urllib3)
- [selenium](https://github.com/SeleniumHQ/selenium)
- A web driver such as [chrome driver](https://chromedriver.chromium.org/downloads)

### install
```
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

**NOTE**: edit config.py file and put your webdriver path on it.

## usage
```
$ python ikautofill.py [sample_file.json]
```

## maintainer
- [@amiremohamadi](https://github.com/amiremohamadi)
