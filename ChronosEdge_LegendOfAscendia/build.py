import os
import shutil
import subprocess

def build_demo():
    try:
        os.mkdir("demo_build")
        shutil.copytree("path/to/necessary/files", "demo_build")
        # Modify line 8: Specify the paths for the necessary files in the `shutil.copytree()` function.
        # Example: shutil.copytree("path/to/source", "demo_build/source")
        os.chdir("demo_build")
        subprocess.run("compile_command")
        # Modify line 10: Specify the compile command in the `subprocess.run()` function.
        # Example: subprocess.run("compile_command", shell=True)
        os.chdir("..")
        shutil.make_archive("demo", "zip", "demo_build")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Build process complete.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

build_dem

