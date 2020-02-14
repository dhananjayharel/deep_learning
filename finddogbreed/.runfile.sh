#!/usr/bin/env bash
echo "Processing the image please wait.."
:> .testcaseop && python3 findcatdog.py > .testcaseop
echo "done"
