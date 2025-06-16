#!/bin/bash

# ===================================================================================
# SCRIPT DE PRUEBAS PARA LA API DE GESTIÓN DE ACADEMIAS
# ===================================================================================
#
# Instrucciones:
# 1. Guarda este archivo como 'test_api.sh' en la raíz de tu proyecto.
# 2. Reemplaza los valores de las variables URL_... con los endpoints de tus despliegues.
# 3. Dale permisos de ejecución con: chmod +x test_api.sh
# 4. Ejecútalo con: ./test_api.sh
#
# ===================================================================================

# --- CONFIGURACIÓN: Reemplaza estas URLs con las de tus despliegues ---
URL_USERS="http://localhost:4566/restapis/kfazpbuebz/local/_user_request_/users"
URL_SUCURSALES="http://localhost:4566/restapis/bntx7wvqa6/local/_user_request_/sucursales"
URL_TIPOS_NIVEL="http://localhost:4566/restapis/ertcwvrttr/local/_user_request_/tipos-nivel"
URL_NIVELES="http://localhost:4566/restapis/gclxpronko/local/_user_request_/niveles"
# --------------------------------------------------------------------


# --- Funciones de Ayuda para una Salida Bonita ---
log_step() {
  echo ""
  echo "---------------------------------------------------------"
  echo "➡️  $1"
  echo "---------------------------------------------------------"
}

# --- INICIO DE LAS PRUEBAS ---
echo "🚀 INICIANDO SUITE DE PRUEBAS DE LA API DE ACADEMIAS..."

# --- Pruebas de TIPO NIVEL SERVICE ---
log_step "Probando: TIPO NIVEL SERVICE"
echo "Creando un nuevo Tipo de Nivel (Danza Contemporánea)..."
TIPO_NIVEL_RESPONSE=$(curl --location --request POST "${URL_TIPOS_NIVEL}/tipos-nivel" --header 'Content-Type: application/json' --data-raw '{"nombre": "Danza Contemporánea", "edad_minima": 16, "edad_maxima": 99}')
echo "Respuesta: $TIPO_NIVEL_RESPONSE"
TIPO_NIVEL_ID=$(echo $TIPO_NIVEL_RESPONSE | jq -r '.id')
echo "✅ ID de Tipo de Nivel capturado: $TIPO_NIVEL_ID"

# --- Pruebas de USER SERVICE ---
log_step "Probando: USER SERVICE"
echo "Creando una nueva Maestra (Marta Graham)..."
MAESTRA_RESPONSE=$(curl --location --request POST "${URL_USERS}/users" --header 'Content-Type: application/json' --data-raw '{"nombre": "Marta Graham", "rut": "55555555-5", "email": "marta@test.com", "edad": 40, "rol": "Maestra", "sucursal": "Centro"}')
echo "Respuesta: $MAESTRA_RESPONSE"
MAESTRA_ID=$(echo $MAESTRA_RESPONSE | jq -r '.id')
echo "✅ ID de Maestra capturado: $MAESTRA_ID"

# --- Pruebas de NIVELES SERVICE ---
log_step "Probando: NIVELES SERVICE"
if [ -z "$TIPO_NIVEL_ID" ] || [ -z "$MAESTRA_ID" ]; then
    echo "❌ ERROR: No se pudieron obtener los IDs necesarios para crear un Nivel. Abortando."
    exit 1
fi

echo "Creando un nuevo Nivel (Técnica Graham)..."
NIVEL_RESPONSE=$(curl --location --request POST "${URL_NIVELES}/niveles" --header 'Content-Type: application/json' --data-raw "{\"nombre\": \"Técnica Graham\", \"rango_edad\": \"Adultos\", \"horario\": \"Sábados 10:00\", \"tipo_nivel_id\": \"$TIPO_NIVEL_ID\", \"maestra_id\": \"$MAESTRA_ID\"}")
echo "Respuesta: $NIVEL_RESPONSE"
NIVEL_ID=$(echo $NIVEL_RESPONSE | jq -r '.id')
echo "✅ ID de Nivel capturado: $NIVEL_ID"

echo ""
echo "Listando todos los niveles..."
curl --location --request GET "${URL_NIVELES}/niveles"
echo ""

echo ""
echo "Obteniendo el nivel recién creado por su ID..."
curl --location --request GET "${URL_NIVELES}/niveles/${NIVEL_ID}"
echo ""

echo ""
echo "Listando niveles por el Tipo 'Danza Contemporánea'..."
curl --location --request GET "${URL_NIVELES}/niveles/tipo/${TIPO_NIVEL_ID}"
echo ""

# --- Pruebas de Asignación de Alumnos ---
log_step "Probando: Asignación de Alumno a Nivel"
echo "Creando un nuevo Alumno (Juan Alumno)..."
ALUMNO_RESPONSE=$(curl --location --request POST "${URL_USERS}/users" --header 'Content-Type: application/json' --data-raw '{"nombre": "Juan Alumno", "rut": "66666666-6", "email": "juan@test.com", "edad": 25, "rol": "Alumno", "sucursal": "Centro"}')
ALUMNO_ID=$(echo $ALUMNO_RESPONSE | jq -r '.id')
echo "✅ ID de Alumno capturado: $ALUMNO_ID"

echo ""
echo "Asignando a Juan Alumno al nivel 'Técnica Graham'..."
curl --location --request POST "${URL_USERS}/users/${ALUMNO_ID}/nivel" --header 'Content-Type: application/json' --data-raw "{\"nivel_id\": \"$NIVEL_ID\"}"
echo ""


log_step "¡PRUEBAS BÁSICAS COMPLETADAS!"
echo "Puedes ejecutar más pruebas manualmente o expandir este script."
echo "Los recursos creados (Niveles, Usuarios, etc.) permanecen en tu LocalStack para que los inspecciones."