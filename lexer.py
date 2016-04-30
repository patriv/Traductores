#!/usr/bin/env python
# -*- coding: utf-8 *-* 

'''
Creado 26/04/2016

@author: Cinthya Ramos. 09-11237
@author: Patricia Valencia. 10-10916

'''

import ply.lex as lex

#Palabras Claves de NEO

reserved = {

	#Correspondientes al programa

	'begin' : 'TkBegin',
	'end'   : 'TkEnd',
	'with' : 'TkWith',
	'var'   : 'TkVar',

	#Condicional

	'if'        : 'TkIf',
	'otherwise' : 'TkOtherwise',

	#Ciclos

	'for'   : 'TkFor',
	'from'  : 'TkFrom',
	'to'    : 'TkTo',
	'step'  : 'TkStep',
	'while' : 'TkWhile',

	#Entrada y salida
	'read'  : 'TkRead',
	'print' : 'TkPrint',

	#Boolenos
	'true'  : 'TkTrue',
	'false' : 'TkFalse',

	#Tipos 
	'char'  : 'TkChar',
	'bool'  : 'TkBool', 
	'int'   : 'TkInt',
	'matrix': 'TkMatrix',

	'of'    : 'TkOf',

	#operador
	'not'  : 'TkNot'
}

# Tokens relevantes
tokens = [
	#Identificador de variable
	'TkId',

	#Literales numericos
	'TkNum',

	#Literales Caracter
	'TkCaracter',

	#Separadores
	'TkComa',
	'TkPunto',
	'TkDosPuntos',
	'TkParAbre',
	'TkParCierra',
	'TkCorcheteAbre',
	'TkCorcheteCierra',
	'TkLlaveAbre',
	'TkLlaveCierra',
	'TkHacer',
	'TkAsignacion',

	#Operadores
	'TkSuma',
	'TkResta',
	'TkMult',
	'TkDiv',
	'TkMod',
	'TkConjuncion',
	'TkDisyuncion',
	'TkNegacion',
	'TkMenor',
	'TkMenorIgual',
	'TkMayor',
	'TkMayorIgual',
	'TkIgual',
	'TkSiguienteCar',
	'TkAnteriorCar',
	'TkValorAscii',
	'TkConcatenacion',
	'TkRotacion',
	'TkTrasposicion'

] + list(reserved.values())


#Ignora Tabulador y espacio uno o mas veces
t_ignore = ' \t'

#Ignoramos comentarios simples
t_ignore_commentSimple = r'\%\%(.)*'

#Ignoramos los comentarios de secciones completas
def t_ignore_comment(t):
	r'\%{([^-]|([-]+[^\$]))*\}%'
	t.lexer.lineno += t.value.count('\n') 

#Definimos la expresion para los digitos decimales
t_TkNum = '\d+'
    
#Definimos las expresiones para los separadores
t_TkComa = r','
t_TkPunto = r'\.'
t_TkDosPuntos = r':'
t_TkParAbre = r'\('
t_TkParCierra = r'\)'
t_TkCorcheteAbre = r'\['
t_TkCorcheteCierra = r'\]'
t_TkLlaveAbre = r'{'
t_TkLlaveCierra = r'}'
t_TkHacer = r'\->' #no se   
t_TkAsignacion = r'\<-' #no se

#Definimos las expresiones para operadores
t_TkSuma = r'\+'
t_TkResta = r'-'
t_TkMult = r'\*'
t_TkDiv = r'/'
t_TkMod = r'%'
t_TkConjuncion = r'\/\\'
t_TkDisyuncion = r'\\/'
t_TkNegacion = r'\not'
t_TkMenor = r'<'
t_TkMenorIgual = r'<='
t_TkMayor = r'>'
t_TkMayorIgual = r'>='
t_TkIgual = r'='
t_TkSiguienteCar = r'\+\+'
t_TkAnteriorCar = r'\-\-' 
t_TkValorAscii = r'[#]' 
t_TkConcatenacion = r'::'
t_TkRotacion = r'\$'
t_TkTrasposicion = r'\?'


#Expresion regular para TkId
def t_TkId(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'TkId')    # Check for reserved words
    return t


#Expresion regular para un caracter

def t_TkCaracter(t):
	r'\'((\\t)|(\\n)|([^\']))\''
	t.value = str(t.value)
	return t

#Cuenta numero de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Cuenta numero de columna 
def find_column(t):
	last_cr = lexer.lexdata.rfind('\n', 0, t.lexpos)
	if last_cr < 0:
		column = t.lexpos + 1
	else:
		column = t.lexpos - last_cr
	return column

#Errores de caracteres no esperados
def t_error (t):
	errorCaracter = 'ERROR: Caracter inesperado "{0}" en la fila {1}, columna {2}' .format(t.value[0], t.lineno, find_column(t))
	lexer_error.append(errorCaracter)
	t.lexer.skip(1)

def print_error():
    print('\n'.join(lexer_error))



#Creamos Lista de errores
lexer_error = []

#Creamos una lista de nuestros tokens
lexer_tokenList = []

# #Construccion del lexer
lexer = lex.lex()


def analyzeNeo (code) :

	lexer.input(code)


	while True:
	    tok = lexer.token()
	    if not tok: 
	        break  
	    lexer_tokenList.append(tok)    
	    
	   
	if len(lexer_error) != 0:
	    print_error()
	else: 
		print('\n'+"----------------------------BIENVENIDO----------------------------"+'\n')
		print('\n'+"Los tokens reconocidos en el archivo son: "+'\n')
		nlinea = -1
		tok = []
		for t in lexer_tokenList:
			if (not(t.lineno == nlinea)) and not(t==lexer_tokenList[0]):
				tok.append('\n')

			nlinea = t.lineno
			if t.type == 'TkId':
				tok.append("{0}(\"{1}\") {2} {3}".format(t.type,t.value,t.lineno,find_column(t)))
			elif (t.type == 'TkNum') or (t.type == 'TkCaracter'):
				tok.append("{0}({1}) {2} {3}".format(t.type,t.value,t.lineno,find_column(t)))
			else:
				tok.append("{0} {1} {2}".format(t.type,t.lineno,find_column(t)))
			tok.append(', ')

		toke= "".join(tok)

		print toke[:(len(toke)-2)]+'\n'
		

lex.lex()


if __name__ == '__main__':
	pass
