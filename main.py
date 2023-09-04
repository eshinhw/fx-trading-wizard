from trade import entry

INSTRUMENTS = ["EUR_USD", "GBP_USD", "AUD_USD", "NZD_USD"]


def main():
    for ins in INSTRUMENTS:
        entry(ins)


if __name__ == "__main__":
    main()
