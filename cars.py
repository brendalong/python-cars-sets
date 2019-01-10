# take 1 - define a set with parens and add
showroom1 = set()
showroom1.add("mini")
showroom1.add("limo")
## another way

showroom  = set(["mini", "limo", "truck", "van"])
print("showroom", len(showroom))
showroom.add("limo")
#only adds unique items
print(showroom)
newcars = set(["mazda", "chevy"])
showroom.update(newcars)
print("new showroom", showroom)
showroom.discard("mini")
print(showroom)
#can use remove or discard
#discard will not show error if item does not exist while remove will
print(showroom)
print("hi")
junkyard = set(["dodge", "volkswagon", "mini", "four-wheel", "moped", "chevy", "mini"])
samecars = junkyard.intersection(showroom)
print("samecars", samecars)
new_showroom = showroom.union(junkyard)
print("new_showroom", new_showroom)

