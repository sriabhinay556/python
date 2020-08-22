items = input("Input comma separated sequence of words")
set_items = {word for word in items.split(",")}
print(",".join(sorted(set_items)))
