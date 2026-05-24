import re

from parser import parse_formula


class ProofLine:

    def __init__(
        self,
        number,
        formula,
        rule,
        refs
    ):

        self.number = number
        self.formula = formula
        self.rule = rule
        self.refs = refs


class ProofParser:

    def __init__(self, text):
        self.text = text

    def parse(self):

        proof = {}

        for raw_line in self.text.strip().split('\n'):

            raw_line = raw_line.strip()

            if not raw_line:
                continue

            match = re.match(
                r'(\d+)\.\s+(.*?)\s+([a-zA-Z\-\>\&0-9]+)(?:\s+(.*))?',
                raw_line
            )

            if not match:

                raise SyntaxError(
                    f"Linha inválida: {raw_line}"
                )

            number = int(match.group(1))
            formula_text = match.group(2)
            rule = match.group(3)
            refs_text = match.group(4)

            refs = []

            if refs_text:

                refs = [
                    int(x.strip())
                    for x in refs_text.split(',')
                ]

            formula = parse_formula(
                formula_text
            )

            proof[number] = ProofLine(
                number,
                formula,
                rule,
                refs
            )

        return proof