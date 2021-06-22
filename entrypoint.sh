#!/bin/bash
set +x

echo $1 $2 $3 $4
rpios-dl --version=$1 --release=$2 --raspios-image-cache-dir=$3

rpios-img $1 $2 $4/output.img --raspios-image-cache-dir=$3

fdisk -l $4/output.img