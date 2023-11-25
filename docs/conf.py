# Configuration file for the Sphinx documentation builder.
#
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'System Level, Analog Devices'
copyright = '2023, Analog Devices Inc'
author = 'Analog Devices Inc'
release = 'v0.1'

# -- General configuration ---------------------------------------------------

import os, sys

user = os.environ.get("USER")
sys.path.append(os.path.abspath("./extensions"))

extensions = [
	"sphinx.ext.todo",
	"sphinx.ext.intersphinx",
	"adi_basic",
	"adi_links"
]

templates_path = ['sources/template']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- External docs configuration ----------------------------------------------

intersphinx_mapping = { 'hdl'  : ('https://analogdevicesinc.github.io/hdl',   None),
						'no-os': ('https://analogdevicesinc.github.io/no-os', None)}

intersphinx_disabled_reftypes = ["*"]

# -- Custom extensions configuration ------------------------------------------

hide_collapsible_content = True
validate_links = False

# -- todo configuration -------------------------------------------------------

todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output --------------------------------------------------

html_theme = 'furo'
html_static_path = ['sources']
source_suffix = '.rst'
html_css_files = ["custom.css"]
html_favicon = "sources/icon.svg"
