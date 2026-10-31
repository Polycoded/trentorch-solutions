def filter_quality(examples: list[str], min_length: int, banned_phrases: list[str]) -> list[str]:
    """Keep only examples that are at least `min_length` characters long AND
    contain none of `banned_phrases` (case-insensitive substring match).
    Return the kept examples in their original order.
    """
    # TODO: implement
    if isinstance(banned_phrases, str):
        banned_phrases = [banned_phrases]
        
    banned_lower = [phrase.lower() for phrase in banned_phrases]
    return[
        ex for ex in examples
        if(len(ex)>=min_length and not any(phrase in ex.lower() for phrase in banned_lower) )
    ]
