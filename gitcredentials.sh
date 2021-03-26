#!/bin/bash

git config --global credential.helper cache

git config --global credential.helper 'cache --timeout=3600' 

git config --global user.name $1
git config --global user.password $2

