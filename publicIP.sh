#!/bin/bash

# myip.enix.org replies our Public IP in response. A simple curl works wonder.

PUBLIC_IP=$(curl -s http://myip.enix.org/REMOTE_ADDR)

#sleep .5

if [ -n "$PUBLIC_IP" ]; then
    echo "Public IP Address: $PUBLIC_IP"
else
    echo "Unable to retrieve public IP address."
fi
