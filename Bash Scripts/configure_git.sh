#!/bin/bash

echo ""
echo "Working..."
echo "Your Git Username: "
read USER
echo " "
echo "Your Git Email: "
read EMAIL

echo "Configuring global user name and email..."
git config --global user.name "$USER"
git config --global user.email "$EMAIL"
