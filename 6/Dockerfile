# ベースイメージを指定
FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /app

# ホストのファイルをコンテナにコピー
COPY src/ /app

# 必要なパッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナを起動する際に実行されるコマンド
CMD ["python", "your_script.py"]