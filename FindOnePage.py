from Finder import Finder
from bs4 import BeautifulSoup


class FindOnePage(Finder):
  '''
  Procura em apenas uma página
  '''

  def find(self, path, filtro, driver):
    '''
    Procura em apenas uma página
    retorna uma lista de anuncios ()dicionários {titulo, valor, link} 
    que pode estar vazia
    '''
    print(f'Procura por {filtro} no path: {path}')

    retorno = []

    path_with_filter = path + 'q=' + filtro
    driver.get(path_with_filter)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    anuncios = soup.select('#ad-list li')

    if anuncios:
      for anuncio in anuncios:

        # print(anuncio)
        anuncio_soup = BeautifulSoup(str(anuncio), 'lxml')
        try:
          h2 = anuncio_soup.h2.string
          print(h2)
          price = anuncio_soup.find(attrs={"color": "graphite"})
          price = price.string
          print(price)
          link = anuncio_soup.a

          print(link['href'])
          produto = {
            'nome': h2,
            'valor': price,
            'link': link['href']
          }
          retorno.append(produto)
        except Exception as e:
          # print('titulo não encontrado')
          pass

    # print(retorno)
    return retorno
