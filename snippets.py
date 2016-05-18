# Tyler Hedegard 5/17/2016
# Thinkful.com Python Introduction Unit 2 Lesson 1
# Snippets Assignment

import logging

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    """
    Store a snippet with an associated name.

    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'.

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
def remove(name):
    """
    Remove a snippet with a given name
    If there is no such snippet, return '404: Snippet Not Found'.
    """
    logging.error("FIXME: Unimplemented - remove({!r}".format(name))
    return ""
    
def update(name,snippet):
    """
    Find and update a named snippet
    If there is no such snippet, put the snippet.
    Return the snippet
    """
    logging.error("FIXME: Unimplemented - update({!r},{!r}".format(name,snippet))
    return name, snippet