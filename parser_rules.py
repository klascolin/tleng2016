from lexer_rules import tokens

# Para el arbol sintactico
class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf

# Simbolo inicial
start = 'g'

# ---------------------------------------------------------------------------------------
#Sentencias:

#Generalizo la gramatica con linea, puede ser una sentencia o un comentario
def p_g1(subexpressions):
  'g : linea g  '
  subexpressions[0] = str(subexpressions[1]) + "\n" + str(subexpressions[2]) 

def p_g3(subexpressions):
  '''g : empty'''
  subexpressions[0] = "\n"

def p_linea(subexpressions):
  '''linea : lAbierta'''
  subexpressions[0] = "L abierta"

def p_linea1(subexpressions):
  '''linea : lCerrada'''
  subexpressions[0] = subexpressions[1]


def p_lAbierta(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' linea
  | IF '(' cosaBooleana ')' bloqueCerrado ELSE lAbierta 
  | loop  lAbierta '''
  subexpressions[0] = toString(subexpressions)

def p_bloqueCerrado(subexpressions):
  '''bloqueCerrado : lCerrada
  | '{' g '}' '''
  subexpressions[0] = toString(subexpressions)

def p_lCerrada1(subexpressions):
  '''lCerrada : sentencia'''
  subexpressions[0] = toString(subexpressions)

def p_lCerrada2(subexpressions):
  '''lCerrada : COMMENT'''
  subexpressions[0] = toString(subexpressions)

def p_lCerrada3(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' bloqueCerrado ELSE bloqueCerrado'''
  subexpressions[0] = toString(subexpressions)

def p_lCerrada4(subexpressions):
  '''lCerrada : loop bloqueCerrado '''
  subexpressions[0] = toString(subexpressions)

def p_lCerrada5(subexpressions):
  '''lCerrada : DO bloqueCerrado WHILE '(' cosaBooleana ')' ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia1(subexpressions):
  '''sentencia : varsOps  ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia2(subexpressions):
  '''sentencia : func ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia3(subexpressions):
  '''sentencia : varAsig ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia4(subexpressions):
  '''sentencia : RETURN ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia5(subexpressions):
  '''sentencia : ';' '''
  subexpressions[0] = toString(subexpressions)


def p_loop1(subexpressions):
  '''loop : WHILE '(' cosaBooleana ')' '''
  subexpressions[0] = toString(subexpressions)
#def p_loop2(subexpressions):
 # '''loop : DO lCerrada WHILE '(' expBool ')' ';' '''

def p_loop3(subexpressions):
  '''loop : FOR '(' primParam ';' cosaBooleana ';' tercerParam ')' '''
  subexpressions[0] = toString(subexpressions)

#en el tercer parametro del for pongo varOps, pero en realidad puede ser mas general(!), es lo que discutimos en clase.

#Este puede ser util para otras cosas de mas abajo. Ver como reemplazar !

def p_cosaBooleana(subexpressions):
  '''cosaBooleana : expBool
  | valoresBool'''
  subexpressions[0] = toString(subexpressions)

def p_primParam(subexpressions):
  '''primParam : varAsig
  | empty'''
  subexpressions[0] = toString(subexpressions)

def p_tercerParam(subexpressions):
  '''tercerParam : varsOps
  | varAsig
  | func
  | empty'''
  subexpressions[0] = toString(subexpressions)

# ---------------------------------------------------------------------------------------
#Control:

#-----------------------------------------------------------------------------
#Funciones


# Func -> FuncReturn | FuncVoid
def p_func1(subexpressions):
  '''func : funcReturn'''
  subexpressions[0] = subexpressions[1]

def p_func2(subexpressions):
  '''func : funcVoid'''
  subexpressions[0] = subexpressions[1]


# FuncReturn -> FuncInt | FuncString | FuncBool
def p_funcReturn1(subexpressions):
  '''funcReturn : funcInt'''
  subexpressions[0] = subexpressions[1]

def p_funcReturn2(subexpressions):
  '''funcReturn : funcString'''
  subexpressions[0] = subexpressions[1]

def p_funcReturn3(subexpressions):
  '''funcReturn : funcBool'''
  subexpressions[0] = subexpressions[1]



#ATENCION: para simplificar, o no, hice que las funciones tomen valores. Despues hay que restringirle el tipo 
#La otra opcion es ir separando , x ej, la primera recibiria un emat o valorMat. Asi con los otros

def p_funcInt1(subexpressions):
  '''funcInt : MULTIESCALAR '(' valores ',' valores   param ')' '''
  subexpressions[0] = toString(subexpressions)


def p_funcInt2(subexpressions):
  '''funcInt : LENGTH '(' valores ')' '''
  subexpressions[0] = toString(subexpressions)

# FuncString -> capitalizar(eMat)
#Aca lo mismo que en la de arriba, recibe un "string"

def p_funcString(subexpressions):
  '''funcString : CAPITALIZAR '(' valores ')' '''
  subexpressions[0] = toString(subexpressions)

# FuncBool -> colineales(Vec,Vec )
def p_funcBool(subexpressions):
  '''funcBool : COLINEALES '(' valores ',' valores ')' '''
  subexpressions[0] = toString(subexpressions)

# FuncVoid -> print(Valores) 
def p_funcVoid(subexpressions):
  '''funcVoid : PRINT '(' valores ')' '''
  subexpressions[0] = toString(subexpressions)

#Parametros de las funciones:

def p_param1(subexpressions):
  '''param : ',' valores'''
  subexpressions[0] = toString(subexpressions)

def p_param2(subexpressions):
  '''param : empty'''
  subexpressions[0] = toString(subexpressions)

def p_empty(subexpressions):
  '''empty : '''
  subexpressions[0] = toString(subexpressions)

#-----------------------------------------------------------------------------
#Vectores  y variables


def p_vec1(subexpressions):
  '''vec : '[' elem ']' '''
  subexpressions[0] = toString(subexpressions)

#Elem-> Valores, Elem | Valores
def p_elem1(subexpressions):
  '''elem : valores ',' elem'''
  subexpressions[0] = toString(subexpressions)

def p_elem2(subexpressions):
  '''elem : valores'''
  subexpressions[0] = toString(subexpressions)

def p_valores(subexpressions):
  '''valores : eMat
  | expBool
  | funcReturn
  | reg
  | INT
  | FLOAT
  | STRING
  | BOOL
  | varYVals
  | varsOps
  | vec
  | ternarioVars
  | '(' ternarioVars ')'
  | atributos
  | RES'''
  subexpressions[0] = toString(subexpressions)

def p_atributos(subexpressions):
  '''atributos : ID '.' valoresCampos'''
  subexpressions[0] = toString(subexpressions)

def p_valoresCampos(subexpressions):
  '''valoresCampos : varYVals
  | END
  | BEGIN'''
  subexpressions[0] = toString(subexpressions)

def p_ternarioVars(subexpressions):
  '''ternarioVars : valoresBool '?' valoresTernarioVars ':' valoresTernarioVars  
  | expBool '?' valoresTernarioVars ':' valoresTernarioVars
  '''
  subexpressions[0] = toString(subexpressions)

def p_valoresTernarioVars(subexpressions):
  '''valoresTernarioVars : varsOps
  | varYVals
  | reg
  | vec
  | ternarioVars
  | '(' ternarioVars ')'
  | valoresTernarioMat
  | valoresTernarioBool
  | atributos
  | RES'''
  subexpressions[0] = toString(subexpressions)

#VarYVals -> var | VecVal
def p_varYVals1(subexpressions):
  '''varYVals : ID'''
  subexpressions[0] = toString(subexpressions)

def p_varYVals2(subexpressions):
  '''varYVals : vecVal
    | vecVal '.' varYVals
  '''
  subexpressions[0] = toString(subexpressions)

#VecVal ->  var M
def p_vecVal1(subexpressions):
  '''vecVal : ID m'''
  subexpressions[0] = toString(subexpressions)

#Aca se volvio un poco turbio, pero debe poder pasar esto g[b] 
#Entonces, mas general deberia poder pasar g[h[t[a]]] mientras los tipos anden :)
def p_m1(subexpressions):
  '''m : '[' INT ']' '''
  subexpressions[0] = toString(subexpressions)
def p_m2(subexpressions):
  ''' m : '[' INT ']' m '''
  subexpressions[0] = toString(subexpressions)
def p_m3(subexpressions):
  ''' m : '[' varYVals ']' m '''
  subexpressions[0] = toString(subexpressions)
def p_m4(subexpressions):
  ''' m : '[' varYVals ']' '''
  subexpressions[0] = toString(subexpressions)
# a[3*4]
def p_m5(subexpressions):
 ''' m : '[' eMat ']' m '''
 subexpressions[0] = toString(subexpressions)
def p_m6(subexpressions):
 ''' m : '[' eMat ']' '''
 subexpressions[0] = toString(subexpressions)


#Registros:
#Reg -> {U}
def p_reg(subexpressions):
  '''reg :  '{' campos '}' '''
  subexpressions[0] = toString(subexpressions)

#U -> campo: Valores, U | campof: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string(!)
#Me parece que mejore el campo es un ID (!)
def p_campos1(subexpressions):
  '''campos : ID ':' valores ',' campos'''
  subexpressions[0] = toString(subexpressions)
def p_campos2(subexpressions):
  '''campos : ID ':' valores'''
  subexpressions[0] = toString(subexpressions)


#-----------------------------------------------------------------------------
#Operadores de variables:
#VarsOps -> --SMM | ++SMM | SMM
def p_varsOps1(subexpressions):
  '''varsOps : MENOSMENOS varYVals 
  | MASMAS varYVals
  | varYVals MASMAS 
  | varYVals MENOSMENOS'''
  subexpressions[0] = toString(subexpressions)
  
#-----------------------------------------------------------------------------
#Asignaciones:

#Dejo las asignaciones no ambiguas como estaban antes
def p_valoresAsig(subexpressions):
  '''valoresAsig : valores'''
  subexpressions[0] = toString(subexpressions)

#Aca pongo varYvals por este caso g[a] = b;

def p_varAsig(subexpressions):
  '''varAsig : varYVals MULEQ valoresAsig
  | varYVals DIVEQ valoresAsig
  | varYVals MASEQ valoresAsig
  | varYVals MENOSEQ valoresAsig
  | varYVals '=' valoresAsig
  | ID '.' ID '=' valoresAsig'''
  subexpressions[0] = toString(subexpressions)

#-----------------------------------------------------------------------------
#Operaciones binarias enteras

# Coloco string aqui, luego chequeamos tipos para cuando se use
# las operaciones solo para INT
def p_valoresMat(subexpressions):
  '''valoresMat : INT
  | FLOAT
  | funcInt
  | varYVals
  | varsOps
  | STRING'''
  subexpressions[0] = toString(subexpressions)

def p_ternarioMat(subexpressions):
  '''ternarioMat : valoresBool '?' valoresTernarioMat ':' valoresTernarioMat  
  | expBool '?' valoresTernarioMat ':' valoresTernarioMat
  '''
  subexpressions[0] = toString(subexpressions)

def p_valoresTernarioMat(subexpressions):
  '''valoresTernarioMat : INT
  | FLOAT
  | funcInt
  | STRING
  | eMat'''
  subexpressions[0] = toString(subexpressions)

#EMat -> EMat '+' P | EMat - P | P
def p_eMat(subexpressions):
    '''eMat : eMat '+' p
    | eMat '-' p
    | valoresMat '+' p
    | valoresMat '-' p
    | eMat '+' valoresMat
    | eMat '-' valoresMat
    | valoresMat '+' valoresMat
    | valoresMat '-' valoresMat
    | p'''
    subexpressions[0] = toString(subexpressions)

#P -> P * Exp | P / Exp | P % Exp | Exp

def p_p(subexpressions):
    '''p : p '*' exp
    | p '/' exp
    | p '%' exp
    | valoresMat '*' exp
    | valoresMat '/' exp
    | valoresMat '%' exp
    | p '*' valoresMat
    | p '/' valoresMat
    | p '%' valoresMat
    | valoresMat '*' valoresMat
    | valoresMat '/' valoresMat
    | valoresMat '%' valoresMat
    | exp
    '''
    subexpressions[0] = toString(subexpressions)

#Exp -> Exp ^ ISing | ISing
def p_exp(subexpressions):
  '''exp : exp '^' iSing
  | valoresMat '^' iSing
  | exp '^' valoresMat
  | valoresMat '^' valoresMat
  | iSing'''
  subexpressions[0] = toString(subexpressions)

#ISing -> -Paren | '+'Paren | Paren
def p_iSing(subexpressions):
  '''iSing : '-' paren
  | '+' paren
  | '-' valoresMat
  | '+' valoresMat
  | paren
  '''
  subexpressions[0] = toString(subexpressions)

#Paren -> (EMat) | int | VarYVals | float | VarsOps| FuncInt
def p_paren1(subexpressions):
  '''paren : '(' eMat ')' 
  | '(' valoresMat ')'
  '''
  subexpressions[0] = toString(subexpressions)

# ---------------------------------------------------------------------------------------
# Expresiones booleanas

#Aca agrego int y float y emat y STRING porque si no lo que sigue no se puede generar
#(x > 5 ? y : 10) o f ? 3 : x + 5
#Esto tambien daria lugar a cosas como 
#(2? 3 : 4) que tiene cierto sentido (porque 2 es siempre true). Si no, se puede filtrar con atributos.

def p_valoresBool(subexpressions):
  '''valoresBool : BOOL
  | funcBool
  | varYVals
  | varsOps'''
  subexpressions[0] = toString(subexpressions)

def p_ternarioBool(subexpressions):
  '''ternarioBool : valoresBool '?' valoresTernarioBool ':' valoresTernarioBool  
  | expBool '?' valoresTernarioBool ':' valoresTernarioBool
  '''
  subexpressions[0] = toString(subexpressions)

def p_valoresTernarioBool(subexpressions):
  '''valoresTernarioBool : BOOL
  | funcBool
  | expBool
  '''
  subexpressions[0] = toString(subexpressions)
  
def p_ternario(subexpressions):
  '''ternario : valoresBool '?' valores ':' valores  
  | expBool '?' valores ':' valores
  | '(' ternario ')' '''
  subexpressions[0] = toString(subexpressions)

# Or -> Or or And | And
def p_expBool(subexpressions):
  '''expBool : expBool OR and
  | valoresBool OR and
  | expBool OR valoresBool
  | valoresBool OR valoresBool
  | and'''
  subexpressions[0] = toString(subexpressions)

# And ->  And and Eq | Eq
def p_and(subexpressions):
  '''and : and AND eq
  | valoresBool AND eq
  | and AND valoresBool
  | valoresBool AND valoresBool
  | eq'''
  subexpressions[0] = toString(subexpressions)

# Eq -> Eq == TBool |  Eq != TBool | Mayor 
def p_eq(subexpressions):
  '''eq : eq EQEQ mayor
  | eq DISTINTO mayor
  | tCompare EQEQ mayor
  | tCompare DISTINTO mayor
  | eq EQEQ tCompare
  | eq DISTINTO tCompare
  | tCompare EQEQ tCompare
  | tCompare DISTINTO tCompare
  | mayor'''
  subexpressions[0] = toString(subexpressions)

# TCompare -> EMat | VarsOps | VarYVals
#Aca agrego para que puedan aparecer ints o floats solos por ej 5 < 5, emat no lo captura
def p_tCompare(subexpressions):
  '''tCompare : eMat
  | varsOps
  | varYVals
  | INT
  | funcInt 
  | FLOAT'''
  subexpressions[0] = toString(subexpressions)

# Mayor -> TCompare > TCompare | Menor
def p_mayor(subexpressions):
  '''mayor : tCompare '>' tCompare
  | menor'''
  subexpressions[0] = toString(subexpressions)

  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")


# Menor -> TCompare < TCompare | Not 
def p_menor3(subexpressions):
  '''menor : tCompare '<' tCompare
  | not'''
  subexpressions[0] = toString(subexpressions)
  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")
# Not ->  not Not | TBool 
def p_not(subexpressions):
  '''not :  NOT not
  | NOT valoresBool
  | parenBool'''
  subexpressions[0] = toString(subexpressions)

# TBool -> (ExpBool) | bool | VarYVals | FuncBool
def p_parenBool(subexpressions):
  '''parenBool : '(' expBool ')' '''
  subexpressions[0] = toString(subexpressions)
  # if len(subexpressions) == 2:
  #   tokens = [subexpressions[1]]
  #   if not chequearTipo(tokens, ["bool"]):
  #     raise SemanticException("Se esperaba tipo bool")

#--------------------------------------------------------------------------------------
# Caso error

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

#------------------------------------------------------------------------------
# Funciones auxiliares 

def toString(subexpressions):
  res = ""
  for exp in subexpressions[1:]:
    res += str(exp)
  return res

# #chequea si todos los elementos de la lista de subexpresiones son de 
# algun tipo de la lista tipos
def chequearTipo(subexps, tipos):

    for subexp in subexps:
        if subexp["type"] not in tipos:
            message = "[] Se esperaba tipo "
            message += listTypes(tipos)
            raise Exception(message)

    pass

def listTypes(tipos):
    print tipos
    if len(tipos) == 1:
        return tipos[0]

    if len(tipos) == 2:
        return tipos[0] + " o " + tipos[1]

    message = tipos[0]
    for i in range(1, len(tipos)-1):
        message += ", " + tipos[i]

    message += " o " + tipos[len(tipos)-1]
    return message

# Por cada operador (binario, unario, ternario) hay un chequeador de tipos
# Pueden usarlo sin importar si hay otro tipo de operador en la misma regla
# Cada una chequea que sea su tipo de operador el de la expresion,
# comparando la longitud de la lista
# Si hay otro operador con la misma cantidad de elementos y no es de estos tipos hay que tener
# cuidado
# Cada chequeador, en caso de falla, levanta una excepcion con los tipos esperados
def chequeadorBinario(subexpressions, tipos):
    if len(subexpressions) == 4:
        subexps = [ subexpressions[1], subexpressions[3] ]
        chequearTipo(subexps, tipos)

    pass

def chequeadorUnarioPrefijo(subexpressions, tipos):
    if len(subexpressions) == 3:
        subexps = [ subexpressions[2] ]
        chequearTipo(subexps, tipos)

    pass

def chequeadorUnarioPostfijo(subexpressions, tipos):
    if len(subexpressions) == 3:
        subexps = [ subexpressions[1] ]
        chequearTipo(subexps, tipos)

    pass

def chequeadorTernario(subexpressions, tipos):
    if len(subexpressions) == 6:

        if subexpressions[3]["type"] != subexpressions[5]["type"]:
            raise Exception("Los valores de retorno del operador ? tiene que ser del mismo tipo")

    pass








