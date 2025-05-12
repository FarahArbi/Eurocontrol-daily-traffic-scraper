from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

url = 'https://www.eurocontrol.int/Economics/DailyTrafficVariation-States.html'
driver.get(url)

time.sleep(5)  # Adjust based on the page loading time

soup = BeautifulSoup(driver.page_source, 'html.parser')

chart_div = soup.find('div', {'id': 'MyGeoEntityChart_div'})

if chart_div:
    table = chart_div.find('table')
    date = chart_div.find('text', {'text-anchor': 'start'})
    print (date.get_text())
    
    if table:
        headers = [th.text.strip() for th in table.find('thead').find_all('th')]

        rows = []
        for tr in table.find('tbody').find_all('tr'):
            cells = [td.text.strip() for td in tr.find_all('td')]
            rows.append(cells)

        # Create a DataFrame from the scraped data
        df_flights = pd.DataFrame(rows, columns=headers)

        df_flights.to_csv(f"{date.get_text()}.csv", index=False)  # Save the DataFrame to a CSV file

        print(df_flights)
    else:
        print("Table not found inside chart_div.")
else:
    print("Chart div not found.")

# Close the driver session
driver.quit()
