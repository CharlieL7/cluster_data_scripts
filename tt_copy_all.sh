#!/usr/bin/env bash

IN_DIR=/depot/vnarsim/data/lin_data/os_shear_full/
OUT_DIR=/depot/vnarsim/data/lin_data/os_shear_thin/

for dir in ${IN_DIR}*/; do
    python tt_copy.py "$dir" "${OUT_DIR}/$(basename ${dir}/)" --mod 100 &
done
