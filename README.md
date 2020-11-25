# Montana Exhibitions

Static site generator for our iPad exhibitions

## Usage

(Optional) Setup virtualenv
```bash
sudo apt install python3-venv python3-pip python3-dev
python3 -m venv .venv
source .venv/bin/activate
# pip3 install commands below
deactivate
```

Setup
```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt # or pip3 install Jinja2
```

Running
```bash
python3 src/main.py --csv test.csv
```

Viewing
```bash
python3 -m http.server
```
Now visit http://localhost:8000/output

Clear output folder
```bash
rm -rf output/*
```