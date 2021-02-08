import pickle

infile = open("names_file.dat", "rb")

names = pickle.load(infile)

print(type(names))
print(names)

name = input("add a name: ")

names.append(name)

print(names)