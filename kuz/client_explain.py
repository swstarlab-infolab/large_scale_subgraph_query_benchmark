import time
import sys
import kuzu
import logging

def run_query(conn, system_variant, sf, query_id, query_spec, results_file):
    start = time.time()
    results = conn.execute(query_spec)
    if results.has_next():
        result = results.get_next()

    end = time.time()
    duration = end - start
    results_file.write(f"KuzuDB\t{system_variant}\t{sf}\t{query_id}\t{duration:.4f}\t{result[0]}\n")
    results_file.flush()
    return (duration, result)

def run_query_only(conn, system_variant, sf, query_id, query_spec):
    start = time.time()
    results = conn.execute(query_spec)
    if results.has_next():
        result = results.get_next()

    end = time.time()
    duration = end - start
    print(f"{query_id} | {sf}")
    print(result[0])
    return (duration, result)

def main():
    if len(sys.argv) < 1:
        print("Usage: client.py sf query_id")
        print("Where sf is the scale factor)")
        exit(1)
    else:
        sf = sys.argv[1]
        q_id = sys.argv[2] + "_explain"

    db = kuzu.Database('kuz/scratch/lsqb-database', max_num_threads=64)
    conn = kuzu.Connection(db)

    with open(f"results/results.csv", "a+") as results_file:
        with open(f"kuz/query/q{q_id}.cypher", "r") as query_file:
            run_query_only(conn, "", sf, q_id, query_file.read())

if __name__ == "__main__":
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.DEBUG)
    main()
