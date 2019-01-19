## Werkzeug

```bash
  git clone https://github.com/AlexKorob/werkzeug.git
  python3 -m venv ./venv
  source venv/bin/activate
  pip3 install -r requirements.txt
```

Before start server you need run mongo database from mongo/db:

```bash
  mongod --dbpath ./mongo/db --logpath ./mongo/mongo_logs.log
```
and then start server:
```bash
  python3 main.py
```
