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
			
	@_('ECRIRE "(" expr ")" ";"')
	def ecrire(self, p):
		return arbre_abstrait.Ecrire(p.expr) #p.expr = p[2]

                
	@_('produit "/" facteur')
	def produit(self, p):
                return arbre_abstrait.Operation('/',p[0],p[2])
                
	@_('produit "%" facteur')
	def produit(self, p):
                return arbre_abstrait.Operation('%',p[0],p[2])

	@_('"-" facteur')
	def produit(self, p):
            return arbre_abstrait.Operation('*', arbre_abstrait.Entier(-1), p[1])

	@_('ENTIER')
	def facteur(self, p):
		return arbre_abstrait.Entier(p.ENTIER)

	@_('BOOLEEN')
	def facteur(self, p):
		return arbre_abstrait.Booleen(p.BOOLEEN)

	@_('"(" expr ")"')
	def expr(self, p):
		return p.expr #ou p[1]

	#2.3 Autres Factuers
	
	@_('IDENTIFIANT AFFECTATION ENTIER') #facteur nomVariable
	def facteur(self, p):
		return arbre_abstrait.Nom_Variable('=', p.IDENTIFIANT, p.ENTIER)
	
	@_('nomFonction') #facteur nomFonction
	def facteur(self, p):
                return p[0]

	@_('IDENTIFIANT "(" facteur ")"')
	def nomFonction(self, p):
                return arbre_abstrait.Nom_Fonction(p.factuer)

	@_('lire') #facteur lire()
	def facteur(self, p):
		return p[0]
	
	@_('LIRE "(" expr ")"')
	def lire(self, p):
		return arbre_abstrait.Lire(p.expr)

			
	#3. Expressions Booléennes

	#3.1 Problème de Type

	@_('booleen')
	def expr(self, p):
		return p.booleen #ou p[1]

	@_('somme')
	def booleen(self, p):
                return p.somme

	@_('VRAI')
	def booleen(self, p):
                return arbre_abstrait.Vrai(p.VRAI)

	@_('FAUX')
	def booleen(self, p):
                return arbre_abstrait.Faux(p.FAUX)
        
	@_('produit')
	def somme(self, p):
                return p.produit
        
	@_('somme "+" produit')
	def somme(self, p):
                return arbre_abstrait.Operation('+',p[0],p[2])

	@_('somme "-" produit') #duplicate
	def somme(self, p):
                return arbre_abstrait.Operation('-',p[0],p[2])

	@_('facteur') #duplicate
	def produit(self, p):
                return p.facteur	        

	@_('produit "*" facteur') #duplicate
	def produit(self, p):
                return arbre_abstrait.Operation('*',p[0],p[2])
                
	@_('variable')
	def facteur(self, p):
                return p.variable

	@_('IDENTIFIANT')
	def variable(self, p):
                return arbre_abstrait.Identifiant(p.IDENTIFIANT)


        #3.2 Comparateurs

	@_('somme EGAL somme')
	def booleen(self, p):
                return arbre_abstrait.Comparateur('==', p[0], p[2])

	@_('somme PAS_EGAL somme')
	def booleen(self, p):
                return arbre_abstrait.Comparateur('!=', p[0], p[2])

	@_('somme INFERIEUR somme')
	def booleen(self, p):
                return arbre_abstrait.Comparateur('<', p[0], p[2])

	@_('somme INFERIEUR_OU_EGAL somme')
	def booleen(self, p):
                return arbre_abstrait.Comparateur('<=', p[0], p[2])

	@_('somme SUPERIEUR somme')
	def booleen(self, p):
                return arbre_abstrait.Comparateur('>', p[0], p[2])

	@_('somme SUPERIEUR_OU_EGAL somme')
	def booleen(self, p):
                return arbre_abstrait.Comparateur('>=', p[0], p[2])

	
	#3.3 Operarteurs Logiques

	@_('NON booleen')
	def booleen(self, p):
                return arbre_abstrait.Negation('non', p.booleen)

	@_('somme OU produit')
	def booleen(self, p):
                return arbre_abstrait.Conjonction('ou', p.somme, p.produit)

	@_('somme ET produit')
	def booleen(self, p):
                return arbre_abstrait.Conjonction('et', p.somme, p.produit)


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

	@_('si') #SI
	def instruction(self, p):
		return p[0]
			
	@_('SI "(" expr ")" "{" listeInstructions "}"')
	def si(self, p):
		return arbre_abstrait.Si(p.expr, p.listeInstructions) 

	@_('sinon_si') #SINON_SI
	def instruction(self, p):
		return p[0]
			
	@_('SINON_SI "(" expr ")" "{" listeInstructions "}"')
	def sinon_si(self, p):
		return arbre_abstrait.Sinon_Si(p.expr, p.listeInstructions) 

	@_('sinon') #SINON 
	def instruction(self, p):
		return p[0]
			
	@_('SINON "{" listeInstructions "}"')
	def sinon(self, p):
		return arbre_abstrait.Sinon(p.listeInstructions)

	@_('tantque') #TANTEQUE 
	def instruction(self, p):
		return p[0]
			
	@_('TANTQUE "(" expr ")" "{" listeInstructions "}"')
	def tantque(self, p):
		return arbre_abstrait.Instruction_Boucle(p.expr, p.listeInstructions) 


	@_('retourner') #Instruction retourner expression
	def instruction(self, p):
                return p[0]
        
	@_('RETOURNER expr ";"') #Instruction retourner expression
	def retourner(self, p):
                return arbre_abstrait.Retourner(p.expr)
        

	@_('appel_fonction') #Appel de fonction
	def instruction(self, p):
                return p[0]

	@_('IDENTIFIANT "(" facteur ")" ";"') #Appel de fonction
	def appel_fonction(self, p):
                return arbre_abstrait.Appel_Fonction(p.IDENTIFIANT)

	@_('max') #Max
	def instruction(self, p):
                return p[0]
        
	@_('MAX "(" expr ")" ";"') #Max
	def max(self, p):
                return arbre_abstrait.Max(p.expr)
        



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
