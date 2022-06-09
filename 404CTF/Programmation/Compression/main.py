import tarfile
from os import listdir, system

fname = "flag2500.tar.xz"


def extract(fname):
    if fname.endswith("tar.gz"):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()
    elif fname.endswith("tar"):
        tar = tarfile.open(fname, "r:")
        tar.extractall()
        tar.close()
    elif fname.endswith("tar.xz"):
        tar = tarfile.open(fname, "r:xz")
        tar.extractall()
        tar.close()
    elif fname.endswith("tar.bz2"):
        tar = tarfile.open(fname, "r:bz2")
        tar.extractall()
        tar.close()
    else:
        print("Unknown file type")
        raise TypeError("Unknown file type")

    if fname != "flag2500.tar.xz":
        system("rm " + fname)


size_bar = 40
for i in range(2500, 0, -1):
    # list file in directory
    files = listdir(".")
    # check if file exist
    for file in files:
        if file.startswith("flag" + str(i) + ".tar"):
            fname = file
            extract(fname)
    # loading bar
    print(f"\r[{'='*abs(i//size_bar-63):<63}] {abs(i-2500)}/2500, {fname}    ", end="")
print()

