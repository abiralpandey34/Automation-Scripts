#!/bin/bash

# myip.enix.org replies with our Public. A simple curl works wonder.

PUBLIC_IP=$(curl -s http://myip.enix.org/REMOTE_ADDR) # May need to change link in future.

#sleep .5

if [ -n "$PUBLIC_IP" ]; then
    echo "Public IP Address: $PUBLIC_IP"
else
    echo "Unable to retrieve public IP address."
fi
