import  networkx as nx
import numpy as np

class SpikingMachine:
    def __init__(self):
        self.insts = 0
        self.G = nx.DiGraph()
        self.Gs = nx.DiGraph()
        self.node_types = {}
    def add(self, V, inst_name = 'add'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=-1.)
        self.G.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'add'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.nodes()['V_'+str(V)]['label'] = inst_name
        return self.insts
    def lbl(self, inst_name = 'lbl'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'lbl'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        return self.insts
    def jmp(self, N, inst_name = 'jmp'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'N_'+str(N), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'jmp'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(N), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        return self.insts
    def dec(self, V, inst_name = 'dec'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.G.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'dec'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.nodes()['V_'+str(V)]['label'] = inst_name
        return self.insts
    def addn(self, V, n, inst_name = 'addn'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=-n)
        self.G.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'addn'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.nodes()['V_'+str(V)]['label'] = inst_name
        return self.insts
    def decn(self, V, n, inst_name = 'decn'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=n)
        self.G.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'decn'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.nodes()['V_'+str(V)]['label'] = inst_name
        return self.insts
    def mrg(self, Ns, inst_name = 'mrg'):
        self.insts += 1
        for i in Ns:
            self.G.add_edge('N_'+str(i), 'N_'+str(self.insts+1), weight=1/len(Ns)+1e-6)
        self.node_types['N_'+str(self.insts)] = 'mrg'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        return self.insts
    def jnz(self, V, N, inst_name = 'jnz'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'del1_'+str(self.insts), weight=1.)
        self.G.add_edge('del1_'+str(self.insts), 'del2_'+str(self.insts), weight=1.)
        self.G.add_edge('N_'+str(self.insts), 'delp1_'+str(self.insts), weight=1.)
        self.G.add_edge('delp1_'+str(self.insts), 'delp2_'+str(self.insts), weight=1.)
        self.G.add_edge('delp2_'+str(self.insts), 'delp3_'+str(self.insts), weight=1.)
        self.G.add_edge('delp3_'+str(self.insts), 'delp4_'+str(self.insts), weight=1.)
        self.G.add_edge('del2_'+str(self.insts), 'NJ_'+str(self.insts), weight=1.)
        self.G.add_edge('del2_'+str(self.insts), 'del3_'+str(self.insts), weight=-1.)
        self.G.add_edge('V_'+str(V), 'NJ_'+str(self.insts), weight=-1.)
        self.G.add_edge('NJ_'+str(self.insts), 'V_'+str(V), weight=-1.)
        self.G.add_edge('delp4_'+str(self.insts), 'Np_'+str(self.insts), weight=1.)
        self.G.add_edge('NJ_'+str(self.insts), 'Np_'+str(self.insts), weight=-1.)
        self.G.add_edge('Np_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.G.add_edge('NJ_'+str(self.insts), 'N_'+str(N), weight=1.)
        self.G.add_edge('NJ_'+str(self.insts), 'del3_'+str(self.insts), weight=1.)
        # self.G.add_edge('N_'+str(self.insts+1), 'del3_'+str(N), weight=1.)
        self.G.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.G.add_edge('V_'+str(V), 'delpp1_'+str(self.insts), weight=1.)
        self.G.add_edge('delpp1_'+str(self.insts), 'delpp2_'+str(self.insts), weight=1.)
        self.G.add_edge('delpp2_'+str(self.insts), 'delpp3_'+str(self.insts), weight=1.)
        self.G.add_edge('delpp3_'+str(self.insts), 'del3_'+str(self.insts), weight=1.)
        self.G.add_edge('del3_'+str(self.insts), 'NJ_'+str(self.insts), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'jnz'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['N_'+str(N)]['label'] = inst_name
        self.G.nodes()['V_'+str(V)]['label'] = inst_name
        self.G.nodes()['NJ_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['Np_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['del1_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['del2_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['del3_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp1_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp2_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp3_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp4_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delpp1_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delpp2_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delpp3_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(N), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.nodes()['N_'+str(N)]['label'] = inst_name
        self.Gs.nodes()['V_'+str(V)]['label'] = inst_name
        return self.insts
    def jiz(self, V, N, inst_name = 'jiz'):
        self.insts += 1
        self.G.add_edge('N_'+str(self.insts), 'del1_'+str(self.insts), weight=1.)
        self.G.add_edge('del1_'+str(self.insts), 'del2_'+str(self.insts), weight=1.)
        self.G.add_edge('N_'+str(self.insts), 'delp1_'+str(self.insts), weight=1.)
        self.G.add_edge('delp1_'+str(self.insts), 'delp2_'+str(self.insts), weight=1.)
        self.G.add_edge('delp2_'+str(self.insts), 'delp3_'+str(self.insts), weight=1.)
        self.G.add_edge('delp3_'+str(self.insts), 'delp4_'+str(self.insts), weight=1.)
        self.G.add_edge('del2_'+str(self.insts), 'NJ_'+str(self.insts), weight=1.)
        self.G.add_edge('del2_'+str(self.insts), 'del3_'+str(self.insts), weight=-1.)
        self.G.add_edge('V_'+str(V), 'NJ_'+str(self.insts), weight=-1.)
        self.G.add_edge('NJ_'+str(self.insts), 'V_'+str(V), weight=-1.)
        self.G.add_edge('delp4_'+str(self.insts), 'Np_'+str(self.insts), weight=1.)
        self.G.add_edge('NJ_'+str(self.insts), 'Np_'+str(self.insts), weight=-1.)
        self.G.add_edge('NJ_'+str(self.insts), 'del3_'+str(self.insts), weight=1.)
        # self.G.add_edge('N_'+str(self.insts+1), 'del3_'+str(N), weight=1.)
        self.G.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.G.add_edge('V_'+str(V), 'delpp1_'+str(self.insts), weight=1.)
        self.G.add_edge('delpp1_'+str(self.insts), 'delpp2_'+str(self.insts), weight=1.)
        self.G.add_edge('delpp2_'+str(self.insts), 'delpp3_'+str(self.insts), weight=1.)
        self.G.add_edge('delpp3_'+str(self.insts), 'del3_'+str(self.insts), weight=1.)
        self.G.add_edge('del3_'+str(self.insts), 'NJ_'+str(self.insts), weight=1.)
        self.G.add_edge('NJ_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.G.add_edge('Np_'+str(self.insts), 'N_'+str(N), weight=1.)
        self.node_types['N_'+str(self.insts)] = 'jz'
        self.G.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['N_'+str(N)]['label'] = inst_name
        self.G.nodes()['V_'+str(V)]['label'] = inst_name
        self.G.nodes()['NJ_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['Np_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['del1_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['del2_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['del3_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp1_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp2_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp3_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delp4_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delpp1_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delpp2_'+str(self.insts)]['label'] = inst_name
        self.G.nodes()['delpp3_'+str(self.insts)]['label'] = inst_name
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(self.insts+1), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'N_'+str(N), weight=1.)
        self.Gs.add_edge('N_'+str(self.insts), 'V_'+str(V), weight=1.)
        self.Gs.nodes()['N_'+str(self.insts)]['label'] = inst_name
        self.Gs.nodes()['N_'+str(N)]['label'] = inst_name
        self.Gs.nodes()['V_'+str(V)]['label'] = inst_name
        return self.insts
    
def init_computer(n_insts, n_vars):
    machine = SpikingMachine()

    """
    Instruction Headers
    """
    insts = []
    for inst_i in range(n_insts):
        machine.insts = 10000*(inst_i+1)-1
        ### Instruction Interpreter
        inst_lbl = machine.lbl(inst_name = 'start_instruction')
        insts.append(inst_lbl)

    jump_to_next_instruction = machine.jmp(99999999) # End


    """
    JNZ Instruction Implementation: the variable was not zero, so we determine and jump to the address we were seeking
    """
    jnz_jumps = []
    machine.insts = 999999
    for i in range(n_insts):
        b = machine.jiz(97,insts[i], inst_name = 'do_jnz_jump')
        machine.dec(97, inst_name = 'do_jnz_jump')
        jnz_jumps.append(b)

    """
    JNZ: Here we perform the JNZ instruction itself, using the variable argument from 2999999 (next block)
    """
    load_variable = []
    machine.insts = 4999999
    for i in range(n_vars):
        lbl = machine.lbl(inst_name = 'do_jnz')
        machine.jnz(2000+i,999999+1, inst_name = 'do_jnz')
        load_variable.append(lbl)
        machine.jmp(3999999+1, inst_name = 'do_jnz')


    """
    JNZ: Here we determine what the variable was that the JNZ instruction was taking as an argument
    """
    machine.insts = 2999999
    for i in range(n_vars):
        machine.dec(99, inst_name = 'load_jnz_variable')
        machine.jiz(99, load_variable[i], inst_name = 'load_jnz_variable')

    """
    JNZ: Here we determine the next instruction if the variable was zero
    """
    machine.insts = 3999999
    for i in range(n_insts-1):
        machine.jiz(89,insts[i+1], inst_name = 'goto_next_instruction')
        machine.dec(89, inst_name = 'goto_next_instruction')


    """
    Arithmetic Operation Interpreter
    """
    machine.insts = 5999999
    arithmetic_instructions = []
    for arith_i in range(n_vars):
        adda_lbl = machine.lbl(inst_name = 'do_arithmetic')
        adda = machine.add(2000+arith_i, inst_name = 'do_arithmetic')
        machine.jmp(3999999+1, inst_name = 'do_arithmetic')
        arithmetic_instructions.append(adda_lbl)
        deca_lbl = machine.lbl(inst_name = 'do_arithmetic')
        deca = machine.dec(2000+arith_i, inst_name = 'do_arithmetic')
        machine.jmp(3999999+1, inst_name = 'do_arithmetic')
        arithmetic_instructions.append(deca_lbl)
    a = machine.jmp(3999999+1, inst_name = 'do_arithmetic') # Do Nothing
    arithmetic_instructions.append(a)

    machine.insts = 6999999
    for arithmetic_instruction in arithmetic_instructions:
        b = machine.dec(69, inst_name = 'prep_arithmetic')
        a = machine.jiz(69,arithmetic_instruction, inst_name = 'prep_arithmetic')


    """
    Main Loop Implementation
    """
    for inst_i in range(n_insts):
        """
        This is the special section of the code corresponding to the jump instruction.
        """
        jmp_step = machine.addn(100+10*inst_i, 0, inst_name = 'set_jump_instr') # start jmp step
        machine.decn(99, 999, inst_name = 'set_jump_instr') # reset 99, 98 and 97
        machine.decn(97, 999, inst_name = 'set_jump_instr')
        machine.decn(89, 999, inst_name = 'set_jump_instr')
        lbl = machine.lbl(inst_name = 'set_jump_instr') # Jump label setter
        jump = machine.dec(4000+inst_i, inst_name = 'set_jump_instr')
        machine.add(99, inst_name = 'set_jump_instr') # 99 - Jump Argument Register
        machine.add(98, inst_name = 'set_jump_instr') # 98 - Restore Jump Argument Register
        machine.jnz(4000+inst_i,lbl, inst_name = 'set_jump_instr')
        lbl = machine.lbl(inst_name = 'set_jump_instr') # Jump label setter
        machine.add(4000+inst_i, inst_name = 'set_jump_instr')
        machine.dec(98, inst_name = 'set_jump_instr')
        machine.jnz(98,lbl, inst_name = 'set_jump_instr')

        lbl = machine.lbl(inst_name = 'set_jump_instr') # Jump label setter
        jump = machine.dec(3000+inst_i, inst_name = 'set_jump_instr')
        machine.add(97, inst_name = 'set_jump_instr') # 97 - Jump Argument Register
        machine.add(96, inst_name = 'set_jump_instr') # 96 - Restore Jump Argument Register
        machine.jnz(3000+inst_i,lbl, inst_name = 'set_jump_instr')
        lbl = machine.lbl(inst_name = 'set_jump_instr') # Jump label setter
        machine.add(3000+inst_i, inst_name = 'set_jump_instr')
        machine.dec(96, inst_name = 'set_jump_instr')
        machine.jnz(96,lbl, inst_name = 'set_jump_instr')
        #machine.decn(3000+inst_i, 999, inst_name = 'set_jump_instr')
        machine.dec(99, inst_name = 'set_jump_instr') # num fix
        machine.dec(97, inst_name = 'set_jump_instr') # num fix
        lbl = machine.lbl(inst_name = 'set_jump_instr') # Jump label setter
        abc = machine.addn(89, inst_i, inst_name = 'set_jump_instr') # Set next instruction if jnz fails
        machine.jmp(2999999+1, inst_name = 'set_jump_instr') # Jump to jnz instructions

        """Main Function for Instruction inst_i"""
        machine.insts = 10000*(inst_i+1)
        machine.jiz(100+10*inst_i,jmp_step, inst_name = 'main_jump') # if inst counter is 0, go to jmp step
        machine.decn(68, 999, inst_name = 'reset_arithmetic')
        machine.decn(89, 999, inst_name = 'reset_next_instruction')
        lbl = machine.lbl(inst_name = 'set_arithmetic_instr') # Jump label setter
        jump = machine.dec(100+10*inst_i, inst_name = 'set_arithmetic_instr')
        machine.add(69, inst_name = 'set_arithmetic_instr')
        machine.add(68, inst_name = 'set_arithmetic_instr')
        machine.jnz(100+10*inst_i,lbl, inst_name = 'set_arithmetic_instr')
        lbl = machine.lbl(inst_name = 'set_arithmetic_instr') # Jump label setter
        machine.add(100+10*inst_i, inst_name = 'set_arithmetic_instr')
        machine.dec(68, inst_name = 'set_arithmetic_instr')
        machine.jnz(68,lbl, inst_name = 'set_arithmetic_instr')
        abc = machine.addn(89, inst_i, inst_name = 'set_next_instr') # Set next instruction
        a = machine.jmp(6999999+1, inst_name = 'arithmetic_jump') # Jump to Arithmetic Instruction Interpreter
    return machine