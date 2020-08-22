#Import related stuffs
import requests
from bs4 import BeautifulSoup
import lxml
import xlsxwriter
from facebook_scraper import get_posts

#Prompt for input
targetPage  = input("Target facebook page to scrape: ")
noOfPages = int(input("Number of pages: "))

#Set up workbook/worksheet
workbook = xlsxwriter.Workbook('scrappingData_'+str(targetPage)+'_FULL.xlsx') 
worksheet = workbook.add_worksheet() 

# Initialize from the first cell. 
# Rows and columns are zero indexed. 
row = 0
column = 0

#Search for the posts
try:
    for post in get_posts(str(targetPage), pages=noOfPages):
        print("Saving post #"+str(row)+": "+post['text'][:50])
        # write operation perform 
        worksheet.write(row, column, post['text'])
        # incrementing the value of row by one 
        # with each iteratons. 
        row += 1
          
    workbook.close()

#Show invalid message
except:
    print("Invalid page!")
