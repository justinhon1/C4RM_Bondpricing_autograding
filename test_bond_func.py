import bond_func

def test_Bond():
    assert round(bond_func.BondPricer(0.03,2000000,0.04,10,2)) == 2171686
