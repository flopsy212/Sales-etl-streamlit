def normalize_store_name(name):
    return name.strip().replace("支店", "Store").replace("Tokyo A", "Store A")

def normalize_item_name(name):
    name = name.lower().replace("Ｔシャツ", "t-shirt").replace("tshirt", "t-shirt")
    return name.strip()

def normalize_category(cat):
    mapping = {
        "トップス": "Tops",
        "ボトムス": "Bottoms",
        "tops": "Tops",
        "bottoms": "Bottoms"
    }
    return mapping.get(cat.strip().lower(), cat)

def clean_price(price):
    return int(str(price).replace("¥", "").replace(",", "").strip())
