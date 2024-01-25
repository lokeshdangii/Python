#!/bin/bash

# Function to extract email addresses from a given line
extract_emails() {
    line=$1
    # Split the line into words
    words=($line)
    
    # Loop through words to find potential email addresses
    for word in "${words[@]}"; do
        # Check if the word contains @ and .
        if [[ "$word" == *.*@*.* ]]; then
            echo "$word"
        fi
    done
}

# Main script
while IFS= read -r line; do
    # Call the function to extract emails from the current line
    extract_emails "$line"
done < mbox-short.txt

