from Finder import Finder
from selenium import webdriver
from FindOnePage import FindOnePage
from FindMultiplePages import FindMultiplePages


class OLX:
  def __init__(self, filtro, path):
    self.filtro = filtro
    self.driver = webdriver.Chrome('./chromedriver')
    self.path = path

  def process(self):
    print("Iniciando processamento")

    produtos = FindMultiplePages().find(self.path, self.filtro, self.driver)

    # produtos = self.findOnePage()
    self.createCSV(produtos)

  def createCSV(self, produtos, arquivo='produtos.csv'):
    print("Salvando csv")
    print(produtos)
    with open(arquivo, 'w') as writer:
      writer.write("\"Titulo\",\"Valor\",\"Link\"\n")
      for produto in produtos:
        print(produto)
        try:
          writer.write("\"" + self.limpa(produto['nome']) + "\",\"" + self.limpa(produto['valor']) + "\",\"" + self.limpa(produto['link']) + "\"\n")
        except Exception as e:
          print("erro ecrevendo linha")
  def limpa(self, dado):
    try:
      return dado.replace('"','\"')
    except Exception as e:
      return ''
    

  def findOnePage(self):
    print("findOnePage")
    find = FindOnePage()
    return find.find(self.path, self.filtro, self.driver)


    # soup = BeautifulSoup(base_path, 'html.parser')

  def find(self, Finder, path, filtro):
    print("Procurando por finder na pah com filtro")

  def end(self):
    self.driver.quit()
