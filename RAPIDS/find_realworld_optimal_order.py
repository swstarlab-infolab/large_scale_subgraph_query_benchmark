# left deep
import cudf
import time
import itertools
import sys

# Q1
Q1_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 0)
}
Q1_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"]

# Q2
Q2_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 0),
  "E4": (0, 2)
}
Q2_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4"]

# Q3
Q3_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 4),
  "E4": (4, 0),
  "E5": (0, 2)
}
Q3_MATCHING_ORDERS = ["E0", "E1", "E2", "E3", "E4", "E5"]

# Q4
Q4_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 0),
  "E3": (2, 3)
}
Q4_MATCHING_ORDERS = ["E0", "E1", "E2"]

# Q5
Q5_EDGES = {
  "E0": (0, 1),
  "E1": (1, 2),
  "E2": (2, 3),
  "E3": (3, 0),
  "E4": (0, 2)
}
Q5_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"]


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
        print(f"Loading {file_name}...")
        dataframes[key] = cudf.read_csv(file_path, delimiter="|", names=column_names, skiprows=1)
    print("All data loaded.")
    return dataframes

def determine_join_keys(intermediate_columns, current_columns):
    return list(set(intermediate_columns).intersection(current_columns))

def perform_query(order, dataframes):
    try:
        print(f"Testing order: {order}")
        start_time = time.time()

        result = dataframes[order[0]]
        for file_key in order[1:]:
            current_df = dataframes[file_key]
            join_keys = determine_join_keys(result.columns, current_df.columns)

            if not join_keys:
                print(f"Skipping order {order}: No common join keys.")
                return None, float('inf')
            
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
        
        if LB == 1 :
            if QUERY_ID == 1 :
                result = result[result[0] != result[2]]
                result = result[result[1] != result[3]]
            if QUERY_ID == 2 :
                result = result[result[1] != result[3]]
            if QUERY_ID == 3 :
                result = result[result[0] != result[3]]
                result = result[result[1] != result[3]]
                result = result[result[1] != result[4]]
                result = result[result[2] != result[4]]
            if QUERY_ID == 4 :
                result = result[result[0] != result[3]]
                result = result[result[1] != result[3]]
            if QUERY_ID == 5 :
                result = result[result[0] != result[2]]
                result = result[result[1] != result[3]]

        query_time = time.time() - start_time
        print(f"Order {order} completed in {query_time:.4f} seconds. (result: {len(result)})")
        return order, query_time

    except Exception as e:
        print(f"Error with order {order}: {e}")
        return None, float('inf')

def find_optimal_order(dataframes):
    all_orders = list(itertools.permutations(MATCHING_ORDERS))
    optimal_order = None
    min_time = float('inf')

    for order in all_orders:
        _, query_time = perform_query(order, dataframes)
        if query_time < min_time:
            optimal_order = order
            min_time = query_time

    if optimal_order:
        print(f"Optimal order: {optimal_order} with time {min_time:.4f} seconds.")
    else:
        print("No valid orders found.")
    return optimal_order, min_time


def main(lb, dataset):
    data_path = f"${RAW_DATASET_PATH}/cuMatch/CSV/{dataset}-LB{lb}/"    
    
    files = generate_files(EDGES, lb)

    dataframes = load_all_data(files, data_path)

    find_optimal_order(dataframes)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("parameter error!")
        exit(1)

    DATASET = sys.argv[1]
    LB = int(sys.argv[2])
    QUERY_ID = int(sys.argv[3])

    if QUERY_ID == 1 :
        EDGES = Q1_EDGES
        MATCHING_ORDERS = Q1_MATCHING_ORDERS
    
    elif QUERY_ID == 2 :
        EDGES = Q2_EDGES
        MATCHING_ORDERS = Q2_MATCHING_ORDERS
    
    elif QUERY_ID == 3 :
        EDGES = Q3_EDGES
        MATCHING_ORDERS = Q3_MATCHING_ORDERS
    
    elif QUERY_ID == 4 :
        EDGES = Q4_EDGES
        MATCHING_ORDERS = Q4_MATCHING_ORDERS
    
    elif QUERY_ID == 5 :
        EDGES = Q5_EDGES
        MATCHING_ORDERS = Q5_MATCHING_ORDERS
    
    else :
        print("query id error")
        exit(1)

    main(LB, DATASET)

