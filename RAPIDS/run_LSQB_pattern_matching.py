# left deep
import cudf
import time
import itertools
import sys

EDGES = {}
MATCHING_ORDERS = []
SF = ""

# Q1
Q1_EDGES = {
  "E0": (0, 1, "Forum_hasMember_Person.csv"),
  "E1": (0, 2, "Forum_containerOf_Post.csv"),
  "E2": (3, 2, "Comment_replyOf_Post.csv"),
  "E3": (3, 4, "Comment_hasTag_Tag.csv")
}
Q1_MATCHING_ORDERS = ["E0", "E1", "E2", "E3"] # R.E

# Q2
Q2_EDGES = {
  "E0": (0, 1, "Comment_replyOf_Post.csv"),
  "E1": (0, 2, "Comment_hasCreator_Person.csv"),
  "E2": (1, 3, "Post_hasCreator_Person.csv"),
  "E3": (2, 3, "Person_knows_Person_bidirectional.csv")
}
Q2_MATCHING_ORDERS = ["E2", "E0", "E1", "E3"]

# Q3
Q3_EDGES = {
  "E0": (1, 0, "City_isPartOf_Country.csv"),
  "E1": (2, 0, "City_isPartOf_Country.csv"),
  "E2": (3, 0, "City_isPartOf_Country.csv"),
  "E3": (4, 1, "Person_isLocatedIn_City.csv"),
  "E4": (5, 2, "Person_isLocatedIn_City.csv"),
  "E5": (6, 3, "Person_isLocatedIn_City.csv"),
  "E6": (4, 5, "Person_knows_Person_bidirectional.csv"),
  "E7": (5, 6, "Person_knows_Person_bidirectional.csv"),
  "E8": (4, 6, "Person_knows_Person_bidirectional.csv"),
}
Q3_MATCHING_ORDERS = ["E5", "E2", "E8", "E3", "E0", "E7", "E6", "E4", "E1"]

# Q4
Q4_EDGES = {
  "E0": (0, 1, "Message_hasTag_Tag.csv"),
  "E1": (0, 4, "Message_hasCreator_Person.csv"),
  "E2": (2, 0, "Person_likes_Message.csv"),
  "E3": (3, 0, "Message_replyOf_Message.csv")
}
Q4_MATCHING_ORDERS  = ["E0", "E1", "E2", "E3"]

# Q5
Q5_EDGES = {
  "E0": (0, 1, "Message_hasTag_Tag.csv"),
  "E1": (2, 0, "Message_replyOf_Message.csv"),
  "E2": (2, 3, "Comment_hasTag_Tag.csv")
}
Q5_MATCHING_ORDERS  = ["E1", "E2", "E0"]

# Q6
Q6_EDGES = {
  "E0": (0, 1, "Person_knows_Person_bidirectional.csv"),
  "E1": (1, 2, "Person_knows_Person_bidirectional.csv"),
  "E2": (2, 3, "Person_hasInterest_Tag.csv")
}
Q6_MATCHING_ORDERS  = ["E0", "E1", "E2"] # O.O.M.

# Q7
Q7_EDGES = {
  "E0": (0, 1, "Message_hasTag_Tag.csv"),
  "E1": (0, 4, "Message_hasCreator_Person.csv"),
  "E2": (2, 0, "Person_likes_Message.csv"),
  "E3": (3, 0, "Message_replyOf_Message.csv")
}
Q7_MATCHING_ORDERS  = ["E1", "E0"]

# Q8
Q8_EDGES = {
  "E0": (0, 1, "Message_hasTag_Tag.csv"),
  "E1": (2, 0, "Message_replyOf_Message.csv"),
  "E2": (2, 3, "Comment_hasTag_Tag.csv"),
  "E3": (2, 1, "Comment_hasTag_Tag.csv")
}
Q8_MATCHING_ORDERS  = ["E1", "E2", "E0"]

# Q9
Q9_EDGES = {
  "E0": (0, 1, "Person_knows_Person_bidirectional.csv"),
  "E1": (1, 2, "Person_knows_Person_bidirectional.csv"),
  "E2": (2, 3, "Person_hasInterest_Tag.csv"),
  "E3": (0, 2, "Person_knows_Person_bidirectional.csv")
}
Q9_MATCHING_ORDERS  = ["E0", "E1", "E2"] # O.O.M.


def generate_files(edges):
    files = {}
    for key, (src, tgt, name) in edges.items():
        files[key] = name
    return files

FILES = generate_files(EDGES)

def load_all_data(files, data_path):
    dataframes = {}
    for key, file_name in files.items():
        file_path = data_path + file_name
        column_names = [EDGES[key][0], EDGES[key][1]]
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

        if QUERY_ID == 7 :
            current_df = dataframes["E2"]
            join_keys = determine_join_keys(result.columns, current_df.columns)
            result = result.merge(current_df, on=join_keys, how='left')
            current_df = dataframes["E3"]
            join_keys = determine_join_keys(result.columns, current_df.columns)
            result = result.merge(current_df, on=join_keys, how='left')

        if QUERY_ID == 8 :
            current_df = dataframes["E3"]
            join_keys = determine_join_keys(result.columns, current_df.columns)
            result = result.merge(current_df, on=join_keys, how='leftanti')
            
        if QUERY_ID == 9 :
            current_df = dataframes["E3"]
            join_keys = determine_join_keys(result.columns, current_df.columns)
            result = result.merge(current_df, on=join_keys, how='leftanti')

        if QUERY_ID == 5 or QUERY_ID == 8 :
            result = result[result[1] != result[3]]
        
        if QUERY_ID == 6 or QUERY_ID == 9 :
            result = result[result[0] != result[2]]

        return len(result)

    except Exception as e:
        print(f"Error with order {order}: {e}")
        return 0

def run_query(dataframes):
    return perform_query(MATCHING_ORDERS, dataframes)

def main():
    start_time = time.time()

    data_path = f"${RAW_DATASET_PATH}/LSQB/LSQB_dataset/social-network-sf{SF}-projected-fk/"
    
    files = generate_files(EDGES)

    dataframes = load_all_data(files, data_path)

    num_patterns = run_query(dataframes)

    query_time = time.time() - start_time
    print(f"{QUERY_ID} | {SF} | {num_patterns} | {query_time}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("parameter error!")
        exit(1)

    SF = sys.argv[1]
    QUERY_ID = int(sys.argv[2])

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
        
    elif QUERY_ID == 6 :
        EDGES = Q6_EDGES
        MATCHING_ORDERS = Q6_MATCHING_ORDERS
    
    elif QUERY_ID == 7 :
        EDGES = Q7_EDGES
        MATCHING_ORDERS = Q7_MATCHING_ORDERS
    
    elif QUERY_ID == 8 :
        EDGES = Q8_EDGES
        MATCHING_ORDERS = Q8_MATCHING_ORDERS
    
    elif QUERY_ID == 9 :
        EDGES = Q9_EDGES
        MATCHING_ORDERS = Q9_MATCHING_ORDERS

    else :
        print("query id error")
        exit(1)

    main()



