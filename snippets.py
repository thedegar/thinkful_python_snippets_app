# Tyler Hedegard 5/17/2016
# Thinkful.com Python Introduction Unit 2 Lesson 1
# Snippets Assignment

import logging
import argparse
import psycopg2

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

# Connect to DB
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")

def put(name, snippet):
    """
    Store a snippet with an associated name.
    Returns the name and the snippet
    """
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    with connection, connection.cursor() as cursor:
        try:
            command = "insert into snippets values (%s, %s)"
            cursor.execute(command, (name, snippet))
        except psycopg2.IntegrityError as e:
            connection.rollback()
            command = "update snippets set message=%s where keyword=%s"
            cursor.execute(command, (snippet, name))
    logging.debug("Snippet stored successfully.")
    return name, snippet
    
def get(name):
    """
    Retrieve the snippet with a given name.
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet.
    """
    logging.info("Retrieving snippet {!r}".format(name))
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        result = cursor.fetchone()
    if not result:
        # No snippet was found with that name.
        logging.info("Snippet not found")
        return "404: Snippet Not Found"
    logging.debug("Snippet retrieved successfully.")
    return result[0]
    
def catalog():
    """
    Returns a list of keywords in the DB
    """
    logging.info("Retrieving keywords from DB")
    with connection, connection.cursor() as cursor:
        cursor.execute("select keyword from snippets order by keyword")
        result = cursor.fetchall()
    if not result:
        # No keywords found in the
        logging.info("No keywords found")
        return "404: No Keywords Found"
    logging.debug("Keywords retrieved successfully")
    return result

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
    
    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="Name of the snippet")
    
    # Subparser for the catalog command
    logging.debug("Constructing catalog subparser")
    catalog_parser = subparsers.add_parser("catalog", help="Retrieve all keywords")

    arguments = parser.parse_args()
    
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
    elif command == "catalog":
        result = catalog(**arguments)
        print("Keywords: ")
        for i in result:
            print(i[0])

if __name__ == "__main__":
    main()