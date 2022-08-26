## Installing 

Create virtual environment
```bash
python -m venv venv
```

Activate virtual environment
```bash
source venv\bin\activate
```

Install Deps
```bash
pip install -r requirements.txt
```


## Usage
Create config.ini file and fill it
```bash
cp config.example.ini config.ini
```


## Parse "Following" list
First time program has been executed, it'll parse list of a pages and profiles you are following. Python will create 'links.txt' which are supposed to be unfollowd at second execution of exact sime statement 

```bash
python main.py
```




