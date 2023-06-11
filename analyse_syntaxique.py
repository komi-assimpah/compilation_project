import sys
from sly import Parser
from analyse_lexicale import FloLexer
import arbre_abstrait

class FloParser(Parser):
	# On récupère la liste des lexèmes de l'analyse lexicale
	tokens = FloLexer.tokens

	# Règles gramaticales et actions associées

	@_('prog')
	def statement(self, p):
		return p.prog

	@_('listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p.listeInstructions)

	@_('listeFonctions')
	def prog(self, p):
		return arbre_abstrait.Programme(p.listeFonctions)

	@_('listeFonctions listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p.listeFonctions, p.listeInstructions)

	@_('fonction_declaration_without_parm')
	def listeFonctions(self, p):
		l = arbre_abstrait.ListeFonctions()
		l.append(p.fonction_declaration_without_parm)
		return l

	@_('fonction_declaration')
	def listeFonctions(self, p):
		l = arbre_abstrait.ListeFonctions()
		l.append(p.fonction_declaration)
		return l

	@_('listeFonctions fonction_declaration')
	def listeFonctions(self, p):
		p.listeFonctions.append(p.fonction_declaration)
		return p.listeFonctions

	@_('listeFonctions fonction_declaration_without_parm')
	def listeFonctions(self, p):
		p.listeFonctions.append(p.fonction_declaration_without_parm)
		return p.listeFonctions

	@_('listeInstructions instruction')
	def listeInstructions(self, p):
		p.listeInstructions.append(p.instruction)
		return p.listeInstructions

	@_('instruction')
	def listeInstructions(self, p):
		l = arbre_abstrait.ListeInstructions()
		l.append(p.instruction)
		return l

	#reviens
	@_('ecrire', 'boucle', 'appel_fonction_instr', 'appel_fonction_instr_without_parm')
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

	#edit
	@_('somme "+" produit')
	def somme(self, p):
		return arbre_abstrait.Operation('+',p[0],p[2])

	@_('expr "-" produit')
	def expr(self, p):
                return arbre_abstrait.Operation('-',p[0],p[2])
            
    #edit
	@_('somme "-" produit') #duplicate
	def somme(self, p):
		return arbre_abstrait.Operation('-',p[0],p[2])

	@_('produit "*" facteur')
	def produit(self, p):
            return arbre_abstrait.Operation('*', p[0], p[2])


                
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

	@_('VRAI')
	def booleen(self, p):
		return arbre_abstrait.Booleen(True)

	@_('FAUX')
	def booleen(self, p):
		return arbre_abstrait.Booleen(False)

	@_("expr")
	def arg_list(self, p):
		return [p.expr]

	@_("arg_list ',' expr")
	def arg_list(self, p):
		p.arg_list.append(p.expr)
		return p.arg_list


	

	@_('produit')
	def expr(self, p):
            return p.produit





	@_('facteur')
	def produit(self, p):
		return p.facteur



	@_('"(" expr ")"')
	def expr(self, p):
		return p.expr #ou p[1]

	#2.3 Autres Factuers
	


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

    #edit
	@_('produit')
	def somme(self, p):
                return p.produit
        



        

                


    #3.2 Comparateurs
	@_('expr COMPARATEUR expr',)
	def booleen(self, p):
                return arbre_abstrait.Comparateur(p[1], p[0], p[2])

	@_('somme EGAL somme')
	def booleen(self, p):
				return arbre_abstrait.Comparateur('==', p[0], p[2])
            
	#3.3 Operateurs Logiques
	@_('NON booleen')
	def booleen(self, p):
		return arbre_abstrait.Negation('non', p.booleen)

	@_('expr OU expr')
	def booleen(self, p):
		return arbre_abstrait.Disjonction(p[1], p[0], p[2])

	@_('expr ET expr')
	def booleen(self, p):
		return arbre_abstrait.Conjonction(p[1], p[0], p[2])


    
    #4 Autres Instructions

	@_('declaration') #Declaration
	def instruction(self, p):
		return p[0]
			
	@_('affectation') #Affectation
	def instruction(self, p):
		return p[0]
			
	@_('TYPE IDENTIFIANT "=" expr ";"')
	def declaration(self, p):
		return arbre_abstrait.Declaration(p.IDENTIFIANT, p.expr, p.TYPE)

	@_('TYPE IDENTIFIANT ";"')
	def declaration(self, p):
		return arbre_abstrait.Declaration(p.IDENTIFIANT, None, p.TYPE)

	@_('IDENTIFIANT "=" expr ";"')
	def affectation(self, p):
		return arbre_abstrait.Affectation(p.IDENTIFIANT, p.expr)












	@_('condition') #SI
	def instruction(self, p):
		return p[0]

	@_('SI "(" expr ")" "{" listeInstructions "}" suite_sinonsi')
	def condition(self, p):
		return arbre_abstrait.Condition(p.expr, p.listeInstructions, p.suite_sinonsi)

	@_('SINON "{" listeInstructions "}"')
	def suite_sinonsi(self, p):
		return p.listeInstructions

	@_('SINON SI "(" expr ")" "{" listeInstructions "}" suite_sinonsi')
	def suite_sinonsi(self, p):
		return arbre_abstrait.Condition(p.expr, p.listeInstructions, p.suite_sinonsi)

	@_('')
	def suite_sinonsi(self, p):
		return None

	@_('TANTQUE "(" expr ")" "{" listeInstructions "}"')
	def boucle(self, p):
		return arbre_abstrait.TantQue(p.expr, p.listeInstructions)
    
    






	@_('retourner') #Instruction retourner expression
	def instruction(self, p):
                return p[0]
        
	@_('retourner')
	def retourner(self, p):
		return p.retourner

	@_('RETOURNER expr ";"')
	def retourner(self, p):
		return arbre_abstrait.Retourner(p.expr)

	@_('IDENTIFIANT "(" arg_list ")" ";" ')
	def appel_fonction_instr(self, p):
		return arbre_abstrait.Appel_Fonction(p.IDENTIFIANT, p.arg_list)

	@_("IDENTIFIANT '(' arg_list ')'")
	def appel_fonction_expr(self, p):
		return arbre_abstrait.Appel_Fonction(p.IDENTIFIANT, p.arg_list)

	@_('IDENTIFIANT "(" ")" ";"')
	def appel_fonction_instr_without_parm(self, p):
		return arbre_abstrait.Appel_Fonction(p.IDENTIFIANT, [])

	@_('IDENTIFIANT "(" ")" ')
	def appel_fonction_expr_without_parm(self, p):
		return arbre_abstrait.Appel_Fonction(p.IDENTIFIANT, [])

	@_('TYPE IDENTIFIANT "(" param_list ")" "{" listeInstructions "}"')
	def fonction_declaration(self, p):
		return arbre_abstrait.Fonction(p.IDENTIFIANT, p.TYPE, p.param_list, p.listeInstructions)

	@_("TYPE IDENTIFIANT '(' ')' '{' listeInstructions '}'")
	def fonction_declaration_without_parm(self, p):
		return arbre_abstrait.Fonction(p.IDENTIFIANT, p.TYPE, [], p.listeInstructions)

	@_("param")
	def param_list(self, p):
		return [p.param]

	@_("param_list ',' param")
	def param_list(self, p):
		p.param_list.append(p.param)
		return p.param_list

	@_("TYPE IDENTIFIANT")
	def param(self, p):
		return arbre_abstrait.Parametre(p.TYPE, p.IDENTIFIANT)


	@_('variable')
	def facteur(self, p):
                return p.variable

	#edit
	@_('IDENTIFIANT')
	def variable(self, p):
                return arbre_abstrait.Identifiant(p.IDENTIFIANT)


        

            
	@_('appel_fonction_expr')
	def facteur(self, p):
		return p.appel_fonction_expr

	@_('appel_fonction_expr_without_parm')
	def facteur(self, p):
		return p.appel_fonction_expr_without_parm







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
