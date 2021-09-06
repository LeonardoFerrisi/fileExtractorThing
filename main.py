import shutil, os

"""
Copies all the files in each subdirectory and pulls them
into main direcotry
"""

rootDir = input("Please input the root directory: ")
print(str(rootDir))

counter = 0
subDirectories = os.listdir(rootDir)

extension = input("Please input the extension of the files you want to copy and pull: ")
for root, dirs, files in os.walk(rootDir):
    for file in files:
        try:
            # if file.endswith(".txt"):
            if file.endswith(str(extension)):
                print("Found file: " + str(file))
                sourcePath = os.path.join(os.getcwd(), str(root), str(file))

                # Separate base from extension
                print("Separating base from extension and adding numerical identifier. . .")
                base, extension = os.path.splitext(file)
                # Initial new name
                addOn = str(counter)
                newFileName = os.path.join(rootDir, base + addOn + extension)
                print(newFileName)
                destinationPath = os.path.join(os.getcwd(), str(root), newFileName)
                # print(destinationPath)

                # print(sourcePath)
                print("Moving " + str(newFileName) + " from " + str(sourcePath) + " to " + str(destinationPath))
                shutil.copyfile(sourcePath, destinationPath)
                copiedFilePath = destinationPath
                # outputPath = os.path.join(str(rootDir), newFileName)
                # shutil.move(copiedFilePath, outputPath)
                counter += 1
        except:
            pass