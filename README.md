<h1>cybernews</h1>
A package that provides you Latest Cyber and Hacking News from Websites using Web-Scraping.
<br><br>
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
```