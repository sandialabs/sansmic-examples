# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
import glob

try:
    import sansmic
    version = os.environ.get("SANSMIC_SPHINX_VERSION", sansmic.__version__)
except ImportError:
    doxygen_installed = False

extensions = []

##############################################################################
#    Sphinx core options                                                     #
##############################################################################

# -- Project information -----------------------------------------------------
project = "sansmic"
copyright = "2024 National Technology and Engineering Solutions of Sandia, LLC. Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software."
author = "See AUTHORS.md"

if version.startswith('v'):
    version = version[1:]
    release = 'v' + version
else:
    release = version

ga_token = os.environ.get("GOOGLE_ANALYTICS_TOKEN", "G-23TNKN36XM")

extensions.extend(
    [
        "sphinx.ext.autodoc",
        "sphinx.ext.doctest",
        "sphinx.ext.todo",
        "sphinx.ext.coverage",
        "sphinx.ext.mathjax",
        "sphinx.ext.viewcode",
        "sphinx.ext.autosummary",
        "sphinx.ext.napoleon",
        "sphinx.ext.intersphinx",
        "sphinx.ext.githubpages",
        "sphinx_design",
        "sphinx_click" if not version.startswith("1.0.0") else "sphinxarg.ext",
        "sphinxcontrib.bibtex",
        "nbsphinx",
    ]
)


# -- Callout numbering -------------------------------------------------------
numfig = True
numfig_format = {"figure": "Figure %s", "table": "Table %s", "code-block": "Listing %s"}


# -- Internationalization ----------------------------------------------------
language = "en"


# -- Markup options ----------------------------------------------------------


# -- Options for Maths -------------------------------------------------------


# -- Options for object signatures
add_function_parentheses = True
toc_object_entries = True
toc_object_entries_show_parents = "hide"


# -- Options for source files ------------------------------------------------

# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "doxygen"]

# The master toctree document.
master_doc = "index"

# source_suffix = ['.rst', '.md']
source_suffix = {".rst": "restructuredtext"}


# -- Options for templating --------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


##############################################################################
#    Sphinx domain options                                                   #
##############################################################################

# -- Options for the Python domain -------------------------------------------
add_module_names = False
python_display_short_literal_types = True
python_use_unqualified_type_names = True


##############################################################################
#    Sphinx extension options                                                #
##############################################################################

# -- sphinx-bibtex (references) ----------------------------------------------
bibtex_bibfiles = ["references.bib"]
bibtex_default_style = "plain"
bibtex_reference_style = "label"


# -- Docstring parsing (napoleon)---------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = True
napoleon_preprocess_types = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = False


# -- Autodoc & autosummary ---------------------------------------------------
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": False,
    "special-members": "__call__",  #', __enter__, __iter__, __next__',
    "inherited-members": False,
    "show-inheritance": False,
    "member-order": "groupwise",
}
autodoc_typehints = "description"
autodoc_typehints_format = "short"
autodoc_typehints_description_target = "documented"
autodoc_type_aliases = {
    "DataFrame": "pandas.DataFrame",
}
autoclass_content = "both"
autosummary_generate = glob.glob("*.rst")
autosummary_generate_overwrite = True


##############################################################################
#    Builder options                                                         #
##############################################################################
# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_title = "Sansmic Examples"
html_js_files = [
    "pypi-icon.js",
]
# html_sidebars = {"nomenclature": []}
html_theme_options = {
    "icon_links": [
        {
            "name": "Issues",
            "url": "https://github.com/sandialabs/sansmic/issues",
            "type": "fontawesome",
            "icon": "fa-regular fa-circle-dot",
        },
        {
            "name": "GitHub",  # Label for this link
            "url": "https://github.com/sandialabs/sansmic",  # required URL where the link will redirect
            "type": "fontawesome",  # The type of image to be used
            "icon": "fa-brands fa-github",  # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
        },
        {
            "name": "PyPI",  # Label for this link
            "url": "https://pypi.org/project/sansmic/",  # required URL where the link will redirect
            "type": "fontawesome",  # The type of image to be used
            "icon": "fa-custom fa-pypi",  # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
        },
        {
            "name": "Sandia National Laboratories",
            "url": "https://www.sandia.gov",  # required
            "type": "local",
            "icon": "_static/snl_logo.png",
        },
    ],
    "navigation_with_keys": False,
    "use_edit_page_button": False,
    "primary_sidebar_end": ["indices.html"],
    "show_toc_level": 2,
    "navbar_start": [
        "navbar-logo",
    ],
    "navbar_end": [
        "theme-switcher",
        "navbar-icon-links",
    ],
    "analytics": {"google_analytics_id": ga_token},
}
