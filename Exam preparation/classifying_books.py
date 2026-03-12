def classify_books(*args, **kwargs):
    fiction_books = []
    non_fiction_books = []

    genre = args[0]
    title = args[1]
    for isbn, book_title in kwargs.items():
        if title == book_title:
            if genre == "fiction":
                fiction_books.append((isbn, title))
            elif genre == "non-fiction":
                non_fiction_books.append((isbn, title))
    
    fiction_sorted = sorted(fiction_books, key=lambda x: x[0])
    non_fiction_sorted = sorted(non_fiction_books, key=lambda x: x[0], reverse = True)

    result = []

    if fiction_sorted:
        result.append("Fiction Books:")
        for isbn, book_title in fiction_books:
            result.append(f"~~~{isbn}#{book_title}")

    if non_fiction_sorted:
        result.append("Non-Fiction Books:")
        for isbn, book_title in fiction_books:
            result.append(f"***{isbn}#{book_title}")

    return "\n".join(result)

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
