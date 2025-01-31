from pathlib import Path
from dotenv import load_dotenv
from loguru import logger
import os

# Load environment variables from .env file if it exists
RUTA_GLOBAL = os.getcwd().split('\\03. Relationship')[0]
load_dotenv()

PROJ_ROOT = Path(__file__).resolve().parents[1]
RUTA_DATA = r"C:\Users\DF357JZ\EY\INTERBANCO - INTERCONSUMO - PRICING - Interbanco_-_Pricing\03. Relationship\2.1 Analytics\data"

RUTA_CLIENTES_PROCESADO = RUTA_DATA + "\\02_interim\\clientes_procesado.parquet"
RUTA_RENTABILIDAD_PROCESADO = RUTA_DATA + "\\02_interim\\rentabilidad_procesada_periodo_cliente.parquet"
RUTA_CLUSTERS = RUTA_DATA + "\\04_model output\\clientes_historicos_clasificados.parquet.parquet"

RUTA_CLIENTES = RUTA_DATA + os.getenv('RUTA_CLIENTES_2')
RUTA_RENTABILIDAD_CLIENTE = RUTA_DATA + os.getenv('RUTA_RENTABILIDAD_CLIENTE')
RUTA_STOCK = RUTA_DATA + os.getenv('RUTA_STOCK_2')
RUTA_DESEMBOLSOS = RUTA_DATA + os.getenv('RUTA_DESEMBOLSOS_2')
RUTA_COTIZACIONES = RUTA_DATA + os.getenv('RUTA_COTIZACIONES')
RUTA_SERVICIOS = RUTA_DATA + os.getenv('RUTA_SERVICIOS')
RUTA_BURO = RUTA_DATA + os.getenv('RUTA_BURO')
RUTA_CAMP = RUTA_DATA + os.getenv('RUTA_CAMP')
RUTA_RENTABILIDAD = RUTA_DATA + os.getenv('RUTA_RENTABILIDAD')
RUTA_NOMBRE_COLUMNAS = RUTA_DATA + os.getenv('RUTA_NOMBRE_COLUMNAS')
RUTA_PERDIDA_ESPERADA = RUTA_DATA + os.getenv('RUTA_PERDIDA_ESPERADA')
RUTA_CLIENTES_CLUSTERIZADOS = r"C:\Users\DF357JZ\EY\INTERBANCO - INTERCONSUMO - PRICING - Interbanco_-_Pricing\03. Relationship\2.1 Analytics\data\04_model output\clientes_historicos_clasificados.parquet"


RUTA_DATA_INTERIM=RUTA_DATA+os.getenv('RUTA_DATA_INTERIM')
RUTA_DATA_EXTERNAL=RUTA_DATA+os.getenv('RUTA_DATA_EXTERNAL')
RUTA_DATA_RAW=RUTA_DATA+os.getenv('RUTA_DATA_RAW')
RUTA_DATA_PROCESSED=RUTA_DATA+os.getenv('RUTA_DATA_PROCESSED')


RUBROS_INGRESOS = ['Intereses por Creditos','Credito por Proveer Fondos', 'Venta de Divisas','Tarjeta de Débito', 'Cédulas Hipotecarias (FHA)','Por tarjeta de crédito',
                   'Administración de Cuentas','Compra de Divisas','Por prestamos','Servicios de Comercio Exterior','Cash Management','Por cartas de crédito',
                   'Servicios a Cuentahabientes','Por cancelaciones Anticipadas','Impuestos','Cobros por Cuenta Ajena','Seguros','Transferencias','Agua, Electricidad y Teléfono']
