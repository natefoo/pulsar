#!/bin/bash

pdl="$(command -v pulsar-drmaa-launch)"

echo "umask is $(umask)"
echo "pwd is $(pwd)"
echo "\$HOME is $HOME"
echo "\$VIRTUAL_ENV is $VIRTUAL_ENV"
echo "\$DRMAA_LIBRARY_PATH is $DRMAA_LIBRARY_PATH"
echo "pulsar-drmaa-launch is $pdl"

for path in $pdl $DRMAA_LIBRARY_PATH; do
    a=(${path//\// })
    p=''
    for i in "${!a[@]}"; do
        p+="/${a[$i]}"
        ls -ld "$p"
    done
done

/usr/bin/sudo -E -n -u u1 $pdl
