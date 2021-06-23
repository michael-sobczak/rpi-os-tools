#!/bin/bash
set +x

echo "Downloading OS..."
rpios-dl --hide-progress --version=$1 --release=$2 --raspios-image-cache-dir=$3

echo "Customizing Image..."
rpios-img $1 $2 $4/output.img --raspios-image-cache-dir=$3


echo "Checking the disk..."
fdisk -l $4/output.img