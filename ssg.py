import typer
from ssg.site import Site
"""
We'll call this function main. It should accept two keyword arguments: source
with a default value of "content", and dest with a default value of "dist".

In the body of the main function, create a dictionary called config.
Add two key value pairs to config: "source" set to source,
and "dest" set to dest.
"""

def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
        }
    print(config)
    Site(**config).build()


typer.run(main)
