import argparse
import sys
import logging

LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG


def main(number, other_number, output):
    logging.info(f'Dzielenie {number} przez {other_number}')
    result = number / other_number
    print(f'Wynik dzielenia wynosi= {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='liczba', default=1)
    parser.add_argument('-n2', type=int, help='druga liczba', default=1)
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Plik z danymi wyjściowymi',
                        default=sys.stdout)
    parser.add_argument('-l', dest='log', type=str, help='Plik dziennnika', default=None)

    args = parser.parse_args()

    if args.log:
        logging.basicConfig(format=LOG_FORMAT, filename=args.log, level=LOG_LEVEL)
    else:
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
    try:
        main(args.n1, args.n2, args.output)
    except Exception as exc:
        logging.exception("Błąd w czasie wykonywania zadania")
        exit(1)
