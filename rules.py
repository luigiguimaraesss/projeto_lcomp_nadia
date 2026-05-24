from formulas import *


class Rule:

    def validate(self, line, proof):
        raise NotImplementedError


# ==========================================================
# PREMISSA
# ==========================================================

class PremiseRule(Rule):

    def validate(self, line, proof):
        return True


# ==========================================================
# CONJUNÇÃO INTRODUÇÃO
# ==========================================================

class AndIntroduction(Rule):

    def validate(self, line, proof):

        left = proof[
            line.refs[0]
        ].formula

        right = proof[
            line.refs[1]
        ].formula

        expected = And(
            left,
            right
        )

        return (
            line.formula == expected
        )


# ==========================================================
# CONJUNÇÃO ELIMINAÇÃO ESQUERDA
# ==========================================================

class AndElimLeft(Rule):

    def validate(self, line, proof):

        source = proof[
            line.refs[0]
        ].formula

        if not isinstance(source, And):
            return False

        return (
            line.formula == source.left
        )


# ==========================================================
# CONJUNÇÃO ELIMINAÇÃO DIREITA
# ==========================================================

class AndElimRight(Rule):

    def validate(self, line, proof):

        source = proof[
            line.refs[0]
        ].formula

        if not isinstance(source, And):
            return False

        return (
            line.formula == source.right
        )


# ==========================================================
# MODUS PONENS
# ==========================================================

class ImplicationElimination(Rule):

    def validate(self, line, proof):

        implication = proof[
            line.refs[0]
        ].formula

        premise = proof[
            line.refs[1]
        ].formula

        if not isinstance(
            implication,
            Implies
        ):
            return False

        return (
            implication.left == premise
            and implication.right == line.formula
        )


# ==========================================================
# REGISTRO DAS REGRAS
# ==========================================================

RULES = {
    'pre': PremiseRule(),
    '&i': AndIntroduction(),
    '&e1': AndElimLeft(),
    '&e2': AndElimRight(),
    '->e': ImplicationElimination(),
}