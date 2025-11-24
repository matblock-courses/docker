"""
API Flask simple pour l'évaluation Docker
"""
from flask import Flask, jsonify, request
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Configuration depuis les variables d'environnement
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'myapp')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')

def get_db_connection():
    """Connexion à PostgreSQL"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Erreur de connexion DB: {e}")
        return None

@app.route('/')
def home():
    """Page d'accueil de l'API"""
    return jsonify({
        'message': 'Bienvenue sur mon API Flask!',
        'version': '1.0',
        'endpoints': ['/health', '/api/info', '/api/db-test']
    })

@app.route('/health')
def health():
    """Endpoint de santé"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/info')
def info():
    """Informations sur l'application"""
    return jsonify({
        'app': 'Flask API',
        'python_version': os.sys.version,
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'db_host': DB_HOST
    })

@app.route('/api/db-test')
def db_test():
    """Test de connexion à la base de données"""
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute('SELECT version();')
            db_version = cur.fetchone()
            cur.close()
            conn.close()
            return jsonify({
                'status': 'success',
                'database': 'connected',
                'version': db_version[0]
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500
    else:
        return jsonify({
            'status': 'error',
            'message': 'Impossible de se connecter à la base de données'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)