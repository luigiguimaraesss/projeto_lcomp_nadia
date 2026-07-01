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
# INTRODUÇÃO DA IMPLICAÇÃO (Dedução)
# ==========================================================

class ImplicationIntroduction(Rule):

    def validate(self, line, proof):
        # A regra precisa de exatamente duas referências:
        # refs[0]: a linha da hipótese assumida (início da subprova)
        # refs[1]: a linha da conclusão obtida dentro da subprova (fim da subprova)
        if len(line.refs) < 2:
            return False

        hyp_line_num = line.refs[0]
        conc_line_num = line.refs[1]

        # Garante que as linhas referenciadas existem na prova
        if hyp_line_num not in proof or conc_line_num not in proof:
            return False

        hyp_formula = proof[hyp_line_num].formula
        conc_formula = proof[conc_line_num].formula

        # O resultado esperado na linha atual deve ser: (hipótese -> conclusão)
        expected = Implies(hyp_formula, conc_formula)

        # Avalidamos se a fórmula construída é idêntica à da linha:
        return line.formula == expected



# ==========================================================
# REGISTRO DAS REGRAS
# ==========================================================

RULES = {
    'pre': PremiseRule(),
    '&i': AndIntroduction(),
    '&e1': AndElimLeft(),
    '&e2': AndElimRight(),
    '->e': ImplicationElimination(),
    '->i': ImplicationIntroduction(),
}