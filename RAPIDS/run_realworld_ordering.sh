export LB=10
export DATASET=Orkut

python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 1 >> ./result/${DATASET}-${LB}_q1.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 2 >> ./result/${DATASET}-${LB}_q2.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 3 >> ./result/${DATASET}-${LB}_q3.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 4 >> ./result/${DATASET}-${LB}_q4.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 5 >> ./result/${DATASET}-${LB}_q5.txt

export LB=10
export DATASET=Friendster

python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 1 >> ./result/${DATASET}-${LB}_q1.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 2 >> ./result/${DATASET}-${LB}_q2.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 3 >> ./result/${DATASET}-${LB}_q3.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 4 >> ./result/${DATASET}-${LB}_q4.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 5 >> ./result/${DATASET}-${LB}_q5.txt


export LB=15
export DATASET=Twitter

python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 1 >> ./result/${DATASET}-${LB}_q1.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 2 >> ./result/${DATASET}-${LB}_q2.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 3 >> ./result/${DATASET}-${LB}_q3.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 4 >> ./result/${DATASET}-${LB}_q4.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 5 >> ./result/${DATASET}-${LB}_q5.txt


export LB=1
export DATASET=LiveJournal

python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 1 >> ./result/${DATASET}-${LB}_q1.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 2 >> ./result/${DATASET}-${LB}_q2.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 3 >> ./result/${DATASET}-${LB}_q3.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 4 >> ./result/${DATASET}-${LB}_q4.txt
python3 -u find_realworld_optimal_order.py ${DATASET} ${LB} 5 >> ./result/${DATASET}-${LB}_q5.txt