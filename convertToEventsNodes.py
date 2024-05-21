import pandas as pd
import os

def transform_csv_to_events(csv_file, category):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file, sep ='|')

    # Create a list to store events
    events = []

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Event: Create vertex at the creationDate
        create_vertex_event = f"vertex {row['id']} {category} creationDate {row['creationDate']}"
        events.append(create_vertex_event)

        # Event: Add label and value at the corresponding time
        #label_value_event = f"vertex {row['id']} label {row['firstName']} {row['lastName']} {row['gender']} {row['birthday']} {row['locationIP']} {row['browserUsed']} {row['LocationCityId']} {row['language']} {row['email']} {row['creationDate']}"
        #events.append(label_value_event)

        # Event: Create a separate event for each label change
        labels = ['firstName', 'lastName', 'gender', 'birthday', 'locationIP', 'browserUsed', 'LocationCityId', 'language', 'email', 'title', 'ModeratorPersonId']
        for label in labels:
            if label in row:
                if pd.notnull(row[label]):
                    label_change_event = f"Add attribute {row['id']} {category} {label} {row[label]} {row['creationDate']}"
                    events.append(label_change_event)

        # Event: Delete vertex at the deletionDate (if available)
        #if not pd.isnull(row['deletionDate']):
        if row['explicitlyDeleted'] == True :
            delete_vertex_event = f"delete vertex {row['id']} {category} {row['deletionDate']}"
            events.append(delete_vertex_event)
    print (len(events))
    return events

def transformNodes(output, input):
    # Specify the path to your CSV file and output file
    #csv_file_path = 'part-00000-405a2f0d-d21c-493d-b074-45a9e2a2d81e-c000.csv'
    #csv_file_path = input
    #output_file_path = 'eventsNodes.txt'
    output_file_path = output

    # Call the function to transform CSV to events
    # Iterate over all files in the directory
    for inputD in input:
        for filename in os.listdir(inputD):
            file_path = os.path.join(inputD, filename)
            if("Forum" in inputD):
                resulting_events = transform_csv_to_events(file_path, "Forum")
            elif ("Person" in inputD):
                resulting_events = transform_csv_to_events(file_path, "Person")

            # Save the resulting events into a file
            with open(output_file_path, 'a+') as output_file:
                for event in resulting_events:
                    output_file.write(f"{event}\n")

    print(f"Events saved to {output_file_path}")
