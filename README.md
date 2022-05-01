# Methods-of-collecting-and-processing-data-from-the-Internet
# Basics of client-server interaction. Working with the API
1. View the documentation for the GitHub API, figure out how to display a list of repositories for a specific user, save the JSON output in a *.json file.
2. Examine the list of open APIs (https://www.programmableweb.com/category/all/apis ). Find among them any that requires authorization (of any type). Execute requests to it by passing authorization. Write the server response to a file.
# HTML parsing. The Beautiful soup library
It is necessary to collect information about vacancies for the position being entered (using input or using arguments to get a position) from the HH (required) and/or Superjob sites (optional). The application must analyze several pages of the site (also input via input or arguments). The resulting list should contain at least:
The name of the vacancy.
The proposed salary (we put it in three fields: minimum and maximum and currency. convert numbers to numbers).
A link to the vacancy itself.
The site from where the vacancy was collected.
Optionally, you can add more job parameters (for example, employer and location). The structure should be the same for vacancies from both sites. The overall result can be output using dataFrame via pandas. Save it in json or csv.
# MongoDB Database Management System in Python
1. Deploy MongoDB on your computer/virtual machine/hosting and implement a function that will add only new vacancies/products to your database.
2. Write a function that searches for and displays vacancies with a salary greater than the entered amount (it is necessary to analyze both salary fields). For those who completed the task with Roskontrol, write a request to search for products with a rating not lower than the one entered or a quality not lower than the one entered (that is, one digit is entered, and the request checks both fields)
# HTML parsing. XPath
Write an application that collects the main news from the site to choose from news.mail.ru , lenta.ru , yandex-news. Use XPath for parsing. The data structure should contain:
the name of the source;
name of the news;
link to the news;
date of publication.
Add the collected news to the database
# Selenium in Python
Write a program that collects incoming emails from your own or test mailbox and add the data about the emails to the database (from whom, the date of sending, the subject of the letter, the full text of the letter)
The login of the test mailbox: gb_students_787@mail.ru
Test box password: Gfhjkmlkzcneltynjd001#
# The Scrapy framework. Acquaintance
Option I
1) Modify the spider in the existing project so that it forms an item according to the structure:
*Name of the vacancy
*Salary from
*Salary up
to *Link to the vacancy itself
And put all the records in the database (any)

2) Create a second spider in the existing project to collect vacancies from the superjob website. The spider should form items according to a similar structure and add data to the database as well.
# The Scrapy framework. Downloading files and photos
1) Take any category of goods on the Leroy Merlin website. Collect the following data:
● Name;
● all photos;
● Link;
● Price.

Implement data cleaning and transformation using ItemLoader. Prices should be in the form of a numeric value.

Additionally:
2) Write a universal processor of product characteristics that will generate data regardless of their type and quantity.

3)Implement the storage of downloaded files in separate folders, each of which must correspond to the assembled product
# The Scrapy framework. Implementation of client-server interaction mechanisms
Creative task:
1. Choose any open data source
2. Collect data in the Mongo database
3. Perform extraction of the received data
