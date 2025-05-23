import sys
from sly import Parser
from analyse_lexicale import FloLexer
import arbre_abstrait

class FloParser(Parser):    
	# On récupère la liste des lexèmes de l'analyse lexicale
	tokens = FloLexer.tokens

	# Règles gramaticales et actions associées
	@_('listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p[0])

	@_('instruction')
	def listeInstructions(self, p):
		l = arbre_abstrait.ListeInstructions()
		l.instructions.append(p[0])
		return l
					
	@_('instruction listeInstructions')
	def listeInstructions(self, p):
		p[1].instructions.append(p[0])
		return p[1]
		
	@_('ecrire')
	def instruction(self, p):
		return p[0]

	@_('affectation')
	def instruction(self, p):
		return p[0]
			
	@_('ECRIRE "(" expr ")" ";"')
	def ecrire(self, p):
		return arbre_abstrait.Ecrire(p.expr) #p.expr = p[2]
	
	@_('"-" expr "+" produit')
	def expr(self, p):
		return arbre_abstrait.Operation('-',p[3],p[1])
	
	@_('expr "+" produit')
	def expr(self, p):
		return arbre_abstrait.Operation('+',p[0],p[2])

	@_('expr "-" produit')
	def expr(self, p):
                return arbre_abstrait.Operation('-',p[0],p[2])

	@_('produit "*" facteur')
	def produit(self, p):
            return arbre_abstrait.Operation('*', p[0], p[2])

	@_('produit "/" facteur')
	def produit(self, p):
            return arbre_abstrait.Operation('/', p[0], p[2])

	@_('produit "%" facteur')
	def produit(self, p):
            return arbre_abstrait.Operation('%', p[0], p[2])

	@_('"-" expr')
	def produit(self, p):
            return arbre_abstrait.Operation('*', arbre_abstrait.Entier(-1), p[1])
	             



	@_('ENTIER')
	def facteur(self, p):
		return arbre_abstrait.Entier(p.ENTIER) #p.ENTIER = p[0]

	"""@_('BOOLEEN')
	def facteur(self, p):
		return arbre_abstrait.Booleen(p.BOOLEEN)"""
	@_('VRAI')
	def facteur(self, p):
		return arbre_abstrait.Booleen(True)

	@_('FAUX')
	def facteur(self, p):
		return arbre_abstrait.Booleen(False)


	@_('IDENTIFIANT')
	def facteur(self, p):
		return arbre_abstrait.Identifiant(p.IDENTIFIANT)

	@_('IDENTIFIANT "=" expr ";"')
	def affectation(self, p):
		return arbre_abstrait.Affectation(p.IDENTIFIANT, p.expr)

	@_('produit')
	def expr(self, p):
            return p.produit

	@_('facteur')
	def produit(self, p):
            return p.facteur

	@_('"(" expr ")"')
	def facteur(self, p):
		return p[1]
		


	"""@_('lire()')
	def facteur(self, p):
		return arbre_abstrait.Entier(p.lire())"""

	"""@_('nomFonction')
	def facteur(self, p):
		return arbre_abstrait.Entier(p.nomFonction)	"""

if __name__ == '__main__':
	lexer = FloLexer()
	parser = FloParser()
	if len(sys.argv) < 2:
		print("usage: python3 analyse_syntaxique.py NOM_FICHIER_SOURCE.flo")
	else:
		with open(sys.argv[1],"r") as f:
			data = f.read()
			try:
			    arbre = parser.parse(lexer.tokenize(data))
			    arbre.afficher()
			except EOFError:
			    exit()
