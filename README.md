# sphinx-sandbox-code-and-docs

## About
All-in-one repository framework hosting an integrated codebase and Sphinx tree.

## Overview
This repository serves as a live, interactive reference demonstrating a unified monorepo architecture. Instead of isolating software and documentation in separate repositories, this framework houses both components under a single roof to enable atomic commits and simplify CI pipelines.

## Internal Directory Structure

```text
sphinx-sandbox-code-and-docs/         # Combined repository (unified monorepo).
    ├── .github/
    │   └── workflows/
    │       └── ci.yml                # Flat internal CI pipeline.
    ├── codebase/
    │   └── example.py                # Example Python module with reST docstrings.
    └── docs/
        ├── conf.py                   # Sphinx path configuration matrix.
        └── index.rst                 # Documentation index layout file.
```
## Features
* **Atomic Continuous Integration:** Every single commit is automatically validated by an internal GitHub Actions runner that tests the code syntax and docstring compilation simultaneously.
* **Cross-Domain Atomic Commits:** Enables simultaneous tracking of source code adjustments and document updates under a single Git hash, preventing out-of-sync states.
* **Native Path Resolution:** The configuration uses simple relative parent look-ups to discover the application modules natively without complex path environmental requirements.

---

*Feel free to explore the files and adapt this framework to your project.*
