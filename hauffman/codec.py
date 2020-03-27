from collections import Counter

class Node():

    def __init__(self, symbol, freq, left, right):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):

        if self.left != None and self.right != None :
            return (f"{self.symbol} d'occurrence {self.freq} de fils {self.left.symbol} et {self.right.symbol}")

        if self.left == None and self.right != None :
            return (f"{self.symbol} d'occurrence {self.freq} de fils None et {self.right.symbol}")

        if self.left != None and self.right == None :
            return (f"{self.symbol} d'occurrence {self.freq} de fils {self.left.symbol} et None")

        if self.left == None and self.right == None :
            return (f"{self.symbol} d'occurrence {self.freq} de fils None et None")

class TreeBuilder() :



    def __init__(self,text):
        self.text = text





    def tree(self):
        text = self.text
        D = Counter(text)
        Nb, Letter = [], []
        Nb.sort()
        for a,b in sorted(D.items(), key=lambda x: x[1]):  #On a maintenant Letter et Nb les deux listes ordonnées par occurence croissante contenant les différentes lettres du texte, et leur occurences
            Letter.append(a)
            Nb.append(b)
        n = len(Letter)

        # print(Nb)
        # print(Letter)

        nodes=[0 for k in range(n)] #On crée une liste nodes des noeuds que l'on traitera pour construire l'arbre

        for i in range(n) :
            nodes[i] = Node(Letter[i],Nb[i],None,None)  #on crée les feuilles de base

        # for i in nodes :
        #     print(i)


        while len(nodes) >= 2 :  # On va créer les nouveaux noeuds et les classer par occurence croissante dans la liste nodes
            a, b = nodes[0], nodes[1]
            newNode = Node(a.symbol + b.symbol, a.freq + b.freq, a, b)
            del nodes[0]
            del nodes[0]

            nodes.insert(0, newNode)
            c=1

            while c < len(nodes)  and nodes[c].freq <= newNode.freq : #On insère le nouveau noeud de manière ordonnée dans la liste nodes
                nodes[c],nodes[c-1] = nodes[c-1],nodes[c]
                c+=1




            c=0


            for i in nodes :
                print(i)

        return nodes[0]








class Codec():

    def __init__(self,tree):
        self.tree = tree


    def codage(self,text):
        tree = self.tree
        A= Counter(tree.symbol)
        Letters = []
        code = {}
        for i in A.keys():
            Letters.append(i)
        for let in Letters :
            node = tree
            chemin = ''

            while len(node.symbol) > 1:

                a = node.left
                b = node.right
                if let in a.symbol:
                    node = a
                    chemin = chemin + '0'
                else :
                    node = b
                    chemin = chemin + '1'
            code[let] = (chemin)

        return (code)


    def encode(self, text):
        code = self.codage(text)
        rep = ''
        for i in text:
            rep = rep + code.get(i)
        return rep

    def decode(self, encoded):
        res = ''
        tree = self.tree
        node = tree

        for i in encoded :
            if i == '0':
                node = node.left
            else :
                node = node.right
            if len(node.symbol) == 1 :
                res = res + node.symbol
                node = tree

        return res





#
# test = TreeBuilder('a dead dad ceded a bad babe a beaded abaca bed')
# tree = test.tree()
# cod = Codec(tree)
# # print(cod)
# print(cod.encode('a dead dad ceded a bad babe a beaded abaca bed'))
# print(cod.decode(cod.encode('a dead dad ceded a bad babe a beaded abaca bed')))
















