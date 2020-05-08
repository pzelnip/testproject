#!/usr/bin/env python3
import os
from jinja2 import Template


def main():
    filename = os.path.join(os.path.dirname(__file__), "hello.jinja2")
    template = Template(open(filename).read())
    print(template.render(message="fldskfjasdlfkadjs"))

    print("hello world")


if __name__ == "__main__":
    exit(main())
