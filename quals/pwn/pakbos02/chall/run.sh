#!/bin/sh
socat -T120 tcp-l:10098,reuseaddr,fork exec:"timeout -s 9 120 ./pakbos02"
