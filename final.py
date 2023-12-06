import csv
import plotly.express as px

if __name__ == '__main__':
    # Specify the path to your CSV file
    csv_file_path = 'finalcsv.csv'
    csv_data = []
    suspicious_person = 'Richard Fox'
    # Open the CSV file and read its contents
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file)

        # Iterate through each row in the CSV file and append to the list
        for row in csv_reader:
            csv_data.append(row)
    temp = []
    update = []

    for line in csv_data:
        if len(line) != 0:
            update.append(line)
    for line in update:
        date_string = line[3]
        month = date_string[5:7]
        year = date_string[:4]
        if line[0] == suspicious_person:
            temp_node = [line[1], line[2], month, year, line[3], "The Target"]
            temp.append(temp_node)
        elif line[1] == suspicious_person:
            temp_node = [line[0], line[2], month, year, line[3], "The Source"]
            temp.append(temp_node)
    data = []
    for line in temp:
        half = "Second Half"
        if int(line[2]) < 6:
            half = "First Half"
        year = int(line[3])
        name = line[0]
        type = line[1]
        time = line[4]
        sot = line[5]
        temp_node = {"center": suspicious_person,
                     "node": name,
                     "type": type,
                     "half": half,
                     "year": year,
                     "time": time,
                     "source_or_target":sot}
        data.append(temp_node)
        # Define custom colors for nodes
        colors = {
            "(?)":  "jade",
            "calls": "blue",
            "meetings": "green",
            "purchases": "red",
            "emails": "purple",
        }
    # Create sunburst chart
    fig = px.sunburst(data, path=["center", 'year', 'half', 'type', 'node'], color='type', color_discrete_map=colors,
                      values='year', branchvalues='total')

    # Update layout for better visibility
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30))

    # Show the plot
    fig.show()
