import json 


"""
Functions:

add_asset
list_asset - prints assets in readable format
save_asset
save_to_json
load_from_json
find_asset
remove_asset

"""

def add_asset(
    asset_id: int,
    name: str,
    category: str,
    size: str,
    file_path: str
    #Convert it into dictionary
) -> dict:
    asset = {
        "id": asset_id,
        "name": name,
        "category": category,
        "size": size,
        "file_path": file_path
    }

    return asset

"""Create and return a new asset dictionary."""

# TODO: Understand why the type annotation is written as list[dict].
assets: list[dict] = []

def list_assets(assets: list[dict]) -> None:
    for asset in assets:
        print(
            f"{asset['id']}: "
            f"{asset['name']} - "
            f"{asset['size']} - "
            f"{asset['category']}"
        )

"""Print all assets in a readable format."""
# TODO Review whether list_assets() should remain separate from the (Command-Line Interface)CLI.

def save_asset(
    assets: list[dict],
    asset: dict
) -> None:
    assets.append(asset)

"""Add an asset to the current asset collection."""

# Save to json file
def save_to_json(assets: list[dict]) -> None:
    with open("assets.json", "w", encoding="utf-8") as file:
        json.dump(assets, file, indent=4)
        print("Assets saved to file.")

def load_from_json(
    file_path: str = "assets.json"
) -> list[dict]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
#search for asset
def find_asset(
    assets: list[dict],
    name: str
) -> dict | None:
    for asset in assets:
        if asset["name"].lower() == name.lower():
            return asset

    return None

def remove_asset(
    assets: list[dict],
    asset_id: int
) -> bool:
    for asset in assets:
        if asset["id"] == asset_id:
            assets.remove(asset)
            print(f"Asset {asset["id"]} removed.")
            return True

    return False

# TODO - continue edit_asset, fix numbers id
def edit_asset(
    assets: list[dict],
    asset_id: int,
    asset_name: str
) -> bool:
    for asset in assets:
        if asset["id"] == asset_id:
            asset["name"] = asset_name
            print(f"Asset {asset["id"]} changed.")
            save_to_json(assets)
            return True

    return False

#Custom input
if __name__ == "__main__":
    assets = [
        {"id": 1, "name": "tree",  "category": "nature" , "size": "16x16", "file_path":"assets/tree.png" },
        {"id": 2, "name": "sword", "category": "weapons" , "size": "16x16", "file_path":"assets/sword.png" },
    ]

"""Testing commands"""

# Adding 1st asset
hero = add_asset(
    1, "hero", "character", "16x16","assets/hero.png"
)
assets.append(hero)

# Adding 2nd asset - add_asset
tree = add_asset(
    2, "tree", "nature",  "16x16", "assets/tree.png"
)
assets.append(tree)

# Adding 3rd asset - add_asset
potion = add_asset(
    3, "potion", "item", "16x16", "assets/potion.png"
)
assets.append(potion)

# Saving 4th asset - save_asset
bookshelf = add_asset(
    4, "bookshelf", "furniture", "32x32", "assets/bookshelf.png"
)
save_asset(assets, bookshelf)

# Saving 5th asset - save_asset
grass_block = add_asset(
    5, "grass_block", "nature", "32x32", "assets/grass_block.png"
)
save_asset(assets, grass_block)

dirt_block = add_asset(
    6, "dirt_block", "nature", "32x32", "assets/dirt_block.png"
)
save_asset(assets, dirt_block)

#Testing remove_asset
removed = remove_asset(assets, 2)

#TODO - add value that is deleted
if removed:
    print(f"Asset {removed} removed.")
    save_to_json(assets)
elif removed is None:
    print(f"Asset {removed} is None.")
else:
    print(f"Asset {removed} not found.")

save_to_json(assets)

edit_asset(assets, 6, "rock")

# Testing find_asset - The search is case-insensitive, so hero, Hero, and HERO match.
result = find_asset(assets, "hero")
result = find_asset(assets, "stone")

if result is not None:
    print(f"Found asset: {result}")
else:
    print("Asset not found.")

assets = load_from_json()

print("Current assets:")

list_assets(assets)




