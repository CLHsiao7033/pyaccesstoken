#!/bin/bash
echo "========== ========== =========="
az account show
echo "========== ========== =========="
gunicorn -w 2 -b ${SERVICE_IP}:${SERVICE_PORT} main:app
echo "========== ========== =========="
