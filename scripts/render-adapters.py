#!/usr/bin/env python3
import sys

from manage import main

if __name__ == "__main__":
    sys.argv = [sys.argv[0], "render-adapters"]
    main()
