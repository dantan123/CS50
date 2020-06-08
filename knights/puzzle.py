from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# rules
general = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight, CKnave))
)
# Puzzle 0
# A says "I am both a knight and a knave."
sentence0A = And(AKnight, AKnave) # what A said
knowledge0 = And(
    general,
    Implication(AKnight, sentence0A), # A is a Knight, the sentence is true because Knight doesn't lie
    Implication(AKnave,Not(sentence0A)) # A is a Knave, the sentence is false because Knave always lies
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence1A = And(AKnave, BKnave) # what A said
knowledge1 = And(
    general,
    Implication(AKnight, sentence1A), 
    Implication(AKnave, Not(sentence1A))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2A = Or(And(AKnight, BKnight), And(AKnave, BKnave)) # what A said
sentence2B = Or(And(AKnight, BKnave), And(BKnight, AKnave)) # what B said
knowledge2 = And(
    general,
    Implication(AKnave, Not(sentence2A)),
    Implication(AKnight, sentence2A),
    Implication(BKnave, Not(sentence2B)),
    Implication(BKnight, sentence2B)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence3A = Or(AKnight, AKnave) # what A said
sentence3B1 = Implication(Or(AKnight, AKnave), AKnave) # what B said
sentence3B2 = CKnave # what B said
sentence3C = AKnight # what C said
knowledge3 = And(
    general,
    Implication(AKnight, sentence3A),
    Implication(AKnave, Not(sentence3A)),
    Implication(BKnight, And(sentence3B1, sentence3B2)), # if B is Knight, both of these statements must be correct
    Implication(BKnave,Not(Or(sentence3B1,sentence3B2))), # if B is Knave, one of these statements must be wrong
    Implication(CKnight, sentence3C),
    Implication(CKnave, Not(sentence3C))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
