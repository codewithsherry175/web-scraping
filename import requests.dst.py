import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ul.ie/scieng/department-computer-science-and-information-systems-staff"

print("Connecting to University of Limerick...")

try:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    
    faculty_list = []
    for link in soup.find_all('a'):
        name_text = link.text.strip()
        if any(title in name_text for title in ["Dr", "Prof", "Professor", "Lecturer"]):
            faculty_list.append(name_text)

    faculty_list = list(set(faculty_list))

    
    df = pd.DataFrame(faculty_list, columns=['Name'])
    df['Department'] = 'Computer Science'
    df['Qualification'] = 'PhD' # You can edit these later
    df['Gender'] = 'TBD'        # To be determined for charts

   
    df.to_csv('university_data.csv', index=False)

    print(f"Success! Found {len(faculty_list)} faculty members.")
    print("Data saved to 'university_data.csv'. You can open this in Excel!")
    print(df.head()) # Shows the first 5 names

except Exception as e:
    print(f"An error occurred: {e}")