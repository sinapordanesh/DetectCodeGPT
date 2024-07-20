def count_verdicts(N, verdicts):
    AC = verdicts.count("AC")
    WA = verdicts.count("WA")
    TLE = verdicts.count("TLE")
    RE = verdicts.count("RE")
    
    return f"AC x {AC}\nWA x {WA}\nTLE x {TLE}\nRE x {RE}"