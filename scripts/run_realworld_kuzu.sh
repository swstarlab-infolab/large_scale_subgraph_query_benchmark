export LB=10
export DATASET=Orkut

./kuz/init-and-load-realworld.sh > /dev/null 2>&1
sleep 10
./kuz/run_benchmark_realworld.sh

export LB=10
export DATASET=Friendster

./kuz/init-and-load-realworld.sh > /dev/null 2>&1
sleep 10
./kuz/run_benchmark_realworld.sh

export LB=1
export DATASET=LiveJournal

./kuz/init-and-load-realworld.sh
sleep 10
./kuz/run_benchmark_realworld.sh

export LB=15
export DATASET=Twitter

./kuz/init-and-load-realworld.sh > /dev/null 2>&1
sleep 10
./kuz/run_benchmark_realworld.sh
