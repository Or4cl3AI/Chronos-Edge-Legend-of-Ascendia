import os
import shutil
import subprocess

def build_demo():
    os.mkdir("demo_build")
    shutil.copytree("path/to/necessary/files", "demo_build")
    os.chdir("demo_build")
    subprocess.run("compile_command")
    os.chdir("..")
    shutil.make_archive("demo", "zip", "demo_build")
    print("Build process complete.")

build_demo()

