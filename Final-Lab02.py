def moore_machine(input_str):
    transitions = {
        'A_A': {'0': 'A_A', '1': 'B_B'},
        'B_B': {'0': 'C_A', '1': 'D_B'},
        'C_A': {'0': 'D_C', '1': 'B_B'},
        'C_C': {'0': 'D_C', '1': 'B_B'},
        'D_B': {'0': 'B_B', '1': 'C_C'},
        'D_C': {'0': 'B_B', '1': 'C_C'},
        'E_C': {'0': 'D_C', '1': 'E_C'}
    }
    
    outputs = {
        'A_A': 'A',
        'B_B': 'B',
        'C_A': 'A',
        'C_C': 'C',
        'D_B': 'B',
        'D_C': 'C',
        'E_C': 'C'
    }
    
    current_state = 'A_A'
    output_str = ''
    
    for symbol in input_str:
        current_state = transitions[current_state][symbol]
        output_str += outputs[current_state]
    
    return output_str

# Process the given inputs
inputs = ['00110', '11001', '1010110', '101111']
for inp in inputs:
    output = moore_machine(inp)
    print(f"Input: {inp} -> Output: {output}")
