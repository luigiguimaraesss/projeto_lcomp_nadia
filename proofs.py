proof_text_1 = """
1. p->q pre
2. p pre
3. q ->e 1,2
"""
# ✅ VÁLIDA
# Modus ponens clássico:
# p->q e p ⟹ q


proof_text_2 = """
1. p pre
2. q pre
3. (p&q) &i 1,2
4. p &e1 3
"""
# ✅ VÁLIDA
# Introduz a conjunção (p&q)
# Depois extrai p corretamente usando &e1


proof_text_3 = """
1. (p&q)->r pre
2. p pre
3. q pre
4. (p&q) &i 2,3
5. r ->e 1,4
"""
# ✅ VÁLIDA
# Primeiro cria (p&q)
# Depois aplica modus ponens:
# (p&q)->r e (p&q) ⟹ r


proof_text_4 = """
1. p pre
2. q pre
3. (p&q) &i 1,2
4. q &e2 3
"""
# ✅ VÁLIDA
# Cria (p&q)
# Extrai q corretamente usando &e2


proof_text_invalid = """
1. p->q pre
2. r pre
3. q ->e 1,2
"""
# ❌ INVÁLIDA
# Modus ponens aplicado incorretamente
# Precisaria ter p, mas possui r


proof_text_5 = """
1. p->q pre
2. q->r pre
3. p pre
4. q ->e 1,3
5. r ->e 2,4
"""
# ✅ VÁLIDA
# Encadeamento de implicações:
# p->q, q->r e p
# Logo q e depois r


proof_text_6 = """
1. p pre
2. q pre
3. (p&q) &i 1,2
4. p &e1 3
5. q &e2 3
"""
# ✅ VÁLIDA
# Introduz conjunção
# Depois extrai corretamente ambos os lados


proof_text_invalid_2 = """
1. p->q pre
2. q pre
3. p ->e 1,2
"""
# ❌ INVÁLIDA
# Falácia da afirmação do consequente
# De p->q e q NÃO podemos concluir p


proof_text_invalid_3 = """
1. p pre
2. q pre
3. (p|q) &i 1,2
"""
# ❌ INVÁLIDA
# A regra &i cria conjunção (&)
# Não pode produzir disjunção (|)


proof_text_invalid_4 = """
1. (p&q)->r pre
2. p pre
3. r ->e 1,2
"""
# ❌ INVÁLIDA
# Para usar ->e seria necessário possuir (p&q)
# Apenas p sozinho não satisfaz o antecedente


ALL_PROOFS = [
    proof_text_1,
    proof_text_2,
    proof_text_3,
    proof_text_4,
    proof_text_invalid,
    proof_text_5,
    proof_text_6,
    proof_text_invalid_2,
    proof_text_invalid_3,
    proof_text_invalid_4
]