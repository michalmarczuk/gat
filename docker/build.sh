#!/bin/bash

version=0.1
image_name=gat-tests

docker build -t ${image_name}:latest -t ${image_name}:${version} .