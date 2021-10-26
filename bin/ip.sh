#!/bin/bash
echo  " %{F#7fadff}%{-u} %{F#ffffff}$(ip a | grep -w "inet" | grep -v "127" | awk '{print $2}' | tr "/" "\n" | head -1)%{-u} "