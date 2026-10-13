#!/usr/bin/env python3

import os
import sys
import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# fetch credentials from environment variables
MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():
    """
    Connects to the MongoDB Atlas bookstore DB, queries a specific 
    list of authors, and prints a report of their books.
    """
    client = None
    try:
        # connection to MongoDB Atlas
        client = MongoClient(
            MONGODB_ATLAS_URL,
            username=MONGODB_ATLAS_USER,
            password=MONGODB_ATLAS_PWD
        )

        # access the bookstore database and collections
        db = client.bookstore
        authors_col = db.authors
        books_col = db.books

        # list of _ids to query
        author_id_list = ["author_003", "author_004"]

        # print the total number of authors
        print(f"\nAuthors: {len(author_id_list)}\n")

        # retrieve and print each author and their associated books
        for a_id in author_id_list:
            # fetch the author document
            author = authors_col.find_one({"_id": a_id})

            if author:
                print(author.get("name", "Unknown Author"))
                # fetch all books that include this author's _id in their author_ids array
                books = books_col.find({"author_ids": a_id})
                # print the book details indented under the author
                for book in books:
                    title = book.get("title", "Unknown Title")
                    year = book.get("published_year", "Unknown Year")
                    print(f"  {title} ({year})")

                print()

    except (ConnectionFailure, OperationFailure) as e:
        logging.error(f"Database connection or operation failed: {e}")
    finally:
        # verify the client connection is closed
        if client:
            client.close()
            logging.info("MongoDB connection closed.")

if __name__ == "__main__":
    main()
