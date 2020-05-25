# Collage_Life
#### The web site displays saved images and allows user to view location and category photos 
#### By **Waithera-m**
## Description
Collage_Life is a django application that allows users to view saved images as well as the details associated with different images. Users can also use location and category filters to see images associated with particular categories and locations.
## Setup/Installation Requirements
To use the application, users need internet access and web browsers, preferably  Chrome, Safari, and Firefox.
## Set-Up a Local Project
* Fork the repository
* Clone the repository
    ```$ git clone  https://github.com/Waithera-m/collage_life.git```
* Activate a virtual environment
    ```$ python3.8 -m venv virtual```
* Install all prerequisites
    ```$ pip install -r requirements.txt```
* Create file to store sensitive environment variables 
## Known Bugs
* The copy button does not work; therefore users have to manually select and copy the image urls
## Behavior Driven Development (BDD)
#### Landing Page
![image](https://user-images.githubusercontent.com/60571734/82829938-25e51880-9ebd-11ea-96b8-fc18403c1347.png)

#### Category Specific Page
![image](https://user-images.githubusercontent.com/60571734/82830048-5d53c500-9ebd-11ea-8f90-01c8bdf0beb9.png)

#### Filter By Location Page
![image](https://user-images.githubusercontent.com/60571734/82830108-85dbbf00-9ebd-11ea-92b4-204bc88a29b3.png)

#### Results Page
![image](https://user-images.githubusercontent.com/60571734/82830174-ad328c00-9ebd-11ea-94a8-1377fd14934d.png)


|Behavior                |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads |Users scroll | Users see different photos that are neither category nor location specific|
|The landing page loads|Users click on any image|Modal which displays a larger image and image details pops up|
|The landing page loads|Users click on any link in the categories drop down menu |Users are directed to the view that displays all images asociated with the chose category|
|The landing page loads|Users click on filter by location navbar link|Users are directed to view that displays images without locations and a list of available locations|
|The filter by location page loads|Users click on any of the available locations|Users are directed to view that displays images associated with the chosen location|
|The landing page loads|Users type search term in the navbar form|Users are directed to results page which displays the number and images associated with the entered search term|
## Technologies Used
* HTML - HTML was used to dictate the structure of views.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Javascript - The high-level programming language was used to create a function to support the copy to clipboard feature
* Python 3.8.2 - The language was used to create classes, testcases, and functions to retrieve data 
* [django 3.0.6](https://www.djangoproject.com/) - django is a Python web framework.The framework's apps, urls, and views were used to refactor code and promote code maintenance. Inbuilt filters,classes, and methods were used to initialize the created app and installed extensions and loop through and display saved imagesand navigate to different views. 
## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creator via this email address: njihiamary11@gmail.com
## Demo
You can view changes made to the website by visiting this working live demo: https://collage-life.herokuapp.com/
### License
*MIT*
MIT License Copyright (c) 2020 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) 2020 **Waithera-m**