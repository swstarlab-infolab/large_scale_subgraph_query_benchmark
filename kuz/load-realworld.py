import kuzu
from os import listdir
from os.path import isfile, join
import logging
import shutil
import sys

def load_schema(conn):
    schema_file = open('kuz/schema2.cypher').read().split(';')

    for schema in schema_file:
        print(schema)
        print()

        if schema == "":
            continue
        logging.info(f"Loading schema {schema}")
        conn.execute(f"{schema}")

    logging.info("Loaded schema")

def load_lsqb_dataset(conn, dataset, num_lbs):
    data_path = f'${RAW_DATASET_PATH}/cuMatch/CSV/{dataset}-LB{num_lbs}'

    if int(num_lbs) == 15 :
        node_tables = ["V0", "V1", "V2", "V3", "V4"]
        edge_tables = ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24"]
        node_files = ["0", "1", "2", "3", "4"]
        edge_files = ["0_0_0", "0_1_1", "0_2_2", "0_3_3", "0_4_4", "1_15_0", "1_16_1", "1_17_2", "1_18_3", "1_19_4", "2_30_0", "2_31_1", "2_32_2", "2_33_3", "2_34_4", "3_45_0", "3_46_1", "3_47_2", "3_48_3", "3_49_4", "4_60_0", "4_61_1", "4_62_2", "4_63_3", "4_64_4"]
    elif int(num_lbs) == 10 :
        node_tables = ["V0", "V1", "V2", "V3", "V4"]
        edge_tables = ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24"]
        node_files = ["0", "1", "2", "3", "4"]
        edge_files = ["0_0_0", "0_1_1", "0_2_2", "0_3_3", "0_4_4", "1_10_0", "1_11_1", "1_12_2", "1_13_3", "1_14_4", "2_20_0", "2_21_1", "2_22_2", "2_23_3", "2_24_4", "3_30_0", "3_31_1", "3_32_2", "3_33_3", "3_34_4", "4_40_0", "4_41_1", "4_42_2", "4_43_3", "4_44_4"]
    elif int(num_lbs) == 1 :
        node_tables = ["V0"]
        edge_tables = ["E0"]
        node_files = ["0"]
        edge_files = ["0_0_0"]
    else :
        print("Not support yet")
        return

    load_schema(conn)

    extension = ".csv"
    copy_options = "(HEADER=True, DELIM='|')"

    for i in range(len(node_tables)):
        logging.debug(f"Loading {node_tables[i]}")
        conn.execute(f"""COPY {node_tables[i]} from '{data_path}/{node_files[i]}{extension}' {copy_options}""")

    for i in range(len(edge_tables)):
        logging.debug(f"Loading {edge_tables[i]}")
        conn.execute(f"""COPY {edge_tables[i]} from '{data_path}/{edge_files[i]}{extension}' {copy_options}""")
    logging.info("Loaded data files")

def main():
    if len(sys.argv) < 1:
        print("Usage: client.py dataset num_lbs")
        print("Where sf is the scale factor)")
        exit(1)
    else:
        dataset = sys.argv[1]
        num_lbs = sys.argv[2]

    database_file_location = 'kuz/scratch/lsqb-database'
    shutil.rmtree(database_file_location, ignore_errors=True)

    db = kuzu.Database('kuz/scratch/lsqb-database')

    conn = kuzu.Connection(db)


    logging.info("Successfully connected")

    load_lsqb_dataset(conn, dataset, num_lbs)


if __name__ == "__main__":
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.DEBUG)
    main()

