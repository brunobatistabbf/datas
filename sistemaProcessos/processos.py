class process:
    PID:int;
    TP:int;
    CP:int;
    EP:str;
    NES:int;
    N_CPU:int;
    limiteTP:int;

    def __int__(self, PID,  TP,  CP,  EP, NES,  N_CPU,  limiteTP):
        self.PID = PID
        self.TP = TP
        self.CP = CP
        self.EP = EP
        self.NES = NES
        self.N_CPU = N_CPU
        self.limiteTP = limiteTP