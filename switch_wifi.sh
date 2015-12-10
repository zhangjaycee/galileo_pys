#!/bin/bash

cd /var/lib/connman/

if [ $1 = iphone ];then
	cp wifi.config.iphone wifi.config
	exit 0
fi

if [ $1 -eq 113 ];then
	cp wifi.config.113 wifi.config
	exit 0
fi

echo usage: $0 wifi(113 or iphone)
