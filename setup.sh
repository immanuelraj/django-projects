#!/bin/sh

pip install -r ./requirement.txt --default-timeout=100
python ../../manage.py runserver_plus 0.0.0.0:8000 --nopin