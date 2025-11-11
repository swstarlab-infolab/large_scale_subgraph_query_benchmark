export LB=10
export DATASET=Orkut

docker exec -it 9ab bash -c "cd /var/lib/heavyai/realworld && export LB=10 && export DATASET=Orkut && ./load_shell_realworld.sh" > /dev/null 2>&1
sleep 40
./heavyDB/run_benchmark_realworld.sh
sleep 10

export LB=10
export DATASET=Friendster

docker exec -it 9ab bash -c "cd /var/lib/heavyai/realworld && export LB=10 && export DATASET=Friendster && ./load_shell_realworld.sh" > /dev/null 2>&1
sleep 40
./heavyDB/run_benchmark_realworld.sh
sleep 10

export LB=1
export DATASET=LiveJournal

docker exec -it 9ab bash -c "cd /var/lib/heavyai/realworld && export LB=1 && export DATASET=LiveJournal && ./load_shell_realworld.sh" > /dev/null 2>&1
sleep 40
./heavyDB/run_benchmark_realworld.sh
sleep 10

export LB=15
export DATASET=Twitter

docker exec -it 9ab bash -c "cd /var/lib/heavyai/realworld && export LB=15 && export DATASET=Twitter && ./load_shell_realworld.sh" > /dev/null 2>&1
sleep 30
./heavyDB/run_benchmark_realworld.sh
