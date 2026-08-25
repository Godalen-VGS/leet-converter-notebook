import oppgave
import pytest

@pytest.mark.parametrize("tekst,forventet", [("tall", "7411"), ("LEET", "1337")])
def test_leet_eksempler(tekst, forventet):
    assert oppgave.oversett_til_leet(tekst) == forventet
