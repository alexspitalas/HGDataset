import pandas as pd
import os

def transform_csv_to_eventsFmP(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file, sep ='|')

    # Create a list to store events
    events = []

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Event: Create edge at the creationDate
        create_vertex_event = f"edge ForumHasMemberPerson {row['ForumId']} {row['PersonId']} creationDate {row['creationDate']}"
        events.append(create_vertex_event)

        # Event: Add label and value at the corresponding time
        #label_value_event = f"vertex {row['id']} label {row['firstName']} {row['lastName']} {row['gender']} {row['birthday']} {row['locationIP']} {row['browserUsed']} {row['LocationCityId']} {row['language']} {row['email']} {row['creationDate']}"
        #events.append(label_value_event)

        # Event: Delete edge at the deletionDate (if available)
        #if not pd.isnull(row['deletionDate']):
        if row['explicitlyDeleted'] == True :
            delete_vertex_event = f"delete edge ForumHasMemberPerson {row['ForumId']} {row['PersonId']} {row['deletionDate']}"
            events.append(delete_vertex_event)
    print (len(events))
    return events

def transform_csv_to_eventsPkP(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file, sep ='|')

    # Create a list to store events
    events = []

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Event: Create edge at the creationDate
        create_vertex_event = f"edge PersonKnowsPerson {row['Person1Id']} {row['Person2Id']} creationDate {row['creationDate']}"
        events.append(create_vertex_event)

        # Event: Add label and value at the corresponding time
        #label_value_event = f"vertex {row['id']} label {row['firstName']} {row['lastName']} {row['gender']} {row['birthday']} {row['locationIP']} {row['browserUsed']} {row['LocationCityId']} {row['language']} {row['email']} {row['creationDate']}"
        #events.append(label_value_event)

        # Event: Delete edge at the deletionDate (if available)
        #if not pd.isnull(row['deletionDate']):
        if row['explicitlyDeleted'] == True :
            delete_vertex_event = f"delete edge PersonKnowsPerson {row['Person1Id']} {row['Person2Id']} {row['deletionDate']}"
            events.append(delete_vertex_event)
    print (len(events))
    return events

def transformEdges(output, inputPkP, inputFmP = None):
    # Specify the path to your CSV file and output file
    #csv_file_path = 'part-00000-f3990312-a16f-472e-8547-3d36f5312e61-c000.csv'
    #output_file_path = 'events.txt'
    #csv_file_path = input
    output_file_path = output

    # Call the function to transform CSV to events
    # Iterate over all files in the directory
    for filename in os.listdir(inputPkP):
        file_path = os.path.join(inputPkP, filename)
        resulting_events = transform_csv_to_eventsPkP(file_path)

        # Save the resulting events into a file
        with open(output_file_path, 'a+') as output_file:
            for event in resulting_events:
                output_file.write(f"{event}\n")

    # Call the function to transform CSV to events
    # Iterate over all files in the directory
    if inputFmP != None:
        for filename in os.listdir(inputFmP):
            file_path = os.path.join(inputFmP, filename)
            resulting_events = transform_csv_to_eventsFmP(file_path)

            # Save the resulting events into a file
            with open(output_file_path, 'a+') as output_file:
                for event in resulting_events:
                    output_file.write(f"{event}\n")

    print(f"Events saved to {output_file_path}")
