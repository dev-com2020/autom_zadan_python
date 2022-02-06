import parse
from decimal import Decimal
import delorean


class PriceLog(object):

    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return '<PriceLog ({}, {}, {})>'.format(self.timestamp,
                                                self.product_id,
                                                self.price)

    @classmethod
    def parse(cls, text_log):
        '''
        Przetwarza tekstowy wpis z dziennika o formacie
        [<Czas>] - SPRZEDAŻ - PRODUKT: <nr produktu> - CENA: $<cena>
        na obiekt PriceLog
        '''
        def price(string):
            return Decimal(string)

        def isodate(string):
            return delorean.parse(string)

        FORMAT = ('[{timestamp:isodate}] - SPRZEDAŻ - PRODUKT: {product:d} - '
                  'CENA: ${price:price}')

        formats = {'price': price, 'isodate': isodate}
        result = parse.parse(FORMAT, text_log, formats)

        return cls(timestamp=result['timestamp'],
                   product_id=result['product'],
                   price=result['price'])

