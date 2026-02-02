# DeOldify – Entorno reproducible en macOS Apple Silicon

Este repositorio documenta y proporciona una configuración **funcional, estable y reproducible**
para ejecutar **DeOldify** en hardware Apple Silicon moderno.

El trabajo fue realizado y validado específicamente para permitir el uso de DeOldify en una
**MacBook Pro con chip Apple M4**, resolviendo múltiples problemas de compatibilidad que impiden
que el proyecto original funcione correctamente “out of the box” en macOS actual.

---

## 🖥️ Entorno probado

Este repositorio fue desarrollado y probado en el siguiente entorno:

- **Equipo:** MacBook Pro
- **Chip:** Apple M4 (Apple Silicon)
- **Memoria RAM:** 16 GB
- **Arquitectura:** arm64
- **Sistema operativo:** macOS Tahoe 26.2
- **Python:** 3.10.x
- **Aceleración:** CPU / Apple MPS (sin CUDA)

No se garantiza el funcionamiento en otros entornos sin ajustes adicionales, aunque puede servir
como referencia técnica.

---

## 📜 Historia del problema

DeOldify es un proyecto ampliamente conocido para la colorización de imágenes históricas.
Sin embargo, su base de código fue desarrollada originalmente para entornos Linux y versiones
anteriores de Python, PyTorch y fastai.

Al intentar ejecutar DeOldify en un entorno moderno —especialmente en **Apple Silicon (ARM64)**
con versiones actuales de macOS— aparecen múltiples problemas, entre ellos:

- Incompatibilidades entre **NumPy 2.x** y extensiones compiladas para NumPy 1.x
- Cambios en los mecanismos de carga segura de modelos en **PyTorch**
- Dependencias eliminadas o renombradas (`ffmpeg`, `yt_dlp`, `yaml`, etc.)
- Conflictos entre versiones modernas de **fastai**, **torch** y **opencv**
- Errores difíciles de diagnosticar para usuarios sin experiencia previa

El objetivo de este repositorio es **documentar y resolver de forma reproducible** estos problemas,
dejando un entorno funcional que pueda reinstalarse fácilmente en pocos minutos.

---

## 🎯 Objetivo del repositorio

Este repositorio **no pretende modificar el funcionamiento interno de DeOldify**, sino:

- Documentar una **configuración funcional real** en macOS moderno
- Fijar versiones críticas de dependencias para evitar roturas
- Proporcionar una instalación reproducible mediante `setup.sh`
- Ofrecer una interfaz de línea de comandos simple (`colorize.py`)
- Facilitar que terceros puedan entender, reproducir o mejorar la solución

---

## ⚙️ Instalación automática (2 minutos)

Para usuarios que parten desde cero.

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/rpasin/DeOldify.git
cd DeOldify