#encoding: utf8

from tree_search import *
from bayes_net import *
from constraintsearch import *

class MyTree(SearchTree):

    """
    Acrescentar novos nós à fila
      - Os novos nós são acrescentados à fila de forma a
        que sejam visitados por ordem crescente da função 
        de avaliação, sem no entanto afectar o princípio
        da pesquisa em profundidade
    """
    def banbou_add_to_open(self,lnewnodes):
        # IMPLEMENTAR AQUI
        pass


    """
    Suportar a estratégia de pesquisa "banbou"
      - O processo vai encontrar várias soluções e só termina
        quando a fila estiver vazia
      - Mantém-se registo da melhor solução encontrada
      - Quando um nó visitado tem uma função de avaliação superior ao
        custo da melhor solução já encontrada, esse nó é descartado
      - Quando se encontra uma solução com custo inferior
        ao da melhor solução anteriormente encontrada, regista-se a
        nova solução
      - Atribui valores aos atributos self.solution_cost 
        e self.tree_size
    """
    def search2(self):
        # IMPLEMENTAR AQUI
        pass
    
class MyBN(BayesNet):
    """
    Calcula a cobertura de Markov para uma dada
    variavel, na forma de uma lista contendo as variáveis 
    mães, as variáveis filhas e as outras mães das filhas
    """
    def markov_blanket(self,var):
        # IMPLEMENTAR AQUI
        pass


class MyCS(ConstraintSearch):
    """
    Calcula todas as soluções para um problema
    de satisfação de restrições.
    Optimiza de forma a encontrar cada solução
    apenas uma vez.
    """
    def search_all(self,domains=None,xpto=None):
        # Pode usar o argumento 'xpto' para passar mais
        # informação, caso precise
        #
        # IMPLEMENTAR AQUI
        pass



