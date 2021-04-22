import requests
from bs4 import BeautifulSoup

'''
URL of the archive web-page which provides link to
all img lectures. It would have been tiring to
download each img manually.
In this example, we first crawl the webpage to extract
all the links and then download imgs.
'''

# specify the URL of the archive here
archive_url = "https://hirise-pds.lpl.arizona.edu/PDS/EDR/ESP/ORB_067200_067299/ESP_067299_1435/"

def get_img_links():
	
	# create response object
	r = requests.get(archive_url)
	
	# create beautiful-soup object
	soup = BeautifulSoup(r.content,'html.parser')
	
	# find all links on web-page
	links = soup.findAll('a')

	# filter the link sending with .IMG
	img_links = [archive_url + link['href'] for link in links if link['href'].endswith('IMG')]

	return img_links


def download_img_series(img_links):

	for link in img_links:

		'''iterate through all links in img_links
		and download them one by one'''
		
		# obtain filename by splitting url and getting
		# last string
		file_name = link.split('/')[-1]

		print( "Downloading file:%s"%file_name)
		
		# create response object
		r = requests.get(link, stream = True)
		
		# download started
		with open(file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024*1024):
				if chunk:
					f.write(chunk)
		
		print( "%s downloaded!\n"%file_name )

	print ("All files downloaded!")
	return


if __name__ == "__main__":

	# getting all img links
	img_links = get_img_links()

	# download all imgs
	download_img_series(img_links)
	

	
