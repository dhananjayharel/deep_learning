#!/usr/bin/env bash
echo "Processing the image please wait.."
:> .testcaseop2 && python3 dogbreed.py > .testcaseop2

if grep -q 'Error: ' .testcaseop2; then
   echo "SYNTAXERROR"
else if grep -q 'SUCCESS' .testcaseop2; then
   echo "SUCCESS"
else
   echo "UNKNOWNERROR"    
fi
fi
echo ""
echo "!done!"
