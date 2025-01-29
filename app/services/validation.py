def validate_item_category(item, category, language):
    # Dynamically validate item against category based on CATEGORIES data
    CATEGORIES = {
        "en": [
            {"name": "Animals", "label": "Animals", "items": ["Goat", "Horse", "Tiger", "Lion", "Cow"]},
            {"name": "Birds", "label": "Birds", "items": ["Sparrow", "Pigeon", "Himalayan Monal"]},
            {"name": "Crops", "label": "Crops", "items": ["Millet", "Rice", "Wheat", "Buckwheat"]},
            {"name": "Vegetables", "label": "Vegetables", "items": ["Greens", "Potato", "Brinjal", "Pumpkin"]},
            {"name": "Fruits", "label": "Fruits", "items": ["Banana", "Apple", "Mango", "Papaya"]},
        ],
        "ne": [
            {"name": "जनावर समूह", "label": "जनावर समूह", "items": ["बाख्रा", "घोडा", "बाघ", "सिंह", "गाई"]},
            {"name": "पन्छी समूह", "label": "पन्छी समूह", "items": ["भँगेरा", "परेवा", "डाँफे"]},
            {"name": "अन्नबाली समूह", "label": "अन्नबाली समूह", "items": ["कोदो", "धान", "गहुँ", "फापर"]},
            {"name": "तरकारी समूह", "label": "तरकारी समूह", "items": ["साग", "आलु", "भिण्डी", "फर्सी"]},
            {"name": "फलफूल समूह", "label": "फलफूल समूह", "items": ["केरा", "स्याउ", "आँप", "मेवा"]},
        ]
    }

    # Check if the language exists in the CATEGORIES data
    if language not in CATEGORIES:
        return False

    # Get the list of categories for the language
    categories = CATEGORIES[language]

    # Find the matching category by name
    for cat in categories:
        if cat["name"] == category:
            # Check if the item exists in the category's items
            return item in cat["items"]

    # If no matching category is found, return False
    return False
