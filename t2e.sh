#!/bin/bash

#将当前文件夹下的epub文件转化为Txt文件

rm -rf /tmp/epub
mkdir -p /tmp/epub/sources
mkdir -p /tmp/epub/txts

fox x in `ls`
do
    if [[ "${x}" =~ ".epub" ]] && [ -f ${x} ]
    then
        mkdir /tmp/epub/sources/${x}
        unzip ${x} -d /tmp/epub/sources/${x}
    fi
done

cd /tmp/epub/sources

for x in `ls`
do
    if [[ "${x}" =~ ".epub" ]]
    then
        echo “handling ${x}”
        filename=${x/.epub/}
        for y in `find ${x} -name "*ml"`
        do
            if [[ "${y}" =~ "container.xml" ]]
            then
                continue
            else
                echo "handling ${y}"
                cat ${y} | dehtml.py >>../txts/${filename}".txt"
            fi
        done
    fi
done

cd -
cp -R /tmp/epub/txts .
rm -rf /tmp/epub

echo "see ./txts"
