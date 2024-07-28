import re
from unprint import unprint

EXAMPLE = '''
AAAB  
CDDBEE
CXXB F
C GHHF
  G IF
JJJ I
'''

def create_state(raw_string: str):
    state = raw_string.split('\n')
    state = tuple([row.ljust(6) for row in state if row.strip()])
    lengths = list(set(map(len, state)))
    if len(state) != 6 or lengths != [6]:
        raise Exception(f'''invalid state. state should be something like: {EXAMPLE}''')
    return state

def display_state(state: tuple[str]):
    for line in state:
        print(line)
    print()

def get_next_states(state: tuple[str]):
    def get_next_states_horizontal(state: tuple[str]):
        def get_one_line_options(line: str):
            d = {}
            for c in line:
                if c not in d: d[c] = 0
                d[c] += 1
            out = set([line])
            for k,count in d.items():
                if k == ' ' or count < 2: continue                
                match = re.search(' *' + k +  '{2,3} *', line)
                start, end = match.span()
                chunk = line[start: end]
                block = chunk.replace(' ', '')
                for i in range(1, end-start):
                    chunk = chunk[1:] + chunk[0]
                    new_line = line[:start] + chunk + line[end:]
                    if block in new_line:
                        out.add(line[:start] + chunk + line[end:])
            out.remove(line)
            return out

        out = set([state])
        for i,line in enumerate(state):
            for new_line in get_one_line_options(line):
                new_state = state[:i] + (new_line,) + state[i+1:]
                out.add(new_state)
        out.remove(state)
        return out
            
    def transpose(state):
        out = ()
        for i in range(6):
            line = ''
            for j in range(6):
                line += state[j][i]
            out += (line,)
        return out

    next_states = list(get_next_states_horizontal(state))

    state_transposed = transpose(state)
    next_transposed = get_next_states_horizontal(state_transposed)
    
    next_states.extend([transpose(s) for s in next_transposed])

    return next_states

def animate_states(states):
    for state in states:
        unprint(8)
        display_state(state)
        input('>>>')