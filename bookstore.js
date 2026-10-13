// Step 2:
// use bookstore
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
db.authors.find()
db.books.find()

// Step 6: insert two new books
db.books.insertMany([
  {
    title: "The Circle",
    published_year: 2013,
    author_ids: ["author_004"]
  },
  {
    title: "Frankenstein",
    published_year: 1818,
    author_ids: ["author_005"]
  }
]);

// Step 7: add missing authors
db.authors.insertMany([
  {
    _id: "author_004",
    name: "Dave Eggers",
    nationality: "American",
    bio: {
      short: "American writer and publisher.",
      long: "Dave Eggers is an American writer and publisher. His 2000 memoir, A Heartbreaking Work of Staggering Genius, became a bestseller and was a finalist for the Pulitzer Prize for General Nonfiction."
    }
  },
  {
    _id: "author_005",
    name: "Mary Shelley",
    nationality: "English",
    bio: {
      short: "English novelist.",
      long: "Mary Shelley was an English novelist who wrote the Gothic novel Frankenstein; or, The Modern Prometheus."
    }
  }
]);

// Step 8: filter books by a list of authors
db.books.find({ author_ids: { $in: ["author_001", "author_004"] } })
