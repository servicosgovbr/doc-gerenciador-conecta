# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# Project name
project = u'Gerenciador de APIs do Conecta'
copyright = u'2024, gov.br conecta'
author = u'gov.br'

# The short X.Y version
version = u''

# The full version, including alpha/beta/rc tags
release = u''

# -- General configuration ---------------------------------------------------

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = u'pt_BR'

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.imgconverter',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks'
]

# Show copyright
html_show_copyright = False

# Make sure the target is unique
autosectionlabel_prefix_document = True

# Enable numref
numfig = True


# Show "Created using Sphinx"
html_show_sphinx = False

# Show links to the reST sources will be added to the sidebar
html_show_sourcelink = False

# Language to be used for generating the HTML full-text search index.
html_search_language = u'pt'

# Favicon
html_favicon = u'http://www.gov.br/governodigital/++theme++padrao_govbr/favicons/favicon-32x32.png'

html_logo = u'_imagens/logo_conecta.png'

# html_theme = "sphinx_rtd_theme"

# html_theme_options = {
#    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
#    'analytics_anonymize_ip': False,
#    'logo_only': False,
#    'display_version': False,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'vcs_pageview_mode': '',
#    'style_nav_header_background': 'white'

    # Toc options
#    'collapse_navigation': True,
#    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
#    'titles_only': False
#}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DocGerenciadorConecta'


