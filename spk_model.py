from settings import NAMA

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.phone_data = data_dict

        # 1-6
        self.raw_weight = {
            'Nama_Ponsel':5,
            'Harga':4,
            'Kualitas_Kamera':3,
            'Kapasitas_Baterai':2,
            'Kinerja':6,
            'Ukuran_Layar':1
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': phone['id'],
            'Nama_Ponsel': NAMA[phone['Nama_Ponsel']],
            'Harga': phone['Harga'],
            'Kualitas_Kamera': phone['Kualitas_Kamera'],
            'Kapasitas_Baterai': phone['Kapasitas_Baterai'],
            'Kinerja': phone['Kinerja'],
            'Ukuran_Layar': phone['Ukuran_Layar']
        } for phone in self.phone_data]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        Nama_Ponsel = [] # max
        Harga = [] # min
        Kualitas_Kamera = [] # max
        Kapasitas_Baterai = [] # max
        Kinerja = [] # max
        Ukuran_Layar = [] # max

        for data in self.data:
            Nama_Ponsel.append(data['Nama_Ponsel'])
            Harga.append(data['Harga'])
            Kualitas_Kamera.append(data['Kualitas_Kamera'])
            Kapasitas_Baterai.append(data['Kapasitas_Baterai'])
            Kinerja.append(data['Kinerja'])
            Ukuran_Layar.append(data['Ukuran_Layar'])

        max_Nama_Ponsel = max(Nama_Ponsel)
        min_Harga = min(Harga)
        max_Kualitas_Kamera = max(Kualitas_Kamera)
        max_Kapasitas_Baterai = max(Kapasitas_Baterai)
        max_Kinerja = max(Kinerja)
        max_Ukuran_Layar = max(Ukuran_Layar)

        return [{
            'id': data['id'],
            'Nama_Ponsel': data['Nama_Ponsel']/max_Nama_Ponsel, # benefit
            'Harga': min_Harga/data['Harga'], # benefit
            'Kualitas_Kamera': data['Kualitas_Kamera']/max_Kualitas_Kamera, # benefit
            'Kapasitas_Baterai': data['Kapasitas_Baterai']/max_Kapasitas_Baterai, # benefit
            'Kinerja': data['Kinerja']/max_Kinerja, # benefit
            'Ukuran_Layar': data['Ukuran_Layar']/max_Ukuran_Layar, # benefit
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    def __init__(self, phone_data, setWeight:dict):
        super().__init__(data_dict=phone_data, **setWeight)

    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['id']:
            round(
                row['Nama_Ponsel'] ** weight['Nama_Ponsel'] *
                row['Harga'] ** (-weight['Harga']) *
                row['Kualitas_Kamera'] ** weight['Kualitas_Kamera'] *
                row['Kapasitas_Baterai'] ** weight['Kapasitas_Baterai'] *
                row['Kinerja'] ** weight['Kinerja'] *
                row['Ukuran_Layar'] ** weight['Ukuran_Layar']
                ,2)
            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))
