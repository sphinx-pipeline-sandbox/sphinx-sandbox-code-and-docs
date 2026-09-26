import os
import sys

# Inject the parent directory into Python's active system path-matrix
# with '..' telling Python to step up into the repository root:
sys.path.insert(0, os.path.abspath('..'))

# --- Your standard Sphinx configurations continue below ---
project = 'Sphinx Sandbox: Code and Docs'
copyright = '2026, Elliria'
author = 'Elliria'

extensions = [
    'sphinx.ext.autodoc',  # The engine that executes the code to grab docstrings
    'sphinx.ext.viewcode', # Adds handy "[source]" links to your compiled site
]

html_theme = 'sphinx_rtd_theme'
