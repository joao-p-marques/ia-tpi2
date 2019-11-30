

from semantic_network import *
from bayes_net import *


class MySN(SemanticNetwork):


    def query_dependents(self, entity, recursion=False):
        lst = []
        for d in self.declarations:
            # list of direct dependents
            if isinstance(d.relation, Depends) and d.relation.entity2 == entity:
                # recurse direct dependents
                lst += self.query_dependents(d.relation.entity1, recursion=True) # recursion is True so we can add subtypes of dependents
                # check if element is not supertype
                if not d.relation.entity1 in [decl.relation.entity2 for decl in self.declarations if isinstance(decl.relation, Subtype)]:
                    lst.append(d.relation.entity1)
            # if element has subtypes
            if isinstance(d.relation, Subtype) and d.relation.entity2 == entity:
                # see if subtypes have dependents
                lst += self.query_dependents(d.relation.entity1, recursion=False)
                # if we come from a dependant
                if recursion:
                    lst.append(d.relation.entity1)
        return list(set(lst))

    def query_causes(self, entity, recursion=False):
        lst = []
        for d in self.declarations:
            # list of direct causes
            if isinstance(d.relation, Depends) and d.relation.entity1 == entity:
                # append cause
                lst.append(d.relation.entity2)
                # recurse direct cause
                lst += self.query_causes(d.relation.entity2, recursion=True)
            # list of my supertypes 
            if isinstance(d.relation, Subtype) and d.relation.entity1 == entity:
                # see if my supertype has causes
                lst += self.query_causes(d.relation.entity2, recursion=False)
        return list(set(lst))

    def query_causes_sorted(self,entity):
        return sorted(
                [
                    (
                        x,  
                        self.avg( [
                            d.relation.entity2 for d in self.declarations if 
                            isinstance(d.relation, Association) and 
                            d.relation.name == 'debug_time' and
                            d.relation.entity1 == x
                        ] )
                    ) 
                    for x in self.query_causes(entity)
                ],
                key = lambda e : (e[1], e[0])
            )

    def avg(self, lst):
        return sum(lst)/len(lst)

class MyBN(BayesNet):

    def parents(self, var):
        return list(set([e[0] for fset in self.dependencies[var] for e in fset]))

    def markov_blanket(self,var):
        parents = self.parents(var)
        children = list(set([node for node in self.dependencies if var in self.parents(node)]))
        children_parents = []
        for c in children:
            children_parents += self.parents(c)
        children_parents.remove(var)
        return parents + children + children_parents



