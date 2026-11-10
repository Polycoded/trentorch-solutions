def route_handoff(current_agent: str, message: str, routing_rules: list[tuple[str, str]]) -> str:
    """
    current_agent: who's currently handling this conversation.
    message: the latest message text.
    routing_rules: ordered (keyword, target_agent) pairs -- checked in
    order, case-insensitive substring match.

    Return the target_agent of the FIRST routing rule whose keyword
    appears anywhere in message. If no rule matches, stay with
    current_agent (no handoff).
    """
    # TODO: Implement the keyword-based handoff from Theory.
    for rr in routing_rules:
        keyword,target_agent=rr
        if keyword.lower() in message.lower():
            return target_agent
    return current_agent
