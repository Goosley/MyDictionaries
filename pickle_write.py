import pickle

outfile = open("names_file.dat", "wb")

names = []
name = input("add a name: ")

names.append(name)

pickle.dump(names, outfile)

outfile.close()
