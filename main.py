import sys
from build import build_demo

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        build_demo()

if __name__ == "__main__":
    main()

