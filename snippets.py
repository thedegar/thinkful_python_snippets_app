# Tyler Hedegard 5/17/2016
# Thinkful.com Python Introduction Unit 2 Lesson 1
# Snippets Assignment

import logging
import argparse

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
    """
    Retrieve the snippet with a given name.
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
    
def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")

    arguments = parser.parse_args()

if __name__ == "__main__":
    main()