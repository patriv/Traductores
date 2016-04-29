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
	 #Es reservada, no?

	#Tipos 
	'char'  : 'TkChar',
	'bool'  : 'TkBool', #es bool??
	'int'   : 'TkInt',
	'matrix': 'TkMatrix',

	'of'    : 'TkOf'

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
	'TkMayoIgual',
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
t_TkNum = '\d+'

#Ignoramos comentarios simples
t_ignore_commentSimple = r'\%\%(.)*'

#Ignoramos los comentarios de secciones completas
t_ignore_comment = r'\%{([^-]|([-]+[^\$]))*}%'
    

#Definimos las expresiones para los separadores
t_TkComa = r','  #PREGUNTAR
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
t_TkConjuncion = r'/\\' #no se
t_TkDisyuncion = r'\\/' #no se
t_TkNegacion = r'not'
t_TkMenor = r'<'
t_TkMenorIgual = r'<='
t_TkMayor = r'>'
t_TkMayoIgual = r'>='
t_TkIgual = r'='
t_TkSiguienteCar = r'\+\+'
t_TkAnteriorCar = r'\-\-'  #no se!!
t_TkValorAscii = r'[#]' #???
t_TkConcatenacion = r'::'
t_TkRotacion = r'\$'
t_TkTrasposicion = r'\?' #??

'''
#Definimos literales numericos
def TkNum (t):
	r'\d+'
	lexer_tokenList.append(t.lexer)
	'''

#Expresion regular para TkId
def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'TkId')    # Check for reserved words
    return t


#Expresion regular para un caracter




#Cuenta numero de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Cuenta numero de columna 
def findColumn (t):
	last_cr = lexer.lexdata.rfind('\n',0,t.lexpos)
	if last_cr < 0:
		last_cr = 0
	column = t.lexpos - last_cr
	return column

#Errores de caracteres no esperados
def t_error (t):
	errorCaracter = 'ERROR: Caracter inesperado "{0}" en la fila {1}, columna {2}' .format(t.value[0], t.lineno, findColumn(t))
	lexer_error.append(errorCaracter)
	t.lexer.skip(1)

def print_error():
    print('\n'.join(lexer_error))



#Creamos Lista de errores
lexer_error = []

#Creamos una lista de nuestros tokens
lexer_tokenList = []

#Construccion del lexer
lexer = lex.lex()

# Test it out
data = '''

%{ hol }%}%
}%
with
	var contador: int
3 + 4 * 10
  + -20 *2 
 end
'''
z = lexer.input(data)


while True:
    tok = lexer.token()
    if not tok: 
        break  
    lexer_tokenList.append(tok)    
    
   
if len(lexer_error) != 0:
    print_error()
else: 
	for t in lexer_tokenList:
    
        	print t

lex.lex()
'''
#Construimos el lexer
def build_lexer(code):
    lexer = lex.lex()
    lexer.input(code)

    while True:
    	tok = lexer.token()
    	if not tok: 
       		break 
    	lexer_tokenList.append(tok)    

    if lexer_error != []:
    	print_error()
    else:
    	for t in lexer_tokenList:
    
        	print t
    print("no sirve")
'''
if __name__ == '__main__':
	pass
	
#	t_newline(t)