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
		l.append(p.instruction)
		return l

	@_('listeInstructions instruction')
	def listeInstructions(self, p):
		p.listeInstructions.append(p.instruction)
		return p.listeInstructions

	@_('ecrire')
	def instruction(self, p):
		return p[0]

	"""@_('affectation')
	def instruction(self, p):
		return p[0]"""

	@_('ECRIRE "(" expr ")" ";"')
	def ecrire(self, p):
		return arbre_abstrait.Ecrire(p.expr) #p.expr = p[2]

	@_('"-" expr "+" produit')
	def expr(self, p):
		return arbre_abstrait.Operation('-',p[3],p[1])

	@_('expr "+" produit')
	def expr(self, p):
		return arbre_abstrait.Operation('+',p[0],p[2])

	#edit
	@_('somme "+" produit')
	def somme(self, p):
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

	#3.3 Operarteurs Logiques
	@_('NON booleen')
	def booleen(self, p):
		return arbre_abstrait.Negation('non', p.booleen)

	@_('expr OU expr')
	def booleen(self, p):
		return arbre_abstrait.Disjonction(p[1], p[0], p[2])

	@_('expr ET expr')
	def booleen(self, p):
		return arbre_abstrait.Conjonction(p[1], p[0], p[2])


    #3.2 Comparateurs
	@_('expr COMPARATEUR expr',)
	def booleen(self, p):
                return arbre_abstrait.Comparateur(p[1], p[0], p[2])



    #4 Autres Instructions

	@_('declaration') #Declaration
	def instruction(self, p):
		return p[0]

	@_('TYPE IDENTIFIANT ";"')
	def declaration(self, p):
		return arbre_abstrait.Declaration(p.TYPE, p.IDENTIFIANT)

	@_('affectation') #Affectation
	def instruction(self, p):
		return p[0]

	@_('IDENTIFIANT AFFECTATION expr ";"')
	def affectation(self, p):
		return arbre_abstrait.Affectation('=', p.IDENTIFIANT, p.expr)

	@_('declaration_affectation') #Declaration_Affectation
	def instruction(self, p):
		return p[0]

	@_('TYPE IDENTIFIANT AFFECTATION expr ";"')
	def declaration_affectation(self, p):
		return arbre_abstrait.Declaration_Affectation('=', p.TYPE, p.IDENTIFIANT, p.expr)

	@_('ENTIER')
	def facteur(self, p):
		return arbre_abstrait.Entier(p.ENTIER) #p.ENTIER = p[0]

	@_('BOOLEEN')
	def facteur(self, p):
		return arbre_abstrait.Booleen(p.BOOLEEN)

	@_('VRAI')
	def booleen(self, p):
		return arbre_abstrait.Booleen(True)

	@_('FAUX')
	def booleen(self, p):
		return arbre_abstrait.Booleen(False)


	"""@_('IDENTIFIANT')
	def facteur(self, p):
		return arbre_abstrait.Identifiant(p.IDENTIFIANT)"""

	#edit
	@_('IDENTIFIANT')
	def variable(self, p):
		return arbre_abstrait.Identifiant(p.IDENTIFIANT)


	"""@_('IDENTIFIANT "=" expr ";"')
	def affectation(self, p):
		return arbre_abstrait.Affectation(p.IDENTIFIANT, p.expr)"""

	@_('produit')
	def expr(self, p):
            return p.produit

    #edit
	@_('produit')
	def somme(self, p):
		return p.produit



	@_('facteur')
	def produit(self, p):
		return p.facteur

	@_('variable')
	def facteur(self, p):
		return p.variable

	@_('"(" expr ")"')
	def facteur(self, p):
		return p[1]

	@_('booleen')
	def expr(self, p):
		return p.booleen #ou p[1]

	@_('somme')
	def booleen(self, p):
		return p.somme



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
