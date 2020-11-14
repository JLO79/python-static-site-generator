from pathlib import Path
import os

class Site():
    def __init__(self,source,dest):
        print("Class SITE : def __init__")
        self.dest=Path(dest)
        self.source = Path(source)

    def create_dir(self,path):
        # directory
        # This variable will need to contain the full path to the
        # destination folder.
        print("Class SITE : def create_dir")
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
        print("    ", directory)

    def build(self):
        print("Class SITE : def Build")
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
