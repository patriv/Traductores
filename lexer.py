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

#Ignora cualquier tipo de espacio
#Tabulador y espacio uno o mas veces
t_ignore = ' \s+'
t_TkNum = '\d+'

#Ignoramos los comentarios
#t_ignore_comments = r'%{'  REVISAR

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
t_TkValorAscii = r'\#' #???
t_TkConcatenacion = r'::'
t_TkRotacion = r'\$'
t_TkTrasposicion = r'\?' #??

#Definimos literales numericos
def TkNum (t):
	r'\d+'
	lexer_tokenList.append(t.lexer)
	print ('hola',lexer_tokenList.append(t.lexer))


#Cuenta numero de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 #COntamos el numero de columna

#Creamos una lista de nuestros tokens
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



'''

def build_lexer(code):
    lexer = lex.lex()
    lexer.input(code)

    for tok in lexer_tokenList:
        print tok

'''
if __name__ == '__main__':
	pass
	
#	t_newline(t)