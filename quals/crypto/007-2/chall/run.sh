#!/bin/sh
socat tcp-l:10099,reuseaddr,fork exec:"python chall.py"
