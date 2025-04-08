# Unit 10: Accessing Web Documents and APIs

In this unit you will learn to:
- Download and save web pages using Python
- Download and save images and multimedia
- Query application programming interfaces (API)

## 10.1 What is the World Wide Web?

The World Wide Web is an information space that is bound together by Internet connectivity and common communication protocols. The following happens when you visit a web page on your computer or phone:
- The web browser connects to the web server
- The web browser requests the resource (URL)
- The web server returns the resource, which could be HTML, an image, video, or anything even JSON
- The web browser renders the contents: displays links and images and videos, runs scripts, etc
- The web browser, at the user's direction or by following scripted instructions, gets more resources

The World Wide Web is not limited to transferring web pages, images or videos. Any form of data can be shared, as long as the user (human or program) knows the URL of the resource, and the user has the program or means to handle the resource once downloaded.

## 10.2 requests module

`requests` is a well-maintained and easy-to-use Python module to send and download data from the World Wide Web. If requests weren't installed from unit 1, we would install the module with the following command:

```cmd
pip install requests
```

## 10.3 Downloading a Web Page or Other Textual Data

```python
#! /usr/bin/env python
import sys
import requests

url = "https://www.google.com" # must include https:// or http://
html_file = "example.html"

with requests.session() as session:
    response = session.get(url) # This statement connects to the web server.
    print(f"Status: {response.status_code}", file = sys.stderr)

if response.status_code == 200: # success
    # At this point, the textual contents of the URL is stored in the string variable response.text
    # We can do anything with response.text, analyze it, print it. For now, let's just save it to a file.
    with open(html_file, "w", encoding = "utf-8") as output:
        output.write(response.text)
```

## 10.4 Text versus Binary Data

For various technical reasons, operating systems and programming languages make a distinction between textual data (HTML, CSV, JSON) and binary data (images, video, ZIP files.) What matters to us is that when we use Python to create a file, we have to tell Python whether we want text mode or binary mode. When we have written files so far in this course, we have used text mode. But if we use text mode to write binary data, the data will be corrupted.

## 10.5 Downloading Multimedia or Binary Data

```python
#! /usr/bin/env python
import sys
import requests

url = "https://www.fbi.gov/wanted/topten/alejandro-castillo/download.pdf" # must include https:// or http://
pdf_file = "example.pdf"

with requests.session() as session:
    response = session.get(url) # This statement connects to the web server.
    print(f"Status: {response.status_code}", file = sys.stderr)

if response.status_code == 200: # success
    # At this point, the binary contents of the URL is stored in the variable response.content
    # We can do anything with response.content. For now, let's just save it to a file.
    with open(pdf_file, "wb") as output: # mode "wb" is for write binary!
        output.write(response.content)
```

## 10.6 Application Programming Interfaces

The World Wide Web can be used to transfer any type of data, as long as someone knows the resource's URL and as long as someone or some program at the receiving end knows how to handle the data.

Originally the World Wide Web was used only to transfer HTML web pages, images and other media. For lots of technical reasons, developers found the World Wide Web to be a convenient mechanism to transfer, now, everything.

Many applications today that have nothing to do with web pages use the protocols and semantics of the World Wide Web information space to operate and to transfer their data, because it is technically convenient.

An Application Programming Interface (API) on the World Wide Web is a URL that returns data. The particulars of the request and response are decided by the developers. Some APIs require authentication. And many APIs on the World Wide Web return data in the JSON format.

Some APIs are not intended for broad use. The Apple BSSID locator API is one such example. This API is intended to be used by Apple devices, and the API is not publicly documented by Apple. But smart researchers reverse engineered the API.

APIs intended for use by the public are documented by their operator, so that developers know how to interact with the API.

### 10.6.1 Cryptocurrency Price API

We will access a free, publicly available API that returns cryptocurrency prices. [The API documentation is here.](https://docs.coingecko.com/reference/simple-price)

```python
import requests

params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
api_url = "https://api.coingecko.com/api/v3/simple/price"
with requests.session() as session:
    r = session.get(api_url, params = params)
print(r.text)
```

This is JSON! The `requests module has a convenience function that parses the response text into JSON.

## 10.7 Homework

Finish the following program that queries the CoinGecko API by processing the JSON output. Print the cryptocurrencies and prices in a way suitable for humans.

```python
import requests

params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
api_url = "https://api.coingecko.com/api/v3/simple/price"
with requests.session() as session:
    r = session.get(api_url, params = params)
    if r.status_code == 200:
        # At this point, the variable r.text contains the text of the response, which is in the JSON format.
        print(r.text)

        # We can use a convenience function to convert the JSON response into a Python object.
        data = r.json()
        # At this point, the variable data is the Python representation of the JSON returned by the server
```

## 10.8 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- How Python programs can access information on the World Wide Web
- The distinction between text and binary modes when reading and writing files
- The role of application programming interfaces
