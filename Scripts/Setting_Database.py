import pandas


class DBSetup:
    def __new__(cls, *args, **kwargs):
        info = """
        - Author = Bruno Santos
        - Developed Data = 16/05/2022
        """
        print(info)
        print('_' * 50)
        return object.__new__(cls)

    def __init__(self) -> None:
        self.DB_Path: str = '../Database/2022-05-10-11-15-59.csv'
        self.DF_Date: list = []
        self.DF_Condensing_Temperature: list = []
        self.DF_Condensing_Pressure: list = []
        self.DF_Evaporation_Temperature: list = []
        self.DF_Evaporation_Pressure: list = []
        self.Dict_Parameters: dict = {}
        return

    def db_setting(self):
        # ___________________________ [Reading Database File] ____________________________________________
        db_read_file = pandas.read_csv(self.DB_Path, engine='python', delimiter=';', date_parser=True,
                                       skiprows=0, skipfooter=34)

        # _______________________________ [Data Analyze] _________________________________________________
        # print(db_read_file.info())

        # ___________________________ [Deleting Invalid Values] ___________________________________________
        db_csv_file = db_read_file.drop(db_read_file.index[db_read_file['Superaquecimento [K]'] == 'xxx'], axis=0)

        # ___________________________ [Deleting Invalid Columns] __________________________________________
        db_csv_file = db_csv_file.drop(columns=['Unnamed: 9', 'Unnamed: 10'], axis=1)

        # _____________________________ [Deleting Nan Values] _____________________________________________
        db_csv_file = db_csv_file.dropna(axis=0, how='all')

        # _____________________________ [Creating Dataframes] _____________________________________________
        self.DF_Evaporation_Pressure = \
            db_csv_file['Baixa pressão [psi]'].apply(lambda x: x.replace(',', '.')).astype(float).tolist()

        self.DF_Evaporation_Temperature = \
            db_csv_file['Temperatura de evaporação [°C]'].apply(lambda x: x.replace(',', '.')).astype(float).tolist()

        self.DF_Condensing_Pressure = \
            db_csv_file['Alta pressão [psi]'].apply(lambda x: x.replace(',', '.')).astype(float).tolist()

        self.DF_Condensing_Temperature = \
            db_csv_file['Temperatura de condensação [°C]'].apply(lambda x: x.replace(',', '.')).astype(float).tolist()

        self.Dict_Parameters["LP"] = self.DF_Evaporation_Pressure
        self.Dict_Parameters["HP"] = self.DF_Condensing_Pressure
        self.Dict_Parameters["LT"] = self.DF_Evaporation_Temperature
        self.Dict_Parameters["HT"] = self.DF_Condensing_Temperature
        return self.Dict_Parameters

    def update(self):
        self.db_setting()
        return self.Dict_Parameters


if __name__ == '__main__':
    DBSetup().update()
