def simulate_self_play(
    agent_a_moves: list[str], agent_b_moves: list[str], max_turns: int
) -> list[tuple[str, str]]:
    """Simulate two agents, "A" and "B", alternating turns starting with A.
    `agent_a_moves` and `agent_b_moves` are each agent's pre-scripted moves,
    used in order as that agent gets its turns. Build a transcript of
    (agent_name, move) pairs, one per turn, for up to `max_turns` turns --
    but stop early the moment the agent whose turn it is has no more moves
    left to use.
    """
    # TODO: implement
    t=[]
    idx_a=0
    idx_b=0

    for turn in range(max_turns):
        if turn%2==0:
            if(idx_a>=len(agent_a_moves)):
                break
            t.append(("A",agent_a_moves[idx_a]))
            idx_a+=1
        else:
            if(idx_b>=len(agent_b_moves)):
                break
            t.append(("B",agent_b_moves[idx_b]))
            idx_b+=1

    return t
