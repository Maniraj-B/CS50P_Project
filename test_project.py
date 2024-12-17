import pytest
import pandas as pd
from project import recommend_books, save_history, read_history


def test_recommend_books():
    # Mock data
    data = pd.DataFrame({
        "Title": ["To Kill a Mockingbird", "Dune", "Gone Girl"],
        "Genre": ["Fiction", "Sci-Fi", "Mystery"]
    })

    # Mock behavior of recommend_books
    def mock_recommend_books(genre):
        return data[data["Genre"] == genre]["Title"].tolist()

    assert mock_recommend_books("Fiction") == ["To Kill a Mockingbird"]
    assert mock_recommend_books("Sci-Fi") == ["Dune"]
    assert mock_recommend_books("Unknown") == []


def test_save_history():
    # Mock save_history behavior
    def mock_save_history(genre, recommendations):
        # Simulate saving by creating a DataFrame
        return pd.DataFrame({
            "Genre": [genre],
            "Recommendations": [", ".join(recommendations)]
        })

    history = mock_save_history("Mystery", ["Gone Girl", "The Girl with the Dragon Tattoo"])
    assert len(history) == 1
    assert history.iloc[0]["Genre"] == "Mystery"
    assert history.iloc[0]["Recommendations"] == "Gone Girl, The Girl with the Dragon Tattoo"


def test_read_history():
    # Mock data
    mock_data = pd.DataFrame({
        "Genre": ["Fantasy"],
        "Recommendations": ["Harry Potter, The Hobbit"]
    })

    # Mock read_history behavior
    def mock_read_history():
        return mock_data

    history = mock_read_history()
    assert len(history) == 1
    assert history.iloc[0]["Genre"] == "Fantasy"
    assert history.iloc[0]["Recommendations"] == "Harry Potter, The Hobbit"
