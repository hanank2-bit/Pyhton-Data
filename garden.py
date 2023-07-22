import spacy

nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "The old dog the footsteps of the young.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    for token in doc:
        print("Token:", token.text, "\tEntity:", token.ent_type_, "\tExplanation:", spacy.explain(token.ent_type_))
    print("\n")

# Entity 1: PERSON
# Explanation: People, including fictional.
# The entity "PERSON" refers to individuals, including both real and fictional characters. It makes sense in terms of the word associated with it as it can represent names of people.

# Entity 2: GPE
# Explanation: Countries, cities, states.
# The entity "GPE" stands for "Geo-Political Entity" and represents countries, cities, and states. It makes sense in terms of the word associated with it as it can indicate a specific geographic location.
