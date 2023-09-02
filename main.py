from trade import entry

INSTRUMENTS = ["EUR_USD", "GBP_USD"]


def main():
    for ins in INSTRUMENTS:
        entry(ins)
