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

def run_query_only(conn, system_variant, query_id, query_spec, num_lbs, dataset):
    start = time.time()
    results = conn.execute(query_spec)
    if results.has_next():
        result = results.get_next()

    end = time.time()
    duration = end - start
    print(f"{query_id} | {dataset} | {num_lbs} | {result[0]} | {duration}")
    return (duration, result)

def main():
    if len(sys.argv) < 1:
        print("Usage: client.py num_lbs dataset query_id")
        exit(1)
    else:
        num_lbs = sys.argv[1]
        dataset = sys.argv[2]
        q_id = sys.argv[3]

    db = kuzu.Database('kuz/scratch/lsqb-database', max_num_threads=64)
    conn = kuzu.Connection(db)

    if num_lbs != "1" :
        with open(f"kuz/query/realworld-labeled-q{q_id}.cypher", "r") as query_file:
            run_query_only(conn, "", q_id, query_file.read(), num_lbs, dataset)
    else :
        with open(f"kuz/query/realworld-unlabeled-q{q_id}.cypher", "r") as query_file:
            run_query_only(conn, "", q_id, query_file.read(), num_lbs, dataset)

if __name__ == "__main__":
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.DEBUG)
    main()
