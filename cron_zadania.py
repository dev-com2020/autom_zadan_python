import argparse
import configparser
from datetime import datetime
import sys
import yaml


def main(number, other_number, output):
    result = number * other_number
    print(f'[{datetime.utcnow().isoformat()}] Wynik wynosi {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='Plik konfiguracji'
                        , default='etc/automate.ini')
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Plik z danymi wyjściowymi',
                        default=sys.stdout)

    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config['ARG']['n1'])
        args.n2 = int(config['ARG']['n2'])

    main(args.n1, args.n2, args.output)

# chmod +x cron_zadania.py