# Montana Exhibitions

Static site generator for our iPad exhibitions

## Usage

Setup virtualenv
```bash
sudo apt install python3-venv python3-pip python3-dev
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
deactivate
```

Running
```bash
source .venv/bin/activate
python3 src/main.py --csv test.csv
```