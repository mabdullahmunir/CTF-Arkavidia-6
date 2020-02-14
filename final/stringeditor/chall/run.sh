#!/bin/sh
socat -T120 tcp-l:10000,reuseaddr,fork exec:"./stringeditor"
