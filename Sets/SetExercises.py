"""
1.) Split the string of text into a list
2.) Find the set of prepositions as defined in the list of words
"""


text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
def return_set(text: str, prep: set) -> set:
    set_of_words = set(text.split())

    return(set_of_words.intersection(prepositions))

preps_used = return_set(text=text, prep=prepositions)
print(preps_used)


"""
get the list of favourites that aren't already in their basket
"""

favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          }

def get_suggestions(fav: set, basket: set) -> set:
    suggestions = favourites.difference(basket)

    return sorted(suggestions)

suggestions = get_suggestions(favourites, basket)
print(suggestions)
