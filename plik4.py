from price_log import PriceLog

with open('example.log') as file:
    logs = [PriceLog.parse(log) for log in file]

total = sum(log.price for log in logs)
print(total)