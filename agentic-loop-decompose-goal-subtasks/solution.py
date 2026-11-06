def order_subtasks(subtasks: list[str], dependencies: list[tuple[str, str]]) -> list[str]:
    """
    subtasks: every sub-task's name.
    dependencies: (before, after) pairs -- "before" must be scheduled
    strictly earlier than "after". Guaranteed acyclic.

    Produce a valid execution order respecting every dependency. When
    more than one sub-task is available to schedule next, prefer
    whichever comes FIRST in the original `subtasks` list.

    Returns the full ordered list of sub-task names.
    """
    # TODO: Implement the dependency-respecting order from Theory.
    result=[]

    graph={task:[] for task in subtasks}
    indegree={task:0 for task in subtasks}

    for before, after in dependencies:
        graph[before].append(after)
        indegree[after]+=1

    while len(result)<len(subtasks):

        for task in subtasks:
            if indegree[task]==0 and task not in result:

                result.append(task)

                for next_task in graph[task]:
                    indegree[next_task]-=1
                break
    return result
