from bs4 import BeautifulSoup
import requests
import lxml
from random import shuffle


class CyberNews:    

    # Basic
    def basic(self):

        # Basic CyberNews Website and Tags
        basic_type = {'https://cio.economictimes.indiatimes.com/news/internet' : '.descBx h3 a' , 'https://news.ycombinator.com/' : 'a.titlelink' , 'https://cyware.com/cyber-security-news-articles' : 'h1.cy-card__title.m-0.cursor-pointer.pb-3' , 'https://cybernews.com/news/' : 'h3.heading.heading_size_4' , 'https://cybernews.com/editorial/' : 'h3.heading.heading_size_4'}

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

        # Data Breach CyberNews Website and Tags
        data_breach_type = {'https://www.databreachtoday.in/' : 'h2.title.top-none a' , 'https://thehackernews.com/search/label/data%20breach' : 'h2.home-title'}

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

        # Cyber Attack CyberNews Website and Tags
        cyber_attack_type = {'https://cyware.com/hacker-news' : 'h1.cy-card__title.m-0.cursor-pointer.pb-3' , 'https://thehackernews.com/search/label/Cyber%20Attack' : 'h2.home-title'}

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

        # Vulnerabilities CyberNews Website and Tags
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

        # Malware CyberNews Website and Tags
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

        # Security CyberNews Website and Tags
        security_type = {'https://cybernews.com/security/' : 'h3.heading.heading_size_4' , 'https://telecom.economictimes.indiatimes.com/tag/hacking' : '.descBx h3 a' , 'https://cio.economictimes.indiatimes.com/news/digital-security' : '.descBx h3 a'}

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

        # Privacy CyberNews Website and Tags 
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

        # Crypto CyberNews Website and Tags 
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

        # Cloud CyberNews Website and Tags 
        cloud_type = {'https://cybernews.com/cloud/' : 'h3.heading.heading_size_4' , 'https://cio.economictimes.indiatimes.com/news/cloud-computing' : '.descBx h3 a'}

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

        # Technology CyberNews Website and Tags 
        tech_type = {'https://telecom.economictimes.indiatimes.com/tag/digitalindia' : '.descBx h3 a' , 'https://cio.economictimes.indiatimes.com/tag/next+gen+tech' : '.descBx h3 a'}

        news_data = []

        for key in tech_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            news_links = soup.select(tech_type[key])
                
            for data in news_links:
                news_data.append(data.text.strip())
            
        return news_data

    # IOT News
    def iot(self):

        # IOT CyberNews Website and Tags 
        iot_type = {'https://cio.economictimes.indiatimes.com/news/internet-of-things' : '.descBx h3 a'}
        
        news_data = []

        for key in iot_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text , 'lxml')
            news_links = soup.select(iot_type[key])

            for data in news_links:
                news_data.append(data.text.strip())

        return news_data

    # Big Data News
    def bigData(self):

        # Big Data CyberNews Website and Tags 
        bigData_type = {'https://cio.economictimes.indiatimes.com/news/big-data' : '.descBx h3 a' , 'https://cio.economictimes.indiatimes.com/news/data-center' : '.descBx h3 a'}

        news_data = []

        for key in bigData_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text , 'lxml')
            news_links = soup.select(bigData_type[key])

            for data in news_links:
                news_data.append(data.text.strip())

        return news_data

    # Business Analytics News
    def business(self):

        # Business Analytics CyberNews Website and Tags 
        business_type = {'https://cio.economictimes.indiatimes.com/news/business-analytics' : '.descBx h3 a'}

        news_data = []

        for key in business_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text , 'lxml')
            news_links = soup.select(business_type[key])

            for data in news_links:
                news_data.append(data.text.strip())

        return news_data

    # Mobility News
    def mobility(self):

        # Mobility CyberNews Website and Tags 
        mobility_type = {'https://cio.economictimes.indiatimes.com/news/mobility' : '.descBx h3 a'}

        news_data = []

        for key in mobility_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text , 'lxml')
            news_links = soup.select(mobility_type[key])

            for data in news_links:
                news_data.append(data.text.strip())

        return news_data

    # Research News
    def research(self):

        # Research CyberNews Website and Tags 
        research_type = {'https://cio.economictimes.indiatimes.com/tag/research' : '.descBx h3 a'}

        news_data = []

        for key in research_type:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text , 'lxml')
            news_links = soup.select(research_type[key])

            for data in news_links:
                news_data.append(data.text.strip())

        return news_data

    # Corporate News
    def corporate(self):

        # Corporate CyberNews Website and Tags 
        corporate_news = {'https://cio.economictimes.indiatimes.com/news/corporate-news' : '.descBx h3 a'}

        news_data = []

        for key in corporate_news:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text , 'lxml')
            news_links = soup.select(corporate_news[key])

            for data in news_links:
                news_data.append(data.text.strip())

        return news_data

    # Social Media News
    def socialMedia(self):

        # Social Media CyberNews Website and Tags 
        social_news = {'https://cio.economictimes.indiatimes.com/news/social-media' : '.descBx h3 a'}

        news_data = []

        for key in social_news:
            url = key
            response = requests.get(url , timeout=10)
            soup = BeautifulSoup(response.text , 'lxml')
            news_links = soup.select(social_news[key])

            for data in news_links:
                news_data.append(data.text.strip())

        return news_data