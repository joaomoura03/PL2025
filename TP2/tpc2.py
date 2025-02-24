# nome;desc;anoCriacao;periodo;compositor;duracao;_id

class DataAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
            with open(self.filename, "r") as file:
                lines = file.readlines()
            return [line.strip().split(';') for line in lines[1:]]

    def write_to_file(self, text):
            with open("resultados.txt", "a") as output_file:
                output_file.write(text + "\n\n___________________________________\n")

    def listar_alfabeticamente(self, data):
        composers = {entry[4] for entry in data}
        sorted_composers = sorted(composers)
        list_text = "\n".join(sorted_composers)
        self.write_to_file("Lista ordenada alfabeticamente dos compositores musicais:\n" + list_text)

    def distribuicao_obras(self, data):
        periodo_count = {}
        for entry in data:
            periodo = entry[3]
            if periodo in periodo_count:
                periodo_count[periodo] += 1
            else:
                periodo_count[periodo] = 1
        periodos_text = "\n".join([f"{periodo}: {count} obras" for periodo, count in sorted(periodo_count.items())])
        self.write_to_file("Distribuição das obras por período:\n" + periodos_text)

    def dicionario_por_periodo(self, data):
        periodo_dict = {}
        for entry in data:
            periodo = entry[3]
            titulo = entry[0]
            if periodo not in periodo_dict:
                periodo_dict[periodo] = []
            periodo_dict[periodo].append(titulo)
        for periodo in periodo_dict:
            periodo_dict[periodo].sort()
        dict_text = "\n".join([f"{periodo}: {', '.join(periodo_dict[periodo])}" for periodo in sorted(periodo_dict)])
        self.write_to_file("Dicionário de obras por período:\n" + dict_text)

    def analyze_data(self):
        data = self.read_data()
        self.listar_alfabeticamente(data)
        self.distribuicao_obras(data)
        self.dicionario_por_periodo(data)


analyzer = DataAnalyzer("obras.csv")
analyzer.analyze_data()