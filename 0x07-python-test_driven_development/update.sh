#!/bin/bash
rm *~ && rm tests/*~
git add . && git commit -m updates && git push -u origin main
