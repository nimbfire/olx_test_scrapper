import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from Finder import Finder
from OLX import OLX
from FindMultiplePages import FindMultiplePages
from FindOnePage import FindOnePage

print('Iniciando busca')

base_path = 'https://rs.olx.com.br/?'
base_path_com_filtro = 'https://rs.olx.com.br/?q=gameboy'

olx = OLX('playstation', path=base_path)
olx.process()
olx.end()