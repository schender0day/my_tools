import requests
from bs4 import BeautifulSoup
import wget

# The URL of the lecture page
url = 'https://learn.cantrill.io/courses/895720/lectures/17313105'

# Set the headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Make the request to the lecture page
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the video URL within the HTML
video_url = soup.find('source')['src']

# Download the video file using wget
filename = wget.download(video_url)

print(f'Download complete. File saved as {filename}')
