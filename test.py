import wikipedia
wikipedia.set_lang("en")
print(wikipedia.search("rum",suggestion=False))
print(wikipedia.suggest("hot do"))
# x = wikipedia.page("New York")
# print(x.title)
