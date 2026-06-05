proof_text_1 = """
1. p->q pre
2. p pre
3. q ->e 1,2
"""


proof_text_2 = """
1. p pre
2. q pre
3. (p&q) &i 1,2
4. p &e1 3
"""


proof_text_3 = """
1. (p&q)->r pre
2. p pre
3. q pre
4. (p&q) &i 2,3
5. r ->e 1,4
"""


proof_text_4 = """
1. p pre
2. q pre
3. (p&q) &i 1,2
4. q &e2 3
"""


proof_text_invalid = """
1. p->q pre
2. r pre
3. q ->e 1,2
"""


ALL_PROOFS = [
    proof_text_1,
    proof_text_2,
    proof_text_3,
    proof_text_4,
    proof_text_invalid
]