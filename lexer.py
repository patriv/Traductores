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
t_ignore = ' \t'

#Ignoramos los comentarios
t_ignore_comments = r'%{.*}%'

# Reglas de expresiones regulares para tokens simples
t_TkComa = r'\,'
t_TkPunto = r'\.'
t_TkDosPuntos = r'\:'
t_TkParAbre = r'\('
t_TkParCierra = r'\)'
t_TkCorcheteAbre = r'\['
t_TkCorcheteCierra = r'\]'
t_TkLlaveAbre = r'\{'
t_TkLlaveCierra = r'\}'
t_TkHacer = r'\->'
t_TkAsignacion = r'\<-'
t_TkSuma = r'\+'
t_TkResta = r'\-'
t_TkMult = r'\*'
t_TkDiv = r'\/'
t_TkMod = r'\%'
t_TkConjuncion = r'\/\\' #REVISAR
t_TkDisyuncion = r'\\\/' #REVISAR
t_TkNegacion = r'\not'
t_TkMenor = r'\<'
t_TkMenorIgual = r'<='
t_TkMayor = r'\>'
t_TkMayorIgual = r'>='
t_TkIgual = r'\='
t_TkSiguienteCar = r'\++'
t_TkAnteriorCar = r'\-' #ES IGUAL A LA RESTA?
t_TkValorAscii = r'\#'
t_TkConcatenacion = r'\::'
t_TkRotacion = r'\$'
t_TkTrasposicion = r'\?'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# #Retorna un string conteniendo la linea y la columna
# def getLineAndColumn(code,t):
#     return '(Línea {0}, Columna {1})' .format(t.lexer.lineno, find_column(code,t))

#Manejo de errores  

def t_error(t):
    errorString  = 'Error: se encontro un caracter inesperado "{0}"' .format(t.value[0])
    errorString +=  getLineAndColumn(t.lexer.lexdata,t)
    lexer_errorList.append(errorString)
    t.lexer.skip(1)


#Lista de errores del Lexer
lexer_errorList = []

#Lista de tokens del Lexer
lexer_tokenList = []

#Construccion del lexer
lexer = lex.lex()

def build_lexer(code):
    lexer = lex.lex()
    lexer.input(code)

    # Analiza los tokens
    while True:
       	tok = lexer.token()

        if not tok:
            break

        lexer_tokenList.append(tok)

    # Imprime resultados del analisis realizado
        if len(self._errorlist) != 0:
        	for er in lexer_errorList:
        		print er
        else:
            for tok in lexer_tokenList:
        		print tok

if __name__ == '__main__':
	pass
