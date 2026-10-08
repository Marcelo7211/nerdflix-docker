"""API simples da loja de filmes Nerdflix (Flask + MySQL).

A conexão com o banco vem de variáveis de ambiente, então o mesmo código roda
no computador, em um container e em um cluster Swarm sem nenhuma alteração.
"""
import os
import socket

import pymysql
from flask import Flask, jsonify, request

VERSAO = "1.0"

app = Flask(__name__)


def conectar():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "loja"),
        password=os.environ.get("DB_PASSWORD", ""),
        database=os.environ.get("DB_NAME", "loja"),
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5,
    )


@app.get("/api/saude")
def saude():
    # Mostra qual container respondeu (útil para ver as réplicas do Swarm)
    return jsonify({"status": "ok", "host": socket.gethostname(), "versao": VERSAO})


@app.get("/api/filmes")
def listar_filmes():
    try:
        with conectar() as conexao, conexao.cursor() as cursor:
            cursor.execute("SELECT id, titulo, ano FROM filmes ORDER BY id")
            return jsonify(cursor.fetchall())
    except pymysql.MySQLError as erro:
        return jsonify({"erro": "Não consegui falar com o banco de dados", "detalhe": str(erro)}), 503


@app.post("/api/filmes")
def criar_filme():
    dados = request.get_json(silent=True) or {}
    titulo = str(dados.get("titulo", "")).strip()
    ano = dados.get("ano")
    if not titulo or not isinstance(ano, int):
        return jsonify({"erro": "Informe titulo (texto) e ano (número)"}), 400
    try:
        with conectar() as conexao, conexao.cursor() as cursor:
            cursor.execute("INSERT INTO filmes (titulo, ano) VALUES (%s, %s)", (titulo, ano))
            conexao.commit()
            return jsonify({"id": cursor.lastrowid, "titulo": titulo, "ano": ano}), 201
    except pymysql.MySQLError as erro:
        return jsonify({"erro": "Não consegui falar com o banco de dados", "detalhe": str(erro)}), 503


if __name__ == "__main__":
    # Servidor de desenvolvimento: suficiente para estudar Docker
    app.run(host="0.0.0.0", port=5000)
