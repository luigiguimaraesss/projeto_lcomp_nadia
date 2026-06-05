from rules import RULES

class Validator:
    def __init__(self, proof):
        # Armazena a prova que será validada
        self.proof = proof

    def validate(self):

        # Percorre as linhas da prova em ordem crescente
        for line_number in sorted(self.proof.keys()):

            # Obtém a linha atual da prova
            line = self.proof[line_number]

            # Verifica se a regra usada existe
            if line.rule not in RULES:

                print(
                    f"Regra desconhecida "
                    f"na linha {line_number}"
                )

                return False

            # Recupera o objeto da regra
            rule = RULES[line.rule]

            try:
                # Executa a validação da linha
                valid = rule.validate(
                    line,
                    self.proof
                )

            except Exception as e:
                # Trata erros internos da regra
                print(
                    f"Erro interno "
                    f"na linha {line_number}: {e}"
                )

                return False

            # Se a regra considerar a linha inválida
            if not valid:

                print(
                    f"Linha "
                    f"{line_number} inválida"
                )

                return False

        # Todas as linhas passaram na validação
        return True