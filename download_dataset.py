# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:46:02 2022

@author: yorkuniversity
"""

import pandas as pd 
import urllib.request

#-----------------------------------------------
def url_to_jpg(i, ids, urls):
    #name i desired to be 
    filename = 'photo/{}.jpg'.format(ids[i])
   # print(urls[i])
   
    try: 
        urllib.request.urlretrieve(urls[i],filename)
        print('{} saved from {}.'.format(filename,urls[i]))
    except:
        print('Warning: Could not download image {} from {}'.format(ids[i], urls[i]))
    return None

#-------------------------------------------

#set constants


FILENAME = 'data_file.csv'


#read  list of urls as pandas dataframe

urls= pd.read_csv(FILENAME)
print (urls["imageurl"])

#save the images to the directory by iterting through the list 

for i, url in enumerate(urls.values):
    url_to_jpg(i,urls["_unit_id"] , urls["imageurl"])