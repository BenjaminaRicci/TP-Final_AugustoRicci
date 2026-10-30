import time

# Parámetros definidos
UMBRAL_FIEBRE = 38.0
UMBRAL_HIPOTERMIA = 35.0
TEMP_MIN_VALIDA = 25.0
TEMP_MAX_VALIDA = 45.0

INTERVALO_MUESTREO = 5  # segundos
MUESTRAS_ALERTA = 5     # 5 muestras para fiebre/hipotermia
MUESTRAS_ERROR = 10     # 10 muestras fuera de rango para error de sensor

contador_fiebre = 0
contador_hipotermia = 0
contador_error_sensor = 0

def leer_sensor_temperatura():
    # Simulamos una lectura. Podría devolver un valor erróneo o 0 si está desconectado
    return 0.0 

print("Iniciando monitoreo continuo con autodiagnóstico de sensor...")

while True:
    temp_actual = leer_sensor_temperatura()
    print(f"Temperatura leída: {temp_actual}°C")
    
    # --- 1. VERIFICACIÓN DE INTEGRIDAD DEL SENSOR (FUERA DE RANGO) ---
    if temp_actual < TEMP_MIN_VALIDA or temp_actual > TEMP_MAX_VALIDA:
        contador_error_sensor += 1
        print(f"⚠️ Advertencia: Lectura fuera de rango. Conteo error: {contador_error_sensor}/{MUESTRAS_ERROR}")
    else:
        contador_error_sensor = 0  # Si vuelve a la normalidad, reseteamos el error
        
    # Si se acumulan 10 lecturas inválidas consecutivas -> Falla de sensor
    if contador_error_sensor >= MUESTRAS_ERROR:
        print("🔴 ¡FALLA CRÍTICA: Sensor desconectado o en mal funcionamiento! (Encendiendo LED de error)")
        # ACÁ ACTIVAS EL LED DE ERROR EN LA PI 1 (Y podés mandar un aviso a la Pi 2)
        
    else:
        # --- 2. LÓGICA DE FIEBRE Y HIPOTERMIA (Solo si el sensor funciona bien) ---
        if temp_actual >= UMBRAL_FIEBRE:
            contador_fiebre += 1
            print(f"⚠️ Posible fiebre. Consecutivo: {contador_fiebre}/{MUESTRAS_ALERTA}")
        else:
            contador_fiebre = 0
            
        if temp_actual <= UMBRAL_HIPOTERMIA:
            contador_hipotermia += 1
            print(f"⚠️ Posible hipotermia. Consecutivo: {contador_hipotermia}/{MUESTRAS_ALERTA}")
        else:
            contador_hipotermia = 0

        # --- 3. CONFIRMACIÓN DE ALERTAS CLÍNICAS ---
        if contador_fiebre >= MUESTRAS_ALERTA:
            print("🚨 ¡ALERTA CONFIRMADA: FIEBRE! (Enviando trama a central)")
        elif contador_hipotermia >= MUESTRAS_ALERTA:
            print("🚨 ¡ALERTA CONFIRMADA: HIPOTERMIA! (Enviando trama a central)")

    time.sleep(INTERVALO_MUESTREO)