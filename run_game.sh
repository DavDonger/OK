#!/bin/bash

# Folder containing city data files
CITY_DATA_FOLDER="data/cities"
# Path to the agent data file
AGENT_DATA_FOLDER="data/agents"
# Number of cycles and seed
CYCLES=1000
SEED=2
COUNTER=0

for CITY_DATA_FILE in "$CITY_DATA_FOLDER"/cityData_*.data
do
    PREFIX=$(basename "$CITY_DATA_FILE" | sed -E 's/cityData_([0-9]+).data/\1/')

    AGENT_DATA_FILE="$AGENT_DATA_FOLDER/agentData_${PREFIX}.data"
    OUTPUT_FILE="data/tests/output_${BASE_NAME}_${PREFIX}.txt"
    EXPECTED_OUTPUT_FILE="data/tests/expected_output_${BASE_NAME}_${PREFIX}.txt"
    
    (echo "run" | ./game "$CITY_DATA_FILE" "$AGENT_DATA_FILE" "$CYCLES" "$SEED") > "$OUTPUT_FILE"
    
    (echo "run" | /web/cs2521/24T3/ass/ass2/reference/game "$CITY_DATA_FILE" "$AGENT_DATA_FILE" "$CYCLES" "$SEED") > "$EXPECTED_OUTPUT_FILE"
    
    if diff -q "$OUTPUT_FILE" "$EXPECTED_OUTPUT_FILE" > /dev/null; then
        rm "$OUTPUT_FILE" "$EXPECTED_OUTPUT_FILE"
        rm "$AGENT_DATA_FILE" "$CITY_DATA_FILE"
    else
        echo "Differences found for $PREFIX:"
        diff "$OUTPUT_FILE" "$EXPECTED_OUTPUT_FILE"
        exit 1
    fi
    echo "$COUNTER"
    COUNTER=$((COUNTER+1))
done
