import pandas as pd
from spk_model import WeightedProduct

class Phone():

    def __init__(self) -> None:
        self.phone = pd.read_csv('web\dump-pemilihan_ponsel-201011401759.csv')

    def get_recs(self, kriteria):
        wp = WeightedProduct(self.phone.to_dict(orient="records"), kriteria)
        return wp.calculate

