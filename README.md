<h1>cybernews</h1>
A package and an API that provides you Latest Cyber and Hacking News from websites using Web-Scraping.

``
Public REST API :- https://cyber-news-api.herokuapp.com/
``

<h2>Features :-</h2>


```
 News Headlines
 Full News
 News Article URL
 News Image
```
<br>
Developed by GhoulBond (c) 2021<br><br>

<h2>Setup</h2>


<h3>For Window Users</h3>

```python
pip install cybernews 
```

<h3>For Linux/Mac Users</h3>

```python
pip3 install cybernews
```

<h2>Use</h2>

```python
from cybernews import cybernews
news = cybernews.CyberNews() #Instance is created
```

<h2>All Functionalities</h2>

```python
from cybernews import cybernews
news = cybernews.CyberNews() #Instance is created

# Return type of all functions is list

news.basic() # Returns all Latest basic cyber news

news.dataBreach() # Returns Latest news only related to Data Breach

news.cyberAttack() # Returns Latest news only related to Cyber Attack

news.vulnerability() # Returns Latest news only related to Vulnerabilities

news.malware() # Returns Latest news only related to Malware

news.security() # Returns Latest news only related to Security

news.privacy() # Returns Latest news only related to Privacy

news.crypto() # Returns Latest news only related to Crypto

news.cloud() # Returns Latest news only related to Cloud

news.tech() # Returns Latest news only related to Technology

news.iot() # Returns Latest news only related to Internet of Things

news.bigData() # Returns Latest news only related to BigData

news.business() # Returns Latest news only related to Business

news.mobility() # Returns Latest news only related to Mobility

news.research() # Returns Latest news only related to Research

news.corporate() # Returns Latest news only related to Corporate

news.socialMedia() # Returns Latest news only related to Social Media
```