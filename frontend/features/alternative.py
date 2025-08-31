# features/alternative.py

from datasets.alt_dataset import get_dataset_alt
ALTERNATIVE_KNOWLEDGE_BASE = get_dataset_alt()


def find_alternatives(medication_name: str) -> dict | None:
    """
    Looks up a medication in the knowledge base and returns alternatives.
    The keys are matched case-insensitively.
    """
    # Find a matching key in the knowledge base, ignoring case
    for key in ALTERNATIVE_KNOWLEDGE_BASE:
        if key in medication_name.lower():
            return ALTERNATIVE_KNOWLEDGE_BASE[key]
    # Return None if no match is found
    return None
