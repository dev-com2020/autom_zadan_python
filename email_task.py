import argparse
import configparser
import smtplib
from email.message import EmailMessage

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def main(to_email, server, port, from_email, password):
    print(f'Z wyrazami szacunku od {from_email} do {to_email}')

    # Tworzenie wiadomości
    subject = 'Wiadomość testowa od Admina'
    text = '''
               Tutaj miejsce na wstawienie wiadomości
           
           '''
    msg = MIMEMultipart()
    part1 = MIMEText('jakiś tekst', 'plain')
    msg.attach(part1)
    with open('path/image', 'rb') as image:
        part2 = MIMEImage(image.read())
    msg.attach(part2)

    # msg = EmailMessage()
    # msg.set_content(text)
    # msg['Subject'] = subject
    # msg['From'] = from_email
    # msg['To'] = to_email
    # msg['To'] = ','.join(recipients)

    # Nawiązywanie połączenia
    server = smtplib.SMTP_SSL(server, port)
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str, help='docelowy adres')
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'),
                        help='Plik konfiguracyjny', default=None)

    args = parser.parse_args()
    if not args.config:
        print('Błąd! potrzebny plik konfiguracyjny')
        parser.print_help()
        exit(1)
        config = configparser.ConfigParser()
        config.read_file(args.config)

    main(args.email,
         server=config['DEFAULT']['server'],
         port=config['DEFAULT']['port'],
         from_email=config['DEFAULT']['email'],
         password=config['DEFAULT']['password'])
