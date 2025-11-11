start=$(date +%s)

time ./init-and-load-projected.sh

echo time $(( $(date +%s) - $start ))
