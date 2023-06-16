# Instructions

## Installation
```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Setup Cron
```sh
crontab -e
crontab -l
```

```sh
0 0 * * 0 python3 <path>/main.py
```

References

[GeekyTheory](https://geekytheory.com/programar-tareas-en-linux-usando-crontab)
