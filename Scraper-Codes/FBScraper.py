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
workbook = xlsxwriter.Workbook('scrapingData_'+str(targetPage)+'_FULL.xlsx') 
worksheet = workbook.add_worksheet() 

# Initialize from the first cell. 
# Rows and columns are zero indexed. 
row = 0
column = 0

#Search for the posts
for post in get_posts(str(targetPage), pages=noOfPages):
    # write operation perform 
    try: 
        if (len(post['text'])): #Check length of the post
            print("Scraping post #"+str(row)+": ")
            try:
                print(post['text'])
            except:
                print("Failed to print text")
            try:
                worksheet.write(row, column, post['text'])
                # incrementing the value of row by one 
                # with each iteratons. 
                row += 1
                print("-----Post saved------")
            #Show invalid post message
            except:
                print("------Invalid post! Failed to save post-------")
            print("")
    except:
        print("-------Post has no message. Skipping to the next post--------")
#Excel saved message
workbook.close()
#Debug message
print("Successfully saved as scrappingData_"+str(targetPage)+"_FULL.xlsx")
print("Total rows: "+str(row-1))#Total row message
