#!/bin/bash
# Script that sends a request to a URL passed a argument
curl -s -o /dev/null -w "%{http_code}" "$1"
