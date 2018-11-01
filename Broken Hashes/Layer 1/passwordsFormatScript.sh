#!/bin/bash


cat *.broken | grep -o ':.*$' | sort -u | sed 's/://' >> allpasswords
