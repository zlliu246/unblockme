from .state_utils import (
    create_state, 
    animate_states
)
from .djikstra_utils import dijkstra_search

def unblockme(
    state: str,
    animate: bool =True
) -> list[tuple[str]]:
    """
    Args:
        state_raw (str): a string representing a puzzle eg.

            state = '''
            AAAB  
            CDDBEE
            CXXB F
            C GHHF
            G IF
            JJJ I
            '''

        animate (bool): if True, the solution will be animated

    Returns:
        list of states representing solution

    """
    state = create_state(state)
    states = dijkstra_search(state)
    if animate:
        animate_states(states)
    return states

__all__ = ['unblockme']