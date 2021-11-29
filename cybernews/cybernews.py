from bs4 import BeautifulSoup
import requests
import lxml
from random import shuffle


class CyberNews:    

    # Basic
    def basic(self):

        # Basic HackerNews Website and Tags
        basic_type = {'https://thehackernews.com/' : 'h2.home-title' , 'https://news.ycombinator.com/' : 'a.titlelink' , 'https://cyware.com/cyber-security-news-articles' : 'h1.cy-card__title.m-0.cursor-pointer.pb-3' , 'https://cybernews.com/news/' : 'h3.heading.heading_size_4'}

        news_data = []

        for key in basic_type:
            url = key
            response = requests.get(url , timeout=20)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(basic_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        shuffle(news_data)
        return news_data


    # Data Breach
    def dataBreach(self):

        # Data Breach HackerNews Website and Tags
        data_breach_type = {'https://thehackernews.com/search/label/data%20breach' : 'h2.home-title'}

        news_data = []

        for key in data_breach_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(data_breach_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data


    #  Cyber Attack
    def cyberAttack(self):

        # Cyber Attack HackerNews Website and Tags
        cyber_attack_type = {'https://thehackernews.com/search/label/Cyber%20Attack' : 'h2.home-title'}

        news_data = []

        for key in cyber_attack_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(cyber_attack_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data


    # Vulnerability
    def vulnerability(self):

        # Vulnerabilities HackerNews Website and Tags
        vulnerability_type = {'https://thehackernews.com/search/label/Vulnerability' : 'h2.home-title'}

        news_data = []

        for key in vulnerability_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(vulnerability_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data


    # Malware
    def malware(self):

        # Malware HackerNews Website and Tags
        malware_type = {'https://thehackernews.com/search/label/Malware' : 'h2.home-title'}

        news_data = []

        for key in malware_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(malware_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data


    # Security
    def security(self):

        # Security HackerNews Website and Tags
        security_type = {'https://cybernews.com/security/' : 'h3.heading.heading_size_4' , 'https://telecom.economictimes.indiatimes.com/tag/hacking' : '.descBx h3 a'}

        news_data = []

        for key in security_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(security_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data


    # Privacy
    def privacy(self):

        # Privacy HackerNews Website and Tags 
        privacy_type = {'https://cybernews.com/privacy/' : 'h3.heading.heading_size_4'}

        news_data = []

        for key in privacy_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(privacy_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data

    
    # Crypto
    def crypto(self):

        # Crypto HackerNews Website and Tags 
        crypto_type = {'https://cybernews.com/crypto/' : 'h3.heading.heading_size_4'}

        news_data = []

        for key in crypto_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(crypto_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data


    # Cloud
    def cloud(self):

        # Cloud HackerNews Website and Tags 
        cloud_type = {'https://cybernews.com/cloud/' : 'h3.heading.heading_size_4'}

        news_data = []

        for key in cloud_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(cloud_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data


    # Technology News
    def tech(self):

        # Tecchnology HackerNews Website and Tags 
        tech_type = {'https://telecom.economictimes.indiatimes.com/tag/digitalindia' : '.descBx h3 a'}

        news_data = []

        for key in tech_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(tech_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data