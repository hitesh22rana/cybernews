from bs4 import BeautifulSoup
import requests
import lxml
from random import shuffle

session = requests.session()

class CyberNews:    

    # Headers For Performance
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36' , 'Content-Type': 'application/json; charset=utf-8'}

    # Basic News
    def basic(self):

        # Basic CyberNews Website and Tags
        basic_news_type = [
           {'https://cio.economictimes.indiatimes.com/news/internet' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}} ,
           {'https://cybernews.com/news/' : {'headlines' : 'h3.heading.heading_size_4' , 'author' : 'a.link.text.text_color_important' , 'fullNews' : '.text.text_size_small.text_line-height_big' , 'newsImg' : '.cells__item a img' , 'newsURL' : '.cells__item.cells__item_width a.link'}} ,
           {'https://cybernews.com/editorial/' : {'headlines' : 'h3.heading.heading_size_4' , 'author' : 'a.link.text.text_color_important' , 'fullNews' : '.text.text_size_small.text_line-height_big' , 'newsImg' : '.cells__item a img' , 'newsURL' : '.cells__item.cells__item_width a.link'}}
        ]

        news_data = []
        
        for basic_news in basic_news_type:
            for key in basic_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(basic_news[key]['headlines'])
                news_author = soup.select(basic_news[key]['author'])
                news_fullNews = soup.select(basic_news[key]['fullNews'])
                news_URL = soup.select(basic_news[key]['newsURL'])
                news_img_URL = soup.select(basic_news[key]['newsImg'])
   
                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
                
        shuffle(news_data)
        return news_data


    # Data Breach News
    def dataBreach(self):

        # Data Breach CyberNews Website and Tags
        data_breach_news_type = [
            {'https://thehackernews.com/search/label/data%20breach' : {'headlines' : 'h2.home-title' , 'author' : '.item-label span' , 'fullNews' : '.home-desc' , 'newsImg' : '.img-ratio img' , 'newsURL' : 'a.story-link'}}
        ]

        news_data = []
        
        for data_breach_news in data_breach_news_type:
            for key in data_breach_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(data_breach_news[key]['headlines'])
                news_author = soup.select(data_breach_news[key]['author'])
                news_fullNews = soup.select(data_breach_news[key]['fullNews'])
                news_URL = soup.select(data_breach_news[key]['newsURL'])
                news_img_URL = soup.select(data_breach_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
            
        shuffle(news_data)
        return news_data


    #  Cyber Attack News
    def cyberAttack(self):

        # Cyber Attack CyberNews Website and Tags
        cyber_attack_news_type = [
            {'https://thehackernews.com/search/label/Cyber%20Attack' : {'headlines' : 'h2.home-title' , 'author' : '.item-label span' , 'fullNews' : '.home-desc' , 'newsImg' : '.img-ratio img' , 'newsURL' : 'a.story-link'}}
        ]

        news_data = []
        
        for cyber_attack_news in cyber_attack_news_type:
            for key in cyber_attack_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(cyber_attack_news[key]['headlines'])
                news_author = soup.select(cyber_attack_news[key]['author'])
                news_fullNews = soup.select(cyber_attack_news[key]['fullNews'])
                news_URL = soup.select(cyber_attack_news[key]['newsURL'])
                news_img_URL = soup.select(cyber_attack_news[key]['newsImg'])
                
                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
            
        shuffle(news_data)
        return news_data


    # Vulnerability News
    def vulnerability(self):

        # Vulnerabilities CyberNews Website and Tags
        vulnerability_news_type = [
            {'https://thehackernews.com/search/label/Vulnerability' : {'headlines' : 'h2.home-title' , 'author' : '.item-label span' , 'fullNews' : '.home-desc' , 'newsImg' : '.img-ratio img' , 'newsURL' : 'a.story-link'}}
        ]

        news_data = []
        
        for vulnerability_news in vulnerability_news_type:
            for key in vulnerability_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(vulnerability_news[key]['headlines'])
                news_author = soup.select(vulnerability_news[key]['author'])
                news_fullNews = soup.select(vulnerability_news[key]['fullNews'])
                news_URL = soup.select(vulnerability_news[key]['newsURL'])
                news_img_URL = soup.select(vulnerability_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
                
        shuffle(news_data)
        return news_data


    # Malware News
    def malware(self):

        # Malware CyberNews Website and Tags
        malware_news_type = [
            {'https://thehackernews.com/search/label/Malware' : {'headlines' : 'h2.home-title' , 'author' : '.item-label span' , 'fullNews' : '.home-desc' , 'newsImg' : '.img-ratio img' , 'newsURL' : 'a.story-link'}}
    ]

        news_data = []
        
        for malware_news in malware_news_type:
            for key in malware_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(malware_news[key]['headlines'])
                news_author = soup.select(malware_news[key]['author'])
                news_fullNews = soup.select(malware_news[key]['fullNews'])
                news_URL = soup.select(malware_news[key]['newsURL'])
                news_img_URL = soup.select(malware_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
            
        shuffle(news_data)
        return news_data


    # Security News
    def security(self):

        # Security CyberNews Website and Tags
        security_news_type = [
            {'https://cybernews.com/security/' : {'headlines' : 'h3.heading.heading_size_4' , 'author' : 'a.link.text.text_color_important' , 'fullNews' : '.text.text_size_small.text_line-height_big' , 'newsImg' : '.cells__item a img' , 'newsURL' : '.cells__item.cells__item_width a.link'}} , 
            {'https://telecom.economictimes.indiatimes.com/tag/hacking' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' ,'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}} ,
            {'https://cio.economictimes.indiatimes.com/news/digital-security' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []
        
        for security_news in security_news_type:
            for key in security_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(security_news[key]['headlines'])
                news_author = soup.select(security_news[key]['author'])
                news_fullNews = soup.select(security_news[key]['fullNews'])
                news_URL = soup.select(security_news[key]['newsURL'])
                news_img_URL = soup.select(security_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
                
        shuffle(news_data)
        return news_data


    # Privacy News
    def privacy(self):

        # Privacy CyberNews Website and Tags 
        privacy_news_type = [
            {'https://cybernews.com/privacy/' : {'headlines' : 'h3.heading.heading_size_4' , 'author' : 'a.link.text.text_color_important' , 'fullNews' : '.text.text_size_small.text_line-height_big' , 'newsImg' : '.cells__item a img' , 'newsURL' : '.cells__item.cells__item_width a.link'}}
        ]

        news_data = []
        
        for privacy_news in privacy_news_type:
            for key in privacy_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(privacy_news[key]['headlines'])
                news_author = soup.select(privacy_news[key]['author'])
                news_fullNews = soup.select(privacy_news[key]['fullNews'])
                news_URL = soup.select(privacy_news[key]['newsURL'])
                news_img_URL = soup.select(privacy_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
            
        shuffle(news_data)
        return news_data

    
    # Crypto News
    def crypto(self):

        # Crypto CyberNews Website and Tags 
        crypto_news_type = [
            {'https://cybernews.com/crypto/' : {'headlines' : 'h3.heading.heading_size_4' , 'author' : 'a.link.text.text_color_important' , 'fullNews' : '.text.text_size_small.text_line-height_big' , 'newsImg' : '.cells__item a img' , 'newsURL' : '.cells__item.cells__item_width a.link'}}
        ]

        news_data = []
        
        for crypto_news in crypto_news_type:
            for key in crypto_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(crypto_news[key]['headlines'])
                news_author = soup.select(crypto_news[key]['author'])
                news_fullNews = soup.select(crypto_news[key]['fullNews'])
                news_URL = soup.select(crypto_news[key]['newsURL'])
                news_img_URL = soup.select(crypto_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
            
        shuffle(news_data)
        return news_data


    # Cloud News
    def cloud(self):

        # Cloud CyberNews Website and Tags 
        cloud_news_type = [
            {'https://cybernews.com/cloud/' : {'headlines' : 'h3.heading.heading_size_4' , 'author' : 'a.link.text.text_color_important' , 'fullNews' : '.text.text_size_small.text_line-height_big' , 'newsImg' : '.cells__item a img' , 'newsURL' : '.cells__item.cells__item_width a.link'}} ,
            {'https://cio.economictimes.indiatimes.com/news/cloud-computing' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []

        for cloud_news in cloud_news_type:      
            for key in cloud_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(cloud_news[key]['headlines'])
                news_author = soup.select(cloud_news[key]['author'])
                news_fullNews = soup.select(cloud_news[key]['fullNews'])
                news_URL = soup.select(cloud_news[key]['newsURL'])
                news_img_URL = soup.select(cloud_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

            
        shuffle(news_data)
        return news_data


    # Technology News
    def tech(self):

        # Technology CyberNews Website and Tags 
        tech_news_type = [
            {'https://telecom.economictimes.indiatimes.com/tag/digitalindia' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}} ,
            {'https://cio.economictimes.indiatimes.com/tag/next+gen+tech' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []
        
        for tech_news in tech_news_type:
            for key in tech_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(tech_news[key]['headlines'])
                news_author = soup.select(tech_news[key]['author'])
                news_fullNews = soup.select(tech_news[key]['fullNews'])
                news_URL = soup.select(tech_news[key]['newsURL'])
                news_img_URL = soup.select(tech_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

            
        shuffle(news_data)
        return news_data

    # IOT News
    def iot(self):

        # IOT CyberNews Website and Tags 
        iot_news_type = [
            {'https://cio.economictimes.indiatimes.com/news/internet-of-things' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []
        
        for iot_news in iot_news_type:
            for key in iot_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(iot_news[key]['headlines'])
                news_author = soup.select(iot_news[key]['author'])
                news_fullNews = soup.select(iot_news[key]['fullNews'])
                news_URL = soup.select(iot_news[key]['newsURL'])
                news_img_URL = soup.select(iot_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

        shuffle(news_data)
        return news_data

    # Big Data News
    def bigData(self):

        # Big Data CyberNews Website and Tags 
        bigData_news_type = [
            {'https://cio.economictimes.indiatimes.com/news/big-data' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}} , 
            {'https://cio.economictimes.indiatimes.com/news/data-center' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []
        
        for bigData_news in bigData_news_type:
            for key in bigData_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(bigData_news[key]['headlines'])
                news_author = soup.select(bigData_news[key]['author'])
                news_fullNews = soup.select(bigData_news[key]['fullNews'])
                news_URL = soup.select(bigData_news[key]['newsURL'])
                news_img_URL = soup.select(bigData_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

        shuffle(news_data)
        return news_data

    # Business Analytics News
    def business(self):

        # Business Analytics CyberNews Website and Tags 
        business_news_type = [
            {'https://cio.economictimes.indiatimes.com/news/business-analytics' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []
        
        for business_news in business_news_type:
            for key in business_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(business_news[key]['headlines'])
                news_author = soup.select(business_news[key]['author'])
                news_fullNews = soup.select(business_news[key]['fullNews'])
                news_URL = soup.select(business_news[key]['newsURL'])
                news_img_URL = soup.select(business_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

        shuffle(news_data)
        return news_data

    # Mobility News
    def mobility(self):

        # Mobility CyberNews Website and Tags 
        mobility_news_type = [
            {'https://cio.economictimes.indiatimes.com/news/mobility' : {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []
        
        for mobility_news in mobility_news_type:
            for key in mobility_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(mobility_news[key]['headlines'])
                news_author = soup.select(mobility_news[key]['author'])
                news_fullNews = soup.select(mobility_news[key]['fullNews'])
                news_URL = soup.select(mobility_news[key]['newsURL'])
                news_img_URL = soup.select(mobility_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

        shuffle(news_data)
        return news_data

    # Research News
    def research(self):

        # Research CyberNews Website and Tags 
        research_news_type = [{'https://cio.economictimes.indiatimes.com/tag/research' : 
                {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []

        for research_news in research_news_type:
            for key in research_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(research_news[key]['headlines'])
                news_author = soup.select(research_news[key]['author'])
                news_fullNews = soup.select(research_news[key]['fullNews'])
                news_URL = soup.select(research_news[key]['newsURL'])
                news_img_URL = soup.select(research_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

        shuffle(news_data)
        return news_data 

    # Corporate News
    def corporate(self):

        # Corporate CyberNews Website and Tags 
        corporate_news_type = [{'https://cio.economictimes.indiatimes.com/news/corporate-news' : 
                {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []

        for corporate_news in corporate_news_type:
            for key in corporate_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(corporate_news[key]['headlines'])
                news_author = soup.select(corporate_news[key]['author'])
                news_fullNews = soup.select(corporate_news[key]['fullNews'])
                news_URL = soup.select(corporate_news[key]['newsURL'])
                news_img_URL = soup.select(corporate_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip(),
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)
                    
        shuffle(news_data)
        return news_data            


    # Social Media News
    def socialMedia(self):

       # Social Media CyberNews Website and Tags 
        social_news_type = [{'https://cio.economictimes.indiatimes.com/news/social-media' : 
            {'headlines' : '.descBx h3 a' , 'author' : '.metaTx' , 'fullNews' : '.descBx p' , 'newsImg' : 'figure.avtar a img' , 'newsURL' : '.descBx a'}}
        ]

        news_data = []

        for social_news in social_news_type:
            for key in social_news:
                url = key
                response = session.get(url , timeout=10 , headers=self.headers)
                soup = BeautifulSoup(response.text , 'lxml')
                news_headlines = soup.select(social_news[key]['headlines'])
                news_author = soup.select(social_news[key]['author'])
                news_fullNews = soup.select(social_news[key]['fullNews'])
                news_URL = soup.select(social_news[key]['newsURL'])
                news_img_URL = soup.select(social_news[key]['newsImg'])

                for index in range(len(news_headlines)):

                    complete_news = {'headlines' : news_headlines[index].text.strip() ,
                                    'author' : news_author[index].text.strip(),
                                    'fullNews' : news_fullNews[index].text.strip(),
                                    'newsURL' : news_URL[index]['href'],
                                    'newsImgURL' : news_img_URL[index]['data-src']
                    }

                    news_data.append(complete_news)

        shuffle(news_data)
        return news_data