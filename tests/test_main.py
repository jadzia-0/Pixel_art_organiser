import json 
from main import add_asset
from main import find_asset
from main import remove_asset
from main import load_from_json
from main import edit_asset

# python -m pytest

def test_add_asset():
    asset = add_asset(
        1, "hero", "character", "16x16", "assets/hero.png"
    )

    assert asset["id"] == 1
    assert asset["name"] == "hero"
    assert asset["category"] == "character"
    assert asset["size"] == "16x16"
    assert asset["file_path"] == "assets/hero.png"

def test_find_asset():
    assets = [
        {
            "id": 1,
            "name": "hero",
            "category": "character",
            "size": "16x16",
            "file_path": "assets/hero.png"
        },
        {
            "id": 2,
            "name": "tree",
            "category": "nature",
            "size": "16x16",
            "file_path": "assets/tree.png"
        }
    ]

    result = find_asset(assets, "hero")

    assert result is not None
    assert result["name"] == "hero"

def test_find_missing_asset():
    assets = [{"id": 1, "name": "hero"}]

    result = find_asset(assets, "dragon")

    assert result is None

def test_remove_asset():
    assets = [{"id": 2, "name": "tree"}]

    removed = remove_asset(assets, 2)
    assert removed is True
    assert assets == []
  
def test_remove_missing_asset():
    assets = [{"id": 2, "name": "tree"}]

    removed = remove_asset(assets, 99)

    assert removed is False
    assert len(assets) == 1

def test_load_from_json(tmp_path):
    test_file = tmp_path / "assets.json"
    expected_assets = [{"id": 1, "name": "hero"}]

    test_file.write_text(
        json.dumps(expected_assets),
        encoding="utf-8"
    )

    assets = load_from_json(str(test_file))

    assert assets == expected_assets
    
def test_edit_asset():
    assets = [{"id": 1, "name": "tree"}]

    result = edit_asset(assets, 1, "rock")

    assert result is True
    assert assets[0]["id"] == 1
    assert assets[0]["name"] == "rock"