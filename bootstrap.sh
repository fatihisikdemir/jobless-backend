#!/bin/bash

echo "🔧 Jobless as a Service™ — Inicialización total"
echo "-----------------------------------------------"


# 1. Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# 2. Aplicar migraciones
echo "🧱 Aplicando migraciones..."
python manage.py migrate

# 3. Crear superusuario y usuarios de prueba
echo "👤 Creando usuarios administrativos y de prueba..."
python manage.py seed_admin

