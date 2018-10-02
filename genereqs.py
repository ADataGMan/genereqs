#!/usr/bin/env python3
def generate_requirements(globals):
    from pip._internal.operations import freeze
    import sys
    import os
    l1 = list(set(sys.modules) & set(globals))

    r = list(freeze.freeze())
    d1 = dict()
    for p in r:
        j = p.split("=")[0].lower()
        d1[j] = p

    g = list(d1[k] for k in (l1 & d1.keys()))

    with open('requirements.txt', 'w') as f:
        for rw in g:
            f.write(f"{rw}\n")
        f.truncate(f.tell() - len(os.linesep))