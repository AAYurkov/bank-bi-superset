#!/usr/bin/env bash
set -e

echo "⏳ Инициализируем Superset ..."

superset db upgrade

superset fab create-admin \
    --username "$ADMIN_USER" \
    --firstname Superset \
    --lastname Admin \
    --email "$ADMIN_EMAIL" \
    --password "$ADMIN_PWD" || true

superset init
echo "✅ Superset готов! — http://localhost:8088 (login: $ADMIN_USER / $ADMIN_PWD)"