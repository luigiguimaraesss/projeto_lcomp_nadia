from lexer import Lexer
from formulas import *


class Parser:

    def __init__(self, tokens):
        
        # Lista de tokens gerada pelo lexer
        self.tokens = tokens

        # Posição atual dentro da lista
        self.pos = 0

    def current(self):

        # Retorna o token atual
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]

        return None

    def eat(self, token_type):

        token = self.current()

        # Verifica se o token atual é o esperado
        if token and token.type == token_type:

            # Avança para o próximo token
            self.pos += 1

            return token

        raise SyntaxError(
            f"Esperado {token_type}"
        )

    def parse(self):

        # Inicia o parser pela operação de menor precedência
        return self.parse_iff()

    
    # BICONDICIONAL

    def parse_iff(self):

        # Lê o lado esquerdo da expressão
        left = self.parse_implication()

        # Continua enquanto existir ↔
        while (
            self.current()
            and self.current().type == 'IFF'
        ):

            # Consome o token ↔
            self.eat('IFF')

            # Lê o lado direito
            right = self.parse_implication()

            # Cria a AST do bicondicional
            left = Iff(left, right)

        return left

    
    # IMPLICAÇÃO

    def parse_implication(self):

        # Lê a expressão da camada anterior
        left = self.parse_or()

        token = self.current()

        # Verifica se existe →
        if (
            token
            and token.type == 'IMPLIES'
        ):

            # Consome →
            self.eat('IMPLIES')

            # Lê o lado direito
            right = self.parse_implication()

            # Cria a AST da implicação
            return Implies(left, right)

        return left
    

    # DISJUNÇÃO

    def parse_or(self):

        # Lê a expressão anterior
        left = self.parse_xor()

        # Continua enquanto existir ∨
        while (
            self.current()
            and self.current().type == 'OR'
        ):

            # Consome ∨
            self.eat('OR')

            # Lê o lado direito
            right = self.parse_xor()

            # Cria a AST da disjunção
            left = Or(left, right)

        return left
    

    # XOR

    def parse_xor(self):

        # Lê a expressão anterior
        left = self.parse_and()

        # Continua enquanto existir XOR
        while (
            self.current()
            and self.current().type == 'XOR'
        ):

            # Consome XOR
            self.eat('XOR')

            # Lê o lado direito
            right = self.parse_and()

            # Cria a AST do XOR
            left = Xor(left, right)

        return left

    
    # CONJUNÇÃO

    def parse_and(self):

        # Lê a expressão anterior
        left = self.parse_not()

        # Continua enquanto existir ∧
        while (
            self.current()
            and self.current().type == 'AND'
        ):

            # Consome ∧
            self.eat('AND')

            # Lê o lado direito
            right = self.parse_not()

            # Cria a AST da conjunção
            left = And(left, right)

        return left

    
    # NEGAÇÃO

    def parse_not(self):

        token = self.current()

        # Verifica se existe ¬
        if (
            token
            and token.type == 'NOT'
        ):

            # Consome ¬
            self.eat('NOT')

            # Cria a AST da negação
            return Not(
                self.parse_not()
            )

        return self.parse_atom()

    
    # ÁTOMOS

    def parse_atom(self):

        token = self.current()

        # Variáveis proposicionais
        if token.type == 'ATOM':

            self.eat('ATOM')

            return Atom(token.value)

        # Expressões entre parênteses
        if token.type == 'LPAREN':

            # Consome (
            self.eat('LPAREN')

            # Faz parsing da expressão interna
            expr = self.parse_iff()

            # Consome )
            self.eat('RPAREN')

            return expr

        raise SyntaxError(
            "Fórmula inválida"
        )


def parse_formula(text):

    # Cria o lexer
    lexer = Lexer(text)

    # Gera os tokens
    tokens = lexer.tokenize()

    # Cria o parser
    parser = Parser(tokens)

    # Retorna a AST final
    return parser.parse()