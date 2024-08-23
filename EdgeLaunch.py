#====== Jack 2024 Aug.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#============================
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import os
import requests
from urllib.parse import urljoin
#============================

op = Options()
download_dir = os.path.join(os.getcwd(), 'downloads')  # Specify the download directory
preferences = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}

op.add_experimental_option("prefs", preferences)
edge = webdriver.Edge(options=op)      #edge = webdriver.Edge()
#============================

directory_url = 'example.com'
edge.get(directory_url)
links = edge.find_elements(By.XPATH, '//table/tbody/tr/td[@class="n"]/a')

download_dir = os.path.join(os.getcwd(), 'downloads')
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

for index, link in enumerate(links):
    if index == 0:
        continue  # Skip the first file link
    file_name = link.get_attribute('href').split('/')[-1]
    file_url = urljoin(directory_url, link.get_attribute('href'))
    file_path = os.path.join(download_dir, file_name)
    
    print(file_path)    

    # Download the file
    response = requests.get(file_url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    
    print(f"Downloaded: {file_name}")

time.sleep(5)
edge.quit()
