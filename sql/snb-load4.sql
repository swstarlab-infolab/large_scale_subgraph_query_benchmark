COPY V0                 FROM 'PATHVAR/0.csv'                 (DELIMITER '|', HEADER, FORMAT csv);

COPY A2Q          FROM 'PATHVAR/0_0_0.csv'          (DELIMITER '|', HEADER, FORMAT csv);
COPY C2A          FROM 'PATHVAR/0_1_0.csv'          (DELIMITER '|', HEADER, FORMAT csv);
COPY C2Q          FROM 'PATHVAR/0_2_0.csv'          (DELIMITER '|', HEADER, FORMAT csv);
