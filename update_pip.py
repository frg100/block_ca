####
import os

file = open("setup.py", "r+")

text = file.read()
text = list(text)

file.seek(142)
print "Current version: " + file.read(5)
file.close()

version = raw_input("\nWhat is the updated version?: ")

text[143] = version[0]
text[145] = version[2]

text[433] = version[0]
text[435] = version[2]

file = open("setup.py", "w")

file.write("".join(text) )
file.close()
print "\nDone!"

os.system("""git tag %s -m "" """ %(version) )
os.system("git push --tags origin master")
os.system("python setup.py sdist upload -r pypi")

