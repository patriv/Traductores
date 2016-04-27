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
	'whith' : 'TkWith',
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

}

# Tokens relevantes
tokens = [
	#Identificador de variable
	'TkId',

	#Literales numericos
	'TkNum'

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

#Ignora cualquier tipo de espacio
#Tabulador y espacio uno o mas veces
t_ignore = ' \s+'

#Ignoramos los comentarios
#t_ignore_comments = r'%{'  REVISAR

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_TkSuma(t):
	r'\+'
	


'''
#Retorna un string conteniendo la linea y la columna
def getLineAndColumn(code,t):
    return '(Línea {0}, Columna {1})' .format(t.lexer.lineno, find_column(code,t))



#Manejo de errores  

def t_error(t):
    errorString  = 'Error: se encontro un caracter inesperado "{0}"' .format(t.value[0])
    errorString +=  getLineAndColumn(t.lexer.lexdata,t)
    lexer_errorList.append(errorString)
    t.lexer.skip(1)

#Lista de errores del Lexer
lexer_errorList = []
'''
lexer_tokenList = []

#Construccion del lexer
lexer = lex.lex()



# Test it out
data = '''
3 + 4 * 10
  + -20 *2
'''
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)





def build_lexer(code):
    lexer = lex.lex()
    lexer.input(code)

    for tok in lexer_tokenList:
        print tok


if __name__ == '__main__':
	pass
	
#	t_newline(t)