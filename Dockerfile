# ベースイメージ
FROM python:3.11

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のコピーとインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt



# アプリケーションコードのコピー
COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate
# ポート公開
EXPOSE 8000

# デフォルトのコマンドをgunicornでアプリケーションを起動
CMD ["gunicorn", "todo.wsgi:application", "--bind", "0.0.0.0:8000"]