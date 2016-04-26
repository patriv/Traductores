import lexer
import sys

if __name__ == '__main__':
    
    #Comprobacion de los parametros de entrada. 
    if len(sys.argv) < 2:
        print "Error: Parametros de entrada incorrectos."
        exit()
    

    #Abrimos el archivo del codigo setlan
    codeFile = open(sys.argv[1], 'r')
    code = codeFile.read()

    #Ejecutamos el lexer
    lexer.build_lexer(code)


 