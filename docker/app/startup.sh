#!/bin/bash

cd /code

# pipenv install

pipenv install --system

# db migration
db-migrate

/bin/bash