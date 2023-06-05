"""
Affiche une chaine de caractère avec une certaine identation
"""
def afficher(s,indent=0):
	print(" "*indent+s)
	
class Programme:
	def __init__(self,listeInstructions):
		self.listeInstructions = listeInstructions
	def afficher(self,indent=0):
		afficher("<programme>",indent)
		self.listeInstructions.afficher(indent+1)
		afficher("</programme>",indent)

class ListeInstructions (list):
	def __init__(self):
		self.instructions = []
	def afficher(self,indent=0):
		afficher("<listeInstructions>",indent)
		for instruction in self:
			instruction.afficher(indent+1)
		afficher("</listeInstructions>",indent)
			
class Ecrire:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<ecrire>",indent)
		self.exp.afficher(indent+1)
		afficher("</ecrire>",indent)
		
class Operation:
	def __init__(self,op,exp1,exp2):
		self.exp1 = exp1
		self.op = op
		self.exp2 = exp2
	def afficher(self,indent=0):
		afficher("<operation>",indent)
		afficher(self.op,indent+1)
		self.exp1.afficher(indent+1)
		self.exp2.afficher(indent+1)
		afficher("</operation>",indent)
  
class Negation:
	def __init__(self,op,bool1):
		self.bool1 = bool1
		self.op = op
	def afficher(self,indent=0):
		afficher("<negation>",indent)
		afficher(self.op,indent+1)
		self.bool1.afficher(indent+1)
		afficher("</negation>",indent)

class Disjonction:
	def __init__(self,op,bool1,bool2):
		self.bool1 = bool1
		self.op = op
		self.bool2 = bool2
	def afficher(self,indent=0):
		afficher("<disjonction>",indent)
		afficher(self.op,indent+1)
		self.bool1.afficher(indent+1)
		self.bool2.afficher(indent+1)
		afficher("</disjonction>",indent)

class Conjonction:
	def __init__(self,op,bool1,bool2):
		self.bool1 = bool1
		self.op = op
		self.bool2 = bool2
	def afficher(self,indent=0):
		afficher("<conjonction>",indent)
		afficher(self.op,indent+1)
		self.bool1.afficher(indent+1)
		self.bool2.afficher(indent+1)
		afficher("</conjonction>",indent)


class Comparateur:
	def __init__(self,comparateur,somme1,somme2):
		self.somme1 = somme1
		self.comparateur = comparateur
		self.somme2 = somme2
	def afficher(self,indent=0):
		afficher("<comparateur>",indent)
		afficher(self.comparateur,indent+1)
		self.somme1.afficher(indent+1)
		self.somme2.afficher(indent+1)
		afficher("</comparateur>",indent)


class Entier:
	def __init__(self,valeur):
		self.valeur = valeur
	def afficher(self,indent=0):
		afficher("[Entier:"+str(self.valeur)+"]",indent)
  
class Booleen:
	def __init__(self, valeur):
		self.valeur = valeur
	def afficher(self, indent=0):
		if (self.valeur == True):
			afficher(f"[Booleen:vrai]", indent)
		elif (self.valeur == False):
			afficher(f"[Booleen:faux]", indent)
		else:
				afficher("[Booleen:"+str(self.valeur)+"]", indent)
     
class Identifiant:
    def __init__(self, nomDevariable):
        self.nomDevariable = nomDevariable
    def afficher(self, indent=0):
        afficher("[nomDevariable:"+str(self.nomDevariable)+"]", indent)


"""class Affectation:
    def __init__(self, identifiant, expression):
        self.identifiant = identifiant
        self.expression = expression
    def afficher(self, indent=0):
        afficher("<affectation>", indent)
        afficher(f"[Identifiant: {self.identifiant}]", indent + 1)
        self.expression.afficher(indent + 1)
        afficher("</affectation>", indent)"""