import sqlite3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import os
from dotenv import load_dotenv
import threading

load_dotenv()

# Agora você pode acessar as variáveis de ambiente
DB_NAME = os.getenv('DB_NAME')

class Graphic:

    def __init__(self):
        # Configuração do gráfico
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(12, 6))
        # Atribuir a animação a um atributo da instância
        self.ani = None

    def fetch_data(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT timestamp, temperature, humidity FROM weather ORDER BY timestamp')
        data = cursor.fetchall()
        conn.close()
        return data

    def plot_data(self):
        data = self.fetch_data()
        if not data:
            return [], [], []

        # Convert timestamps to datetime objects
        timestamps = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts, _, _ in data]
        temperatures = [temp for _, temp, _ in data]
        humidities = [hum for _, _, hum in data]

        return timestamps, temperatures, humidities

    def update_plot(self, frame):
        timestamps, temperatures, humidities = self.plot_data()

        if not timestamps:
            return

        # Limpar os gráficos
        self.ax1.clear()
        self.ax2.clear()

        # Ativar grade para ambos os eixos
        self.ax1.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
        self.ax2.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)

        # Plotar temperatura
        self.ax1.plot(timestamps, temperatures, label='Temperature', color='blue')
        self.ax1.set_title('Temperature over Time')
        self.ax1.set_xlabel('Timestamp')
        self.ax1.set_ylabel('Temperature (°C)')
        self.ax1.legend()
        self.ax1.tick_params(axis='x', rotation=90)

        # Plotar umidade
        self.ax2.plot(timestamps, humidities, label='Humidity', color='orange')
        self.ax2.set_title('Humidity over Time')
        self.ax2.set_xlabel('Timestamp')
        self.ax2.set_ylabel('Humidity (%)')
        self.ax2.legend()
        self.ax2.tick_params(axis='x', rotation=90)

        # Ajustar layout
        plt.tight_layout()
        
    def start(self):
        
        try:
            # Verifique se há dados antes de criar a animação
            dados = self.plot_data()
            
            self.ani = animation.FuncAnimation(self.fig, self.update_plot, interval=5000)
            
            # Verifique se self.ani foi inicializado corretamente
            if dados:
                plt.show()
            else:
                print("Failed to initialize animation.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

def run_graphic():
    graphic = Graphic()
    graphic.start()

# Iniciar o gráfico em uma thread separada
thread = threading.Thread(target=run_graphic)
thread.start()
