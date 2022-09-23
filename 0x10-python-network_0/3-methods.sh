#!/bin/bash
# Display all HTPP methods accept
curl --head -s "$1" | grep 'Allow:' | cut -d ' ' -f 2-
