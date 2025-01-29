from flask import jsonify, request
from app import app
from app.services.validation import validate_item_category

# Mock data for both languages
ITEMS = {
   "en": [
        "Rice", "Horse", "Potato", "Banana", "Goat", "Tiger", "Lion", "Cow", 
        "Sparrow", "Pigeon", "Himalayan Monal", "Millet", "Wheat", "Buckwheat", 
        "Greens", "Brinjal", "Pumpkin", "Apple", "Mango", "Papaya"
    ],
    "ne": [
        "धान", "घोडा", "आलु", "केरा", "बाख्रा", "बाघ", "सिंह", "गाई", 
        "भँगेरा", "परेवा", "डाँफे", "कोदो", "गहुँ", "फापर", 
        "साग", "भिण्डी", "फर्सी", "स्याउ", "आँप", "मेवा"
    ]
}

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


# API to fetch items and categories
@app.route('/api/dataList', methods=['GET'])
def get_data():
    language = request.args.get("language", "en")  # Default to English
    if language not in ITEMS or language not in CATEGORIES:
        return jsonify({"error": "Invalid language"}), 400

    return jsonify({
        "items": ITEMS[language],
        "categories": CATEGORIES[language]
    })

# API to validate item-category mapping
@app.route('/api/validate', methods=['POST'])
def validate():
    data = request.json
    item = data.get("item")
    category = data.get("category")
    language = data.get("language", "en")  # Default to English

    if not item or not category or language not in ITEMS:
        return jsonify({"valid": False, "message": "Invalid data"}), 400

    is_valid = validate_item_category(item, category, language)
    return jsonify({"valid": is_valid})
