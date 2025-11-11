./umb/stop-and-rm.sh

export LB=10
export DATASET=Orkut

./umb/init-and-load-realworld.sh > /dev/null 2>&1
sleep 10
./umb/run_realworld_benchmark.sh

export LB=10
export DATASET=Friendster

./umb/init-and-load-realworld.sh > /dev/null 2>&1
sleep 10
./umb/run_realworld_benchmark.sh

export LB=1
export DATASET=LiveJournal

./umb/init-and-load-realworld.sh > /dev/null 2>&1
sleep 10
./umb/run_realworld_benchmark.sh

export LB=15
export DATASET=Twitter

./umb/init-and-load-realworld.sh > /dev/null 2>&1
sleep 10
./umb/run_realworld_benchmark.sh
