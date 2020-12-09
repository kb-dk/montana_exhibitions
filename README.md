# Montana Exhibitions

Static site generator for 'Skatteudstilling 2020' iPads

## Usage

#### (Optional) Setup virtualenv
```bash
sudo apt install python3-venv python3-pip python3-dev
python3 -m venv .venv
source .venv/bin/activate
# pip3 install commands below
```

#### Setup
```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
# or pip3 install Jinja2, pandas and xlrd
```

#### Running
Provided that you have access to Royal library's 'Adhoc-Skatteudstilling' team, you can copy 'skatteUdstilling_2020.xlsx' to the project root folder from [here](https://teams.microsoft.com/l/file/899C55C1-1929-4F98-9482-1C0848F71176?tenantId=6a74b223-3e14-422e-a272-1ee287717296&fileType=xlsx&objectUrl=https%3A%2F%2Fkbintern.sharepoint.com%2Fsites%2FAdhoc-Skatteudstilling%2FDelte%20dokumenter%2FGeneral%2FskatteUdstilling_2020.xlsx&baseUrl=https%3A%2F%2Fkbintern.sharepoint.com%2Fsites%2FAdhoc-Skatteudstilling&serviceName=teams&threadId=19:9bc5e6cb3b3b4ceb86190d651bd61050@thread.tacv2&groupId=0cb62681-4a07-4daa-82eb-8e68a610e7ce): 

```bash
python3 src/main.py --csv skatteUdstilling_2020.xlsx
```

#### Viewing
```bash
python3 -m http.server
```
Now visit http://localhost:8000/output

#### Fonts
We use 'Berlingske' fonts in our stylesheet, if you need to access them you need to write to 'servicedesk.kb.dk' and get access to the folder, and then place it under your includes folder.
