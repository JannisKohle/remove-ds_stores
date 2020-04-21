import os

path = "../.."  # CHANGE THIS

see_noEnding_message = True  # CHANGE THIS

file_endings = [".txt", ".json", ".py", ".html", ".css",
                ".js", ".md", ".csv", ".c", ".cpp", ".pyc", ".swift", ".plaintext", ".png", ".jpg", "config", ".git", ".tif", ".iml", ".xml", ".egg", ".pth", ".cfg", ".csh"]  # CHANGE THIS


def not_ends_with_one(s, l):
    for i in l:
        if s.endswith(i):
            return False

    return True


def rm_here():
    global file_endings
    global see_noEnding_message

    if ".DS_Store" in os.listdir("."):
        os.system("rm -rf .DS_Store")

    folders = [i for i in os.listdir(".") if not_ends_with_one(i, file_endings)]  # get all folders

    for i in folders:
        try:
            os.chdir(i)
            rm_here()
        except NotADirectoryError:  # i is a file
            if see_noEnding_message:
                print(f"{os.getcwd()}/{i} is a file without an ending")
            else:
                pass

    os.chdir("..")


os.chdir(path)  # go to my projects folders

rm_here()
