# Define the correct mapping between items and categories
MAPPING = {
    "धान": "अन्नबाली समूह",
    "कालिज": "पन्छी समूह",
    "घोडा": "जनावर समूह",
    "आलु": "तरकारी समूह",
    "केला": "फलफूल समूह"
}

def validate_item_category(item, category):
    """
    Validate if the given item belongs to the correct category.
    :param item: The item being validated.
    :param category: The category to validate against.
    :return: True if valid, False otherwise.
    """
    return MAPPING.get(item) == category
