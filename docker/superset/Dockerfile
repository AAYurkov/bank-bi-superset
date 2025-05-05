# Базируемся на официальном multi‑arch образе
FROM apache/superset:latest

# Устанавливаем драйвер ClickHouse (pure‑python → работает и на ARM64)
USER root
RUN pip install --no-cache-dir "clickhouse-connect~=0.7"

# (опционально) дополнительные пакеты, темы, плагины
# RUN pip install superset-ml-plugin==0.3.0

# возвращаем права
USER superset