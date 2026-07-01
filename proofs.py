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

proof_text_implies_intro_valid = """
1. p pre      
2. p->p ->i 1,1  
"""
# ✅ VÁLIDA

proof_text_implies_intro_valid_2 = """
1. p pre
2. q pre
3. p copy 1
4. q->p ->i 2,3
"""
# ✅ VÁLIDA: Prova que a partir de 'p', se assumirmos 'q', podemos introduzir 'q -> p'

proof_text_invalid_implies_1 = """
1. p pre
2. q pre
3. (p&q) &i 1,2
4. q &e2 3
5. q->p ->i 2,4
"""
# ❌ INVÁLIDA
# A subprova começou na linha 2 (com 'q') e terminou na linha 4 (com 'q').
# A regra ->i deveria gerar (q -> q), mas tentou gerar (q -> p).

proof_text_invalid_implies_2 = """
1. p pre
2. q pre
3. (p&q) &i 1,2
4. q->r ->i 2,3
"""
# ❌ INVÁLIDA
# A subprova inicia em 'q' (linha 2) e termina em '(p&q)' (linha 3).
# O resultado correto deveria ser q -> (p&q). 
# Tentar concluir q -> r quebra a validação da estrutura.

proof_text_intro_valid_3 = """
1. (p&q)->r pre
2. p pre          
3. q pre          
4. (p&q) &i 2,3   
5. r ->e 1,4      
6. q->r ->i 3,5   
7. p->(q->r) ->i 2,6 
"""
# ✅ VÁLIDA

ALL_PROOFS = [
    proof_text_implies_intro_valid,
    proof_text_implies_intro_valid_2,
    proof_text_invalid_implies_1,  
    proof_text_invalid_implies_2,
    proof_text_intro_valid_3
]
