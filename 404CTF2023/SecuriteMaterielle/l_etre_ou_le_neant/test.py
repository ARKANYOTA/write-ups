from myhdl import *


@block
def time_to_see(clk):
    @always(clk.posedge)
    def core():
        print("\thello")

    return core

@block
def mux(z,a,b,sel):
    @always_comb
    def comb():
        if sel == 1:
            z.next = a
        else:
            z.next = b

    return comb


@block
def go_up_go_up_GO_UP(inp):
    tic_tac_toe = Signal(bool(0))

    a = time_to_see(tic_tac_toe)
    b = mux(Signal(0),Signal(0),Signal(0),Signal(0) )

    @always(delay(10))
    def seq():
        tic_tac_toe.next = not tic_tac_toe

    return seq,a,b

simInst = go_up_go_up_GO_UP(Signal(0))
simInst.run_sim(170)


