import pandas as pd


def main():
    print("Welcome to the Enhanced Book Recommendation System!")
    while True:
        genre = input("Enter your favorite genre (e.g., Fiction, Mystery, Sci-Fi) or 'history' to view past searches: ").strip()
        
        if genre.lower() == "history":
            display_history()
            continue
        
        if not genre:
            print("Please enter a valid genre.")
            continue
        
        recommendations = recommend_books(genre)
        if recommendations:
            print("Here are some books you might enjoy:")
            for book in recommendations:
                print(f"- {book}")
        else:
            print(f"Sorry, no recommendations available for '{genre}'. Please try another genre.")
        
        save_history(genre, recommendations)
        again = input("Would you like another recommendation? (yes/no): ").strip().lower()
        if again != "yes":
            break
    print("Thank you for using the Enhanced Book Recommendation System!")


def recommend_books(genre):
    """Return a list of book recommendations based on the genre using a pandas DataFrame."""
    try:
        books = pd.read_csv("books.csv")
        filtered_books = books[books["Genre"].str.contains(genre, case=False, na=False)]
        return filtered_books["Title"].tolist()
    except FileNotFoundError:
        print("Error: Book database (books.csv) not found.")
        return []


def save_history(genre, recommendations):
    """Save user genre input and recommendations to a history file using pandas."""
    history_data = pd.DataFrame({
        "Genre": [genre],
        "Recommendations": [", ".join(recommendations) if recommendations else "None"]
    })
    try:
        # Append to existing history file
        history_data.to_csv("history.csv", mode="a", header=not pd.io.common.file_exists("history.csv"), index=False)
    except Exception as e:
        print(f"Error saving history: {e}")


def read_history():
    """Read and return the history of user inputs and recommendations."""
    try:
        return pd.read_csv("history.csv")
    except FileNotFoundError:
        print("No history found.")
        return pd.DataFrame()


def display_history():
    """Display the history of user inputs and recommendations."""
    history = read_history()
    if history.empty:
        print("No history to display.")
    else:
        print("Your past searches and recommendations:")
        print(history)


if __name__ == "__main__":
    main()
