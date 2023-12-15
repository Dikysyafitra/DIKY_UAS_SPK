import sys
from colorama import Fore, Style
from models import Base, leptop
from engine import engine
from tabulate import tabulate
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import DEV_SCALE

session = Session(engine)


def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has been created!')


def review_data():
    query = select(leptop)
    for laptop in session.query(leptop).all():
        print(laptop)


class BaseMethod():
    def __init__(self):
        self.raw_weight = {'ram': 4, 'cpu': 3, 'gpu': 4, 'baterai': 3, 'harga': 5, 'ukuran_layar': 4}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v / total_weight, 2) for k, v in self.raw_weight.items()}

    def extract_numeric_values_int(self, spec, data_key):
        numeric_values = [int(value.split()[0]) for value in spec.split(',') if value.split()[0].isdigit()]
        max_value = max(numeric_values) if numeric_values else 1
        return {data_key: max_value}

    def extract_numeric_values_float(self, spec, data_key):
        numeric_values = [float(value.split()[0]) for value in spec.split(',') if value.split()[0].replace('.', '').isdigit()]
        max_value = max(numeric_values) if numeric_values else 1
        return {data_key: max_value}

    def extract_harga_value(self, harga, data_key):
        harga_cleaned = ''.join(char for char in harga if char.isdigit())
        return {data_key: float(harga_cleaned)} if harga_cleaned else {data_key: 0}

    @property
    def data(self):
        query = select(leptop.no, leptop.brand, leptop.ram, leptop.cpu, leptop.gpu,
                       leptop.baterai, leptop.harga, leptop.ukuran_layar)
        result = session.execute(query).fetchall()
        return [{'no': laptop.no, 'brand': laptop.brand, 'ram': laptop.ram, 'cpu': laptop.cpu,
                 'gpu': laptop.gpu, 'baterai': laptop.baterai, 'harga': laptop.harga, 'ukuran_layar': laptop.ukuran_layar} for laptop in result]

    @property
    def normalized_data(self):
        ram_values = [self.extract_numeric_values_int(laptop['ram'], 'ram') for laptop in self.data]
        cpu_values = [self.extract_numeric_values_int(laptop['cpu'], 'cpu') for laptop in self.data]
        gpu_values = [self.extract_numeric_values_int(laptop['gpu'], 'gpu') for laptop in self.data]
        baterai_values = [self.extract_numeric_values_int(laptop['baterai'], 'baterai') for laptop in self.data]
        harga_values = [self.extract_harga_value(laptop['harga'], 'harga') for laptop in self.data]
        layar_values = [self.extract_numeric_values_float(laptop['ukuran_layar'], 'ukuran_layar') for laptop in self.data]

        return [dict(no=laptop['no'], **ram, **cpu, **gpu, **baterai, **harga, **layar)
                for laptop, ram, cpu, gpu, baterai, harga, layar in
                zip(self.data, ram_values, cpu_values, gpu_values, baterai_values, harga_values, layar_values)]

class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        normalized_data = self.normalized_data
        produk = [
            {
                'no': row['no'],
                'ram': row['ram']**self.weight['ram'],
                'cpu': row['cpu']**self.weight['cpu'],
                'gpu': row['gpu']**self.weight['gpu'],
                'ukuran_layar': row['ukuran_layar']**self.weight['ukuran_layar'],
                'baterai': row['baterai']**self.weight['baterai'],
                'harga': row['harga']**self.weight['harga'],
                'produk': (
                    row['ram']**self.weight['ram'] *
                    row['cpu']**self.weight['cpu'] *
                    row['gpu']**self.weight['gpu'] *
                    row['ukuran_layar']**self.weight['ukuran_layar'] *
                    row['baterai']**self.weight['baterai'] *
                    row['harga']**self.weight['harga']
                )
            }
            for row in normalized_data
        ]
        sorted_produk = sorted(produk, key=lambda x: x['produk'], reverse=True)
        sorted_data = [
            {
                'no': product['no'],
                'score': product['produk']  # Nilai skor akhir
            }
            for product in sorted_produk
        ]
        return sorted_data


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {row['no']:
                  round(
                      row['ram'] * weight['ram'] +
                      row['cpu'] * weight['cpu'] +
                      row['gpu'] * weight['gpu'] +
                      row['ukuran_layar'] * weight['ukuran_layar'] +
                      row['baterai'] * weight['baterai'] +
                      row['harga'] * weight['harga'], 2)
                  for row in self.normalized_data
                  }
        sorted_result = dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True))
        return sorted_result


def run_saw():
    saw = SimpleAdditiveWeighting()
    result = saw.calculate
    print(tabulate(result.items(), headers=['No', 'Score'], tablefmt='pretty'))



def run_wp():
    wp = WeightedProduct()
    result = wp.calculate
    headers = result[0].keys()
    rows = [
        {k: round(v, 4) if isinstance(v, float) else v for k, v in val.items()}
        for val in result
    ]
    print(tabulate(rows, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == 'create_table':
            create_table()
        elif arg == 'saw':
            run_saw()
        elif arg == 'wp':
            run_wp()
        else:
            print('Command not found')