# Importa a classe responsável por converter o texto da prova em uma estrutura de dados.
from proof import ProofParser

# Importa a classe responsável por validar
from validator import Validator

# Importa a lista contendo todas as provas
from proofs import ALL_PROOFS


def run_proof(text):
    """
    Todo o processo de análise de uma prova:
    1. Exibe a prova.
    2. Faz o parsing do texto.
    3. Valida a prova.
    4. Exibe o resultado.
    """

    print('=' * 60)

    # Mostra a prova que está sendo analisada.
    print(text)

    # Cria o objeto responsável por interpretar o texto da prova.
    parser = ProofParser(text)

    # Converte o texto da prova em uma estrutura que o programa consegue manipular.
    proof = parser.parse()

    # Cria o validador utilizando a prova já processada.
    validator = Validator(proof)

    # Executa a validação da prova.
    # Retorna True se for válida e False caso contrário.
    result = validator.validate()

    # Exibe o resultado da validação.
    print(
        'RESULTADO:',
        'PROVA VÁLIDA'
        if result
        else 'PROVA INVÁLIDA'
    )

    print('=' * 60)


if __name__ == '__main__':

    # Percorre todas as provas disponíveis.
    for proof_text in ALL_PROOFS:

        # Executa o processo completo de análise para cada prova encontrada.
        run_proof(proof_text)