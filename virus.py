class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus():

    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    smallpox = Virus("Smallpox", 0.6, 0.1)
    assert smallpox.name == "Smallpox"
    assert smallpox.repro_rate == 0.6
    assert smallpox.mortality_rate == 0.1

    flu = Virus("Flu", 0.9, 0.05)
    assert flu.name == "Flu"
    assert flu.repro_rate == 0.9
    assert flu.mortality_rate == 0.05

test_virus()

