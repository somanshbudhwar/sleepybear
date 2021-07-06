import glob
# All files ending with .txt
files = glob.glob("Anthropology/Anthro Prehistory/*.html")
names = [filename.replace('Anthropology/Anthro Prehistory/','') for filename in files]
names = [filename.replace('.html','') for filename in names]
names = [filename.replace('1-2','') for filename in names]
names = [filename.replace('1-1','') for filename in names]
names = [filename.replace('2-2','') for filename in names]
# print(names)
addresses = [filename.replace('Anthropology/','') for filename in files]
# print(addresses)

lizzy = []
for address, name in zip(addresses, names):
    print('<li> &bullet; &nbsp;&nbsp;<a target="_blank" href="'+address+'" class="nav-link-item"> '+name+' </a> </li>')
#     lizzy.append()

# for i in lizzy:
#     print(i)