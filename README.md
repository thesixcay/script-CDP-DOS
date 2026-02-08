
**Nombre:** Osvaldo Alejandro Solano Gonzalez  
**Matrícula:** 2024-2361  

---

## 🎯 Objetivo del Laboratorio

El objetivo de este laboratorio es analizar el impacto de un **ataque de Denegación de Servicio (DoS)** basado en el **Cisco Discovery Protocol (CDP)** sobre dispositivos Cisco, dentro de un entorno **controlado y autorizado**.

Se evalúa cómo la generación de tráfico CDP anómalo puede afectar el rendimiento de un **switch o router Cisco**, incrementando el consumo de CPU y provocando comportamientos anómalos en la tabla de vecinos CDP.

⚠️ Este laboratorio es **exclusivamente educativo** y no debe ejecutarse en redes reales.

---

## 🧠 Descripción del Ataque CDP DoS

CDP es un protocolo propietario de Cisco que opera en **capa 2**, utilizado para el descubrimiento de dispositivos de red.

El ataque DoS por CDP consiste en:
- Generar un alto volumen de tramas CDP.
- Forzar al dispositivo Cisco a procesar continuamente estos anuncios.
- Provocar impacto en el rendimiento mediante:
  - Aumento del consumo de CPU.
  - Saturación de la tabla de vecinos CDP.
  - Posible degradación del servicio de red.

📌 **Importante:**  
Este ataque **no se dirige a una dirección IP**, ya que CDP no utiliza capa 3.

---

## 🌐 Topología de Red

La topología utilizada en este laboratorio se muestra a continuación:

<img width="751" height="663" alt="image" src="https://github.com/user-attachments/assets/bc1bac45-866a-4afb-9c6c-32d36f4ffeda" />

## ▶️ Ejecución del Laboratorio (Kali Linux)

La siguiente evidencia corresponde a la ejecución del laboratorio desde **Kali Linux**, donde se genera tráfico CDP de forma masiva en un entorno controlado.

Durante esta fase, el tráfico es capturado y analizado utilizando **Wireshark**, permitiendo observar los paquetes CDP enviados y confirmar la generación del flujo anómalo de capa 2.

<img width="661" height="476" alt="image" src="https://github.com/user-attachments/assets/6efd8ae1-22b3-420a-b82d-2707d0fd897c" />


---

## 🔍 Análisis de Tráfico con Wireshark
<img width="794" height="465" alt="image" src="https://github.com/user-attachments/assets/7d215b55-a6d6-4886-9611-fbefee6f8ca1" />

Wireshark fue utilizado para capturar el tráfico generado durante el laboratorio.

El análisis permite observar:
- Tramas CDP enviadas de forma repetitiva.
- Uso del multicast CDP (**01:00:0c:cc:cc:cc**).
- Comportamiento anómalo del tráfico de descubrimiento.

## 🧱 Dispositivos del Laboratorio

### 🔹 Router Cisco – Osvaldo-Solano
- Función: Gateway y servidor DHCP.
- CDP habilitado para fines de laboratorio.
- Conectado al switch mediante enlace trunk (VLAN 61).

### 🔹 Switch Cisco – SW-Osvaldo
- Función: Dispositivo víctima del ataque CDP DoS.
- CDP habilitado en interfaces.
- Enlace trunk hacia el router.

### 🔹 Host Kali Linux
- Función: Generador de tráfico CDP.
- Ubicado en VLAN 61.
- Utilizado exclusivamente con fines educativos.

---

## 📌 Direccionamiento IP

- Red: 192.168.61.0/24  
- Gateway: 192.168.61.1  
- IP de administración del switch: 192.168.61.2  
- Rango DHCP: 192.168.61.31 – 192.168.61.254  
- VLAN utilizada: 61  
---

## 🛡️ Medidas de Mitigación

Para prevenir ataques DoS basados en CDP en redes reales se recomienda:

1. Deshabilitar CDP globalmente si no es necesario:
   ```cisco
   no cdp run
   ```

2. Deshabilitar CDP por interfaz hacia hosts finales:
   ```cisco
   interface gi0/1
    no cdp enable
   ```

3. Implementar segmentación de red mediante VLANs.
4. Monitorear constantemente el uso de CPU.
5. Aplicar buenas prácticas de hardening en dispositivos Cisco.

---

## 🎥 Video Demostración

https://youtu.be/S-SxRKaqKVw?si=ifFmSCCscxyJbgo2

El video incluye:
1. Topología con nombre y matrícula.
2. Fecha y hora del sistema.
3. Rostro y voz del autor.
4. Evidencia del tráfico CDP en Wireshark.

---

⚠️ **Aviso Legal**  
Este laboratorio fue desarrollado únicamente con fines educativos y académicos.  
El autor no se responsabiliza por el uso indebido de la información fuera de entornos no autorizados.

