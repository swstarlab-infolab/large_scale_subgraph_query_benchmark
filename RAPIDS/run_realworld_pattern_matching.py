# left deep
import cudf
import time
import itertools
import sys
from cudf.utils.performance_tracking import print_memory_report
from rmm.statistics import enable_statistics

enable_statistics()
cudf.set_option("memory_profiling", True)

# Q1
Q1_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 0)
}
LJ_Q1_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # O.O.M
OR_Q1_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # R.E
FR_Q1_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # O.O.M
TW_Q1_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # O.O.M

# Q2
Q2_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 0),
  "E4": (0, 2)
}
LJ_Q2_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4"] # O.O.M
OR_Q2_MATCHING_ORDERS = ["E2", "E4", "E3", "E1", "E0"]
FR_Q2_MATCHING_ORDERS = ["E0", "E4", "E1", "E2", "E3"]
TW_Q2_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4"] # O.O.M

# Q3
Q3_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 4),
  "E4": (4, 0),
  "E5": (0, 2)
}
LJ_Q3_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4", "E5"] # O.O.M
OR_Q3_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4", "E5"] # R.E
FR_Q3_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4", "E5"] # O.O.M
TW_Q3_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4", "E5"] # O.O.M

# Q4
Q4_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 0),
  "E3": (2, 3)
}
LJ_Q4_MATCHING_ORDERS = ["E0", "E1", "E2"] # O.O.M
OR_Q4_MATCHING_ORDERS = ["E2", "E1", "E0"]
FR_Q4_MATCHING_ORDERS = ["E0", "E1", "E2"]
TW_Q4_MATCHING_ORDERS = ["E0", "E1", "E2"] # O.O.M

# Q5
Q5_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 0),
  "E4": (0, 2)
}
LJ_Q5_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # O.O.M
OR_Q5_MATCHING_ORDERS = ["E3", "E2", "E1", "E0"] # R.E
FR_Q5_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # O.O.M
TW_Q5_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # O.O.M


EDGES = {}
MATCHING_ORDERS = {}
LB = 0
DATASET = ""

def generate_files(edges, lb):
    files = {}
    for key, (src, tgt) in edges.items():
        if LB != 1 :
            files[key] = f"{src}_{str(int(src) * LB + int(tgt))}_{tgt}.csv"
        else : 
            files[key] = "0_0_0.csv"
    return files

FILES = generate_files(EDGES, LB)

def load_all_data(files, data_path):
    dataframes = {}
    for key, file_name in files.items():
        file_path = data_path + file_name
        column_names = [str(col) for col in EDGES[key]]
        # print(f"Loading {file_name}...")
        dataframes[key] = cudf.read_csv(file_path, delimiter="|", names=column_names, skiprows=1)
    # print("All data loaded.")
    return dataframes

def determine_join_keys(intermediate_columns, current_columns):
    return list(set(intermediate_columns).intersection(current_columns))

def perform_query(order, dataframes):
    try:
        result = dataframes[order[0]]
        for file_key in order[1:]:
            current_df = dataframes[file_key]
            join_keys = determine_join_keys(result.columns, current_df.columns)

            if not join_keys:
                print(f"Skipping order {order}: No common join keys.")
                return 0
            
            # print(file_key, join_keys)
            result = result.merge(current_df, on=join_keys)
            # result.info()


        if QUERY_ID == 4 :
            current_df = dataframes["E3"]
            join_keys = determine_join_keys(result.columns, current_df.columns)
            result = result.merge(current_df, on=join_keys, how='left')

        if QUERY_ID == 5 :
            current_df = dataframes["E4"]
            join_keys = determine_join_keys(result.columns, current_df.columns)
            result = result.merge(current_df, on=join_keys, how='leftanti')

        return len(result)

    except Exception as e:
        print(f"Error with order {order}: {e}")
        return 0

def run_query(dataframes):
    return perform_query(MATCHING_ORDERS, dataframes)

def main(lb, dataset):
    start_time = time.time()

    data_path = f"${RAW_DATASET_PATH}/cuMatch/CSV/{dataset}-LB{lb}/"    
    
    files = generate_files(EDGES, lb)

    dataframes = load_all_data(files, data_path)

    num_patterns = run_query(dataframes)

    query_time = time.time() - start_time
    print(f"{QUERY_ID} | {DATASET}-LB{LB} | {num_patterns} | {query_time}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("parameter error!")
        exit(1)

    DATASET = sys.argv[1]
    LB = int(sys.argv[2])
    QUERY_ID = int(sys.argv[3])

    if QUERY_ID == 1 :
        EDGES = Q1_EDGES
        if DATASET == "LiveJournal" :
            MATCHING_ORDERS = LJ_Q1_MATCHING_ORDERS
        elif DATASET == "Orkut" :
            MATCHING_ORDERS = OR_Q1_MATCHING_ORDERS
        elif DATASET == "Friendster" :
            MATCHING_ORDERS = FR_Q1_MATCHING_ORDERS
        elif DATASET == "Twitter" :
            MATCHING_ORDERS = TW_Q1_MATCHING_ORDERS
        else :
            print("Supported not yet")
            exit(1)
    
    elif QUERY_ID == 2 :
        EDGES = Q2_EDGES
        if DATASET == "LiveJournal" :
            MATCHING_ORDERS = LJ_Q2_MATCHING_ORDERS
        elif DATASET == "Orkut" :
            MATCHING_ORDERS = OR_Q2_MATCHING_ORDERS
        elif DATASET == "Friendster" :
            MATCHING_ORDERS = FR_Q2_MATCHING_ORDERS
        elif DATASET == "Twitter" :
            MATCHING_ORDERS = TW_Q2_MATCHING_ORDERS
        else :
            print("Dataset error")
            exit(1)
    
    elif QUERY_ID == 3 :
        EDGES = Q3_EDGES
        if DATASET == "LiveJournal" :
            MATCHING_ORDERS = LJ_Q3_MATCHING_ORDERS
        elif DATASET == "Orkut" :
            MATCHING_ORDERS = OR_Q3_MATCHING_ORDERS
        elif DATASET == "Friendster" :
            MATCHING_ORDERS = FR_Q3_MATCHING_ORDERS
        elif DATASET == "Twitter" :
            MATCHING_ORDERS = TW_Q3_MATCHING_ORDERS
        else :
            print("Dataset error")
            exit(1)

    elif QUERY_ID == 4 :
        EDGES = Q4_EDGES
        if DATASET == "LiveJournal" :
            MATCHING_ORDERS = LJ_Q4_MATCHING_ORDERS
        elif DATASET == "Orkut" :
            MATCHING_ORDERS = OR_Q4_MATCHING_ORDERS
        elif DATASET == "Friendster" :
            MATCHING_ORDERS = FR_Q4_MATCHING_ORDERS
        elif DATASET == "Twitter" :
            MATCHING_ORDERS = TW_Q4_MATCHING_ORDERS
        else :
            print("Dataset error")
            exit(1)
    
    elif QUERY_ID == 5 :
        EDGES = Q5_EDGES
        if DATASET == "LiveJournal" :
            MATCHING_ORDERS = LJ_Q5_MATCHING_ORDERS
        elif DATASET == "Orkut" :
            MATCHING_ORDERS = OR_Q5_MATCHING_ORDERS
        elif DATASET == "Friendster" :
            MATCHING_ORDERS = FR_Q5_MATCHING_ORDERS
        elif DATASET == "Twitter" :
            MATCHING_ORDERS = TW_Q5_MATCHING_ORDERS
        else :
            print("Dataset error")
            exit(1)
    
    else :
        print("Query id error")
        exit(1)
    main(LB, DATASET)

    print_memory_report()
