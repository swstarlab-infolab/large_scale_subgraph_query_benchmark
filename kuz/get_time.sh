start=$(date +%s)

time ./init-and-load.sh

echo time $(( $(date +%s) - $start ))
