#!/bin/bash




gunicorn --bind 127.0.0.1:8080 app:app
