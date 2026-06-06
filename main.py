from proof import ProofParser
from validator import Validator


from proofs import ALL_PROOFS


def run_proof(text):

    print('=' * 60)

    print(text)

    parser = ProofParser(text)

    proof = parser.parse()

    validator = Validator(proof)

    result = validator.validate()

    print(
        'RESULTADO:',
        'PROVA VÁLIDA'
        if result
        else 'PROVA INVÁLIDA'
    )

    print('=' * 60)


if __name__ == '__main__':

    for proof_text in ALL_PROOFS:
        run_proof(proof_text)