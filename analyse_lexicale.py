import sys
from sly import Lexer

class FloLexer(Lexer):
	# Noms des lexèmes (sauf les litéraux). En majuscule. Ordre non important

	tokens = {IDENTIFIANT, ENTIER, BOOLEEN, ECRIRE,
           		   INFERIEUR, INFERIEUR_OU_EGAL,
                   EGAL, PAS_EGAL,
                   SUPERIEUR, SUPERIEUR_OU_EGAL,
                   MAX, RETOURNER, TANTQUE, SI, SINON_SI,
                   SINON, ASSIGNMENT, TYPE_VARIABLE, NOM_VARIABLE, LIRE,
                   VRAI, FAUX,
                   NON, ET, OU,
                   COMPARATEUR,
                   #AFFECTATION,
                   TYPE
            }


	#Les caractères litéraux sont des caractères uniques qui sont retournés tel quel quand rencontré par l'analyse lexicale.
	#Les litéraux sont vérifiés en dernier, après toutes les autres règles définies par des expressions régulières.
	#Donc, si une règle commence par un de ces littérals (comme INFERIEUR_OU_EGAL), cette règle aura la priorité.

	literals = { '+','*','(',')',';', '-', '%', '/', '{', '}', '!', ',', '&', '='}



	# chaines contenant les caractère à ignorer. Ici espace et tabulation
	ignore = ' \t'

	# Expressions régulières correspondant au différents Lexèmes par ordre de priorité


	NON= r'non'
	OU= r'ou'
	ET= r'et'
	VRAI = r'Vrai'
	FAUX = r'Faux'
	EGAL = r'=='
	#AFFECTATION = r'='



	"""-----------------------------
	MAX = r'max'
	RETOURNER = r'retourner'
	TANTQUE = r'tantque'
	SI = r'si'
	SINON_SI = r'sinonsi'
	SINON = r'sinon'
	TYPE_VARIABLE = r'int|bool'
	NOM_VARIABLE = r'[a-zA-Z][a-zA-Z0-9_]*'
	LIRE = r'lire'
	-----------------------------"""


	@_(r'0|[1-9][0-9]*')
	def ENTIER(self, t):
		t.value = int(t.value)
		return t

# Règle pour les booléens
	@_(VRAI)
	def VRAI(self, t):
		t.value = "True"
		return t

	@_(FAUX)
	def FAUX(self, t):
		t.value = False
		return t


	@_(r'<=|>=|<|>|!=')
	def COMPARATEUR(self, t):
		return t

    	# cas général
	IDENTIFIANT = r'[a-zA-Z][a-zA-Z0-9_]*' #en général, variable ou nom de fonction
	#IDENTIFIANT = r'(entier\b|booleen\b)[a-zA-Z][a-zA-Z0-9_]*'

	# cas spéciaux:
	IDENTIFIANT['ecrire'] = ECRIRE
	IDENTIFIANT['entier'] = TYPE
	IDENTIFIANT['booleen'] = TYPE
	IDENTIFIANT['lire'] = LIRE
	IDENTIFIANT['max'] = MAX
	IDENTIFIANT['retourner'] = RETOURNER
	IDENTIFIANT['sinon_si'] = SINON_SI
	IDENTIFIANT['si'] = SI
	IDENTIFIANT['sinon'] = SINON
	IDENTIFIANT['tantque'] = TANTQUE

	#Syntaxe des commentaires à ignorer
	ignore_comment = r'\#.*'

	# Permet de conserver les numéros de ligne. Utile pour les messages d'erreurs
	@_(r'\n+')
	def ignore_newline(self, t):
		self.lineno += t.value.count('\n')

	# En cas d'erreur, indique où elle se trouve
	def error(self, t):
		print(f'Ligne{self.lineno}: caractère inattendu "{t.value[0]}"')
		self.index += 1

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("usage: python3 analyse_lexicale.py NOM_FICHIER_SOURCE.flo")
	else:
		with open(sys.argv[1],"r") as f:
			data = f.read()
			lexer = FloLexer()
			for tok in lexer.tokenize(data):
				print(tok)
