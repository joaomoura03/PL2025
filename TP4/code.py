import ply.lex as lex

# Lista de nomes de tokens
tokens = [
    'SELECT',
    'WHERE',
    'LIMIT',
    'PREFIX',
    'IRI',
    'VARIABLE',
    'LITERAL',
    'DOT',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'LCURLY',
    'RCURLY',
    'LANGTAG',
    'A',
    'PREFIXNAME',
    'NUMBER'
]

# Expressões regulares para tokens simples
t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_LIMIT = r'[Ll][Ii][Mm][Ii][Tt]'
t_PREFIX = r'[Pp][Rr][Ee][Ff][Ii][Xx]'
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LANGTAG = r'@[a-zA-Z]+'
t_A = r'[Aa]'

# Expressão regular para prefixos
def t_PREFIXNAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Expressões regulares com ações associadas
def t_IRI(t):
    r'<[^>]*>'
    return t

def t_VARIABLE(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_LITERAL(t):
    r'\"([^\\\"]|\\.)*\"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t\n'

# Função para tratar erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Testar o lexer
data = "?s a dbo:MusicalArtist"

lexer.input(data)

# Tokenizar
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)