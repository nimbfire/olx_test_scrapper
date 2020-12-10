from Finder import Finder
from FindOnePage import FindOnePage

class FindMultiplePages(Finder):
  '''
  Procura em apenas uma página
  '''

  def find(self, path, filtro, driver):
    '''
    Procura em várias paginas
    retorna uma lista de anuncios ()dicionários {titulo, valor, link} 
    que pode estar vazia
    '''
    print(f'Procura por {filtro} no path: {path}')

    find = FindOnePage()
    retorno = []

    parcial = find.find(path, filtro, driver)
    retorno = retorno + parcial

    i = 1
    while i < 10:
      i += 1
      new_path = path + 'o=' + str(i) + '&'
      parcial = find.find(new_path, filtro, driver)
      retorno = retorno + parcial
      pass

    # print(retorno)
    return retorno
