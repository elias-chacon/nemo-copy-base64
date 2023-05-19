#!/bin/bash

__localdir=~/.local/share/nemo-python/extensions

function __create_local_directory() {
    ! [ -d $__localdir ] && mkdir -p $__localdir
}

function __copy_script() {
    cp -f ./nemo-base64-copy.py $__localdir
}

function __restart_nemo() {
    nemo -q
}


# run all
__create_local_directory
__copy_script
__restart_nemo
