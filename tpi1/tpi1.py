

from tree_search import *

from math import *

#generate all possible assignments
#of constants from 'lconsts' to the
#variables in 'lvars'
def assignments(lvars,lconsts):
    #IMPLEMENT HERE
    pass


class TSP(SearchDomain):
    #IMPLEMENT HERE
    pass

class MyTree(SearchTree):

    # add new nodes to the list of open_nodes
    # according to the uniform cost search startegy
    def uniform_add_to_open(self,lnewnodes):
        # IMPLEMENT HERE
        pass

    # add new nodes to the list of open_nodes
    # according to the A* search startegy
    def astar_add_to_open(self,lnewnodes):
        # IMPLEMENT HERE
        pass

    # search for a solution
    def search2(self):
        #IMPLEMENT HERE
        pass


# two shortcuts to solve TSP problems

def formulateTSP(domain,initial,tovisit):
    return SearchProblem(domain, ([],initial), (tovisit,initial))

def solveTSP(p,strategy):
    t = MyTree(p,strategy)
    solution = t.search2()
    return [city for (lv,city) in solution], t.tree_size, t.solution_cost


