#!/usr/bin/env bash

echo "🔧 Configurando entorno DeOldify..."

# Verificar Python 3.10
if ! command -v python3.10 &> /dev/null; then
    echo "❌ Python 3.10 no encontrado. Instálalo antes de continuar."
    exit 1
fi

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3.10 -m venv venv

# Activar entorno
echo "⚡ Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip
echo "⬆️ Actualizando pip..."
python -m pip install --upgrade pip

# Instalar dependencias exactas
echo "📥 Instalando dependencias..."
pip install -r requirements.lock.txt

echo "✅ Instalación completada"
echo "👉 Para usar: source venv/bin/activate"
