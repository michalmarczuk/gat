#!/bin/bash

(cd /usr/src/gat && find . -name "*.pyc" | xargs -r rm)