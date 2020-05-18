# -*- coding: utf-8 -*-
            
import scrapy

from scrapy.linkextractors import LinkExtractor 

class VeredictItem(scrapy.Item):
    url= scrapy.Field()
    content = scrapy.Field()


class SentspiderSpider(scrapy.Spider):
    name = 'sentspider'
    allowed_domains = ['corteconstitucional.gov.co']
    start_urls = ['https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=0&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=1&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=2&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=3&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=4&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=5&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=6&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=7&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=8&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=9&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=10&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=11&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=12&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=13&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=14&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=15&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=16&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=17&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=18&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=19&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=20&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=21&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=22&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=23&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=24&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=25&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=',
    'https://www.corteconstitucional.gov.co/relatoria/radicador/buscar.php?vs=26184&pg=26&ponente=&demandado=&Sentencia=&Tipo=Sentencias&busqueda=&conector=AND&segundotema=&anios=Todos&proceso=']
    base_url = "https://www.corteconstitucional.gov.co"
        
    def parse(self, response): 
        """Method to parse the HTML table and extract the link to each verdict """
        
        links = LinkExtractor(allow_domains=self.allowed_domains).extract_links(response)

        for link in links:
          if not self.use_link(link.url):
            continue

          request = response.follow(link, callback=self.parse_links)
          yield request

    def use_link(self, url):
      return '/relatoria/' in url

    def parse_links(self, response):
        """Method to request a new HTML link to the server, extracted with the parse method"""
        content = ' '.join(response.xpath("//div/p[@class = 'MsoNormal'][not(contains(normalize-space(), '\u00a0'))]//text()").extract())
        content = content.replace('\r\n', ' ')
        yield VeredictItem(url= response.url, content= content)
           
