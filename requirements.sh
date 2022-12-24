#!/bin/bash


Requirements=(
    "Flask"
    "flask_login"
    "flask_sqlalchemy"
    "gunicorn"
    )

for module in ${Requirements[@]};do
   pip install $module
done

