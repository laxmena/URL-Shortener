# URL-Shortener

[URL shortening](https://en.wikipedia.org/wiki/URL_shortening) is a technique on the World Wide Web in which a Uniform Resource Locator (URL) may be made substantially shorter and still direct to the required page. This is achieved by using a redirect which links to the web page that has a long URL.

## How to Run Locally?
### Clone the Repository
```
git clone https://github.com/laxmena/URL-Shortener
```
### Install Dependencies
The project uses following tech stack:
* Python 2.7
* Django 1.11

To insatll dependencies, run
```
pip install -r requirements.txt
```

### Navigate to the Directory
Navigate to the Surukkam Directory by following this command
```
cd Surukkam
```

### Run the Applicaiton
```
python manage.py runserver 8000
```

### Open the WebApp in Browser
Open [http://localhost:8000/home](http://localhost:8000/home)
![URL-Shortner Home Page](https://github.com/laxmena/URL-Shortener/blob/master/Images/image1.png)

### Shorten URL
Enter a URL in the text box
![URL-Shortner URL Preview](https://github.com/laxmena/URL-Shortener/blob/master/Images/image2.png)

After submiting the form, the shortned URL will be generated.
![URL-Shortner Shortned-URL Preview](https://github.com/laxmena/URL-Shortener/blob/master/Images/image3.png)
