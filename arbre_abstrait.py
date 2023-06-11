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

class Lire:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<lire>",indent)
		self.exp.afficher(indent+1)
		afficher("</lire>",indent)


		
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
        




class Nom_Variable:
    def __init__(self, affectation, nom_v, valeur):
        self.nom_v = nom_v
        self.valeur = valeur
        self.affectation = affectation
    def afficher(self, indent=0):
        afficher("[nomVariable: "+str(self.nom_v)+ " " + str(self.affectation) + " " +
                 str(self.valeur) +"]", indent)       
        

"""class Declaration_Affectation:
        def __init__(self, affectation, type1, identif, expr):
                self.type1 = type1
                self.identif = identif
                self.expr = expr
                self.affectation = affectation
        def afficher(self, indent=0):
                afficher("[Declaration-Affectation: " +str(self.type1)+ " "+str(self.identif)+ " "
                         + str(self.affectation) + " " +str(self.expr) +"]", indent)"""
                         
                         
class Declaration:
	def __init__(self, identifiant, expression, type):
		self.identifiant = identifiant
		self.expression = expression
		self.type = type

	def afficher(self, indent=0):
		afficher("<declaration>", indent)
		afficher(f"[Type: {self.type}]", indent + 1)
		afficher(f"[Identifiant: {self.identifiant}]", indent + 1)
		if self.expression:
			self.expression.afficher(indent + 1)
		afficher("</declaration>", indent)


class Affectation:
    def __init__(self, identifiant, expression):
        self.identifiant = identifiant
        self.expression = expression

    def afficher(self, indent=0):
        afficher("<affectation>", indent)
        afficher(f"[Identifiant: {self.identifiant}]", indent + 1)
        self.expression.afficher(indent + 1)
        afficher("</affectation>", indent)
        

class Nom_Fonction:
	def __init__(self):
		self.exprs = []
	def afficher(self,indent=0):
		afficher("<nom_fonction>",indent)
		for expr in self.exprs:
			instruction.afficher(indent+1)
		afficher("</nom_fonction>",indent)


class Si:
	def __init__(self, expr, liste):
		self.liste = liste
		self.expr = expr
	def afficher(self,indent=0):
		afficher("<si>",indent)
		self.expr.afficher(indent+1)
		self.liste.afficher(indent+1)
		afficher("</si>",indent)


class Sinon_Si:
	def __init__(self, expr, liste):
		self.liste = liste
		self.expr = expr
	def afficher(self,indent=0):
		afficher("<sinon_si>",indent)
		self.expr.afficher(indent+1)
		self.liste.afficher(indent+1)
		afficher("</sinon_si>",indent)


class Sinon:
	def __init__(self, liste):
		self.list = []
	def afficher(self,indent=0):
		afficher("<sinon>",indent)
		for instruction in self.list:
			instruction.afficher(indent+1)
		afficher("</sinon>",indent)
		
class Instruction_Boucle:
	def __init__(self,bool1,liste):
		self.bool1 = bool1
		self.liste = liste
	def afficher(self,indent=0):
		afficher("<instruction_boucle>",indent)
		self.bool1.afficher(indent+1)
		self.liste.afficher(indent+1)
		afficher("</instruction_boucle>",indent)


class Retourner:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<retourner>",indent)
		self.exp.afficher(indent+1)
		afficher("</retourner>",indent)

class Appel_Fonction:
	def __init__(self,identif):
		self.identif = identif
	def afficher(self,indent=0):
		afficher("<appel fonction>",indent)
		self.identif.afficher(indent+1)
		afficher("</appel fonction>",indent)

class Max:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<max>",indent)
		self.exp.afficher(indent+1)
		afficher("</max>",indent)

