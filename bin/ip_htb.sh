#!/bin/bash
if [[ $(ip a | grep -w "tun0") ]]
then
    echo "%{F#1bbf3e} $(ip a | grep -w "inet" | grep -v "127" |  grep -v "192" | awk '{print $2}' | tr "/" "\n" | head -1)%{-u}"
else
    echo "%{F#1bbf3e}%{-u} Desconectado"
fi