from  Fetch_api import fetch_data
import utils
from api_Details import api_board, api_Velocity

#Fetch Data using API
data_board = fetch_data(api_board)
data_velocity = fetch_data(api_Velocity)

#Extracting Specific Fields
if data_board:
    start_date = [data_board["values"][index]["startDate"][0:9] for index in range(len(data_board)+1)]
    end_date = [data_board["values"][index]["endDate"][0:9] for index in range(len(data_board)+1)]

if data_velocity:
    sprint_names = [sprint['name'] for sprint in data_velocity['sprints']]
    estimated_values = [data_velocity['velocityStatEntries'][str(sprint['id'])]['estimated']['value'] for sprint in data_velocity['sprints']]
    completed_values = [data_velocity['velocityStatEntries'][str(sprint['id'])]['completed']['value'] for sprint in data_velocity['sprints']]
else:
    print("No data")
    

# List in Row of Particular Sprints
data = []
for i in range(len(sprint_names)):
    row = []
    row.append(sprint_names[i])
    row.append(estimated_values[i])
    row.append(completed_values[i])
    row.append(start_date[i])
    row.append(end_date[i])
    row.append(completed_values[i])
    row.append((completed_values[i] / estimated_values[i]) * 100)
    
    data.append(row)
    
# Creating Excel File
utils.create_excel(data)
