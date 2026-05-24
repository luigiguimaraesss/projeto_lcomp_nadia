import re

# Lista de padrões reconhecidos pelo lexer
TOKEN_REGEX = [
    ('IFF', r'<->'),
    ('IMPLIES', r'->'),
    ('AND', r'&'),
    ('OR', r'\|'),
    ('XOR', r'\^'),
    ('NOT', r'~'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('ATOM', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('SPACE', r'\s+'),
]


class Token:

    def __init__(self, typ, value):

        # Tipo do token
        self.type = typ
        
        # Valor encontrado no texto
        self.value = value

    def __repr__(self):

        # Representação textual do token
        return f"{self.type}:{self.value}"


class Lexer:

    def __init__(self, text):

        # Texto original da fórmula
        self.text = text

    def tokenize(self):

        # Lista final de tokens
        tokens = []
        pos = 0

        # Continua enquanto ainda existir texto
        while pos < len(self.text):

            match = None

            # Percorre todos os padrões possíveis
            for token_type, pattern in TOKEN_REGEX:

                # Compila regex
                regex = re.compile(pattern)

                # Tenta encontrar um padrão na posição atual
                match = regex.match(
                    self.text,
                    pos
                )

                # Se encontrou um token válido
                if match:

                    value = match.group(0)

                    # Ignora espaços e adiciona os outros tokens à lista
                    if token_type != 'SPACE':
                        tokens.append(
                            Token(token_type, value)
                        )

                    # Move a posição para frente
                    pos = match.end(0)

                    break
            
            # Caso nenhum padrão seja reconhecido
            if not match:

                raise SyntaxError(
                    f"Símbolo inválido: "
                    f"{self.text[pos:]}"
                )
            
        # Retorna lista final de tokens
        return tokens