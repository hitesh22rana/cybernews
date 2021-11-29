<h1>cybernews</h1>
A package that provides you Latest Cyber/Hacker News from website using Web-Scraping.
Latest Cyber/Hacker News Using Webscraping<br><br>
Developed by GhoulBond (c) 2021<br><br>

<h2>Setup</h2>

``
For Window Users
``

```python
pip install cybernews 
```

``
For Linux/Mac Users
``

```python
pip3 install cybernews
```

<h2>Use</h2>

```python
from cybernews import cybernews
news = cybernews.CyberNews() #Instace is created
```

<h2>All Functionalities</h2>

```python
from cybernews import cybernews
news = cybernews.CyberNews() #Instace is created

# Return type of all functions is list format

news.basic() # Returns all Latest basic cyber news

news.dataBreach() # Return's Latest news only related to Data Breach's

news.cyberAttack() # Return's Latest news only related to Cyber Attack's

news.vulnerability() # Return's Latest news only related to Vulnerabilities

news.malware() # Return's Latest news only related to Malware's

news.security() # Return's Latest news only related to Security

news.privacy() # Return's Latest news only related to Privacy

news.crypto() # Return's Latest news only related to Crypto

news.cloud() # Return's Latest news only related to Cloud
```