import os

dir=[
    os.path.join("data","raw_data"),
    os.path.join("data","processed"),
    "src",
    "notebooks",
    "save_models"]

for dir_ in dir:
    os.makedirs(dir_)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

files=[
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "readme.amd",
    ".gitignore"

]

for files_ in files:
    with open(files_,"w") as f:
        pass
