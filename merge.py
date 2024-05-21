import convertToEventsNodes
import convertToEventsEdges
import os 

def read_events_from_file(file_path):
    with open(file_path, 'r') as file:
        events = [line.strip() for line in file]
    return events

def merge_and_sort_events(file1_path, file2_path, output_file_path):
    # Read events from both files
    events_file1 = read_events_from_file(file1_path)
    events_file2 = read_events_from_file(file2_path)

    # Merge events
    merged_events = events_file1 + events_file2

    # Sort events by time (last variable)
    sorted_events = sorted(merged_events, key=lambda x: x.split()[-1])

    # Save sorted events into the output file
    with open(output_file_path, 'w') as output_file:
        for event in sorted_events:
            output_file.write(f"{event}\n")

    print(f"Merged and sorted events saved to {output_file_path}")

file1_path = 'eventsNodes.txt'
file2_path = 'eventsEdges.txt'
if os.path.exists(file1_path):
        # If it exists, delete the file
        os.remove(file1_path)
# Create an empty file
with open(file1_path, 'w'):
    pass

if os.path.exists(file2_path):
        # If it exists, delete the file
        os.remove(file2_path)
# Create an empty file
with open(file2_path, 'w'):
    pass

convertToEventsEdges.transformEdges(file2_path, "SF3/Person_knows_Person", "SF3/Forum_hasMember_Person")
convertToEventsNodes.transformNodes(file1_path, ["SF3/Person", "SF3/Forum"])
# Specify the paths to your input files and the output file

output_file_path = 'merged_and_sorted_eventsSF3_extended.txt'

# Call the function to merge and sort events
merge_and_sort_events(file1_path, file2_path, output_file_path)
