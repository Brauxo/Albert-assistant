import pytest
from unittest.mock import MagicMock, patch
from src.utils import Utils
from src.config import COLLECTION_NAME
import pymongo
from bson import ObjectId
import sys
import os

@pytest.fixture
def mock_mongo_client():
    """Creates a mock MongoDB client."""
    mock_client = MagicMock()
    mock_db = MagicMock()
    mock_client.__getitem__.return_value = mock_db
    return mock_client

@patch("src.utils.pymongo.MongoClient")
def test_get_db_connection(mock_client, mock_mongo_client):
    """Tests database connection."""
    mock_client.return_value = mock_mongo_client  # Use the fixture properly
    db = Utils.get_db_connection()
    
    assert db is not None
    mock_client.assert_called_once_with("mongodb://localhost:27017/")

@pytest.fixture
def mock_ollama_client():
    """Creates a mock Ollama client."""
    mock_client = MagicMock()
    mock_client.chat.return_value = {"message": {"content": "Réponse IA"}}
    return mock_client

@patch("src.utils.pymongo.MongoClient")
def test_get_all_courses(mock_mongo_client):
    """Tests retrieving all courses."""
    mock_db = mock_mongo_client.return_value["test_db"]
    mock_db[COLLECTION_NAME].find.return_value = [{"title": "Python", "category": "Informatique", "content": "Cours sur Python"}]

    courses = Utils.get_all_courses()
    
    assert len(courses) == 1
    assert courses[0]["title"] == "Python"