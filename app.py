from flask import Flask, render_template_string, url_for, request, session, redirect

app = Flask(__name__)
app.secret_key = "chave_secreta_super_segura"

produtos = [
    {"nome": "Dipirona 500mg", "preco": "R$ 9,90", "imagem": "dipirona.webp", "categoria": "med"},
    {"nome": "Paracetamol", "preco": "R$ 12,50", "imagem": "paracetamol.webp", "categoria": "med"},
    {"nome": "Vitamina C", "preco": "R$ 24,90", "imagem": "vitamina.webp", "categoria": "med"},
    {"nome": "Protetor Solar Nivea", "preco": "R$ 49,90", "imagem": "protetor.webp", "categoria": "cos"},
    {"nome": "shampoo nivea", "preco": "R$ 18,90", "imagem": "shampool.webp", "categoria": "hig"},
    {"nome": "Sabonete Francis", "preco": "R$ 3,99", "imagem": "francis.webp", "categoria": "hig"},
]

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Farmácia Pollo</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, Helvetica, sans-serif;
}
.produto{
    width:170px;
    height:170px;
    object-fit:contain;
    margin-bottom:15px;
}

body{
    background:#f5f5f5;
}

header{
    background:#d50000;
    color:white;
    padding:20px 60px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.logo{
    display:flex;
    align-items:center;
    gap:15px;
    font-size:30px;
    font-weight:bold;
    color:white;
}

.logo img{
    width:60px;
    height:60px;
    object-fit:contain;
    border-radius:8px;
}
nav a{
    color:white;
    text-decoration:none;
    margin-left:20px;
    font-size:18px;
}

.banner{
    background:white;
    padding:80px;
    text-align:center;
}

.banner h1{
    color:#d50000;
    font-size:55px;
}

.banner p{
    margin-top:15px;
    font-size:22px;
}

input{
    width:400px;
    padding:14px;
    margin-top:30px;
    border:2px solid #d50000;
    border-radius:8px;
    font-size:18px;
}

button{
    padding:14px 25px;
    background:#d50000;
    color:white;
    border:none;
    border-radius:8px;
    cursor:pointer;
    font-size:18px;
}

button:hover{
    background:#b30000;
}

h2{
    text-align:center;
    color:#d50000;
    margin-top:40px;
    margin-bottom:20px;
    font-size:38px;
}

.produto img{
    width:180px;
    height:180px;
    object-fit:contain;
    display:block;
    margin:0 auto 15px;
}

.card{
    background:white;
    border-radius:15px;
    text-align:center;
    padding:25px;
    box-shadow:0 0 15px rgba(0,0,0,.15);
    transition:.3s;
}

.card:hover{
    transform:translateY(-8px);
}

.icone{
    font-size:70px;
}

.card h3{
    margin:20px 0;
}

.preco{
    color:#d50000;
    font-size:24px;
    font-weight:bold;
    margin-bottom:20px;
}

footer{
    margin-top:50px;
    background:#d50000;
    color:white;
    text-align:center;
    padding:20px;
}

</style>

</head>

<body>

<header>

<div class="logo">
    <img src="/static/logo.webp" alt="Logo Farmácia Pollo">
    <span>Farmácia Pollo</span>
</div>

<nav>
<a href="#">inicio</a>
<a href="med">Medicamentos</a>
<a href="hig">Higiene</a>
<a href="cos">Cosméticos</a>
<a href="cont">Contato</a>
</nav>

</header>

<section class="banner">
    <h1>Farmácia Pollo mais econômica!</h1>
    <p>Sua saúde em primeiro lugar.</p>
    
    <form action="/" method="GET">
        <input type="text" name="q" placeholder="Pesquisar medicamento...">
        <button type="submit">Pesquisar</button>
    </form>
</section>

<h2>Produtos em Destaque</h2>

<section class="produtos">

{% for p in produtos %}

<div class="card">

<img src="{{ url_for('static', filename=p.imagem) }}" class="produto">

<h3>{{p.nome}}</h3>

<div class="preco">{{p.preco}}</div>

<a href="/adicionar/{{ p.nome }}" style="text-decoration: none;">
    <button type="button">Comprar</button>
</a>

</div>

{% endfor %}

</section>

<footer>

<h3>Farmácia Pollo</h3>

<p>📍 Avenida londrina, 1000</p>

<p>📞 (44) 99943-3016</p>

<p>✉ contato@farmaciapollo.com.br</p>

<br>

<p>© 2026 - Todos os direitos reservados.</p>

</footer>

</body>

</html>
"""

HTML_MEDICAMENTOS = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Medicamentos - Farmácia Pollo</title>
    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, Helvetica, sans-serif;
        }
        body{
            background:#f5f5f5;
        }
        header{
            background:#d50000;
            color:white;
            padding:20px 60px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }
        .logo{
            display:flex;
            align-items:center;
            gap:15px;
            font-size:30px;
            font-weight:bold;
        }
        .logo img{
            width:60px;
            height:60px;
            object-fit:contain;
            border-radius:8px;
        }
        nav a{
            color:white;
            text-decoration:none;
            font-size:18px;
        }
        h2{
            text-align:center;
            color:#d50000;
            margin-top:40px;
            margin-bottom:20px;
            font-size:38px;
        }
        .produtos {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            padding: 20px;
        }
        .produto{
            width:170px;
            height:170px;
            object-fit:contain;
            margin-bottom:15px;
        }
        .card{
            background:white;
            border-radius:15px;
            text-align:center;
            padding:25px;
            box-shadow:0 0 15px rgba(0,0,0,.15);
            transition:.3s;
            width: 250px;
        }
        .preco{
            color:#d50000;
            font-size:24px;
            font-weight:bold;
            margin-bottom:20px;
        }
        button{
            padding:14px 25px;
            background:#d50000;
            color:white;
            border:none;
            border-radius:8px;
            cursor:pointer;
            font-size:18px;
        }
        footer{
            margin-top:350px;
            background:#d50000;
            color:white;
            text-align:center;
            padding:20px;
        }
    </style>
</head>
<body>

<header>
    <div class="logo">
        <img src="/static/logo.webp" alt="Logo Farmácia Pollo">
        <span>Farmácia Pollo</span>
    </div>
    <nav>
      <a href="/">Início</a>
    <nav>
</header>

<h2>Setor de Medicamentos</h2>

<section class="produtos">
    {% for p in produtos %}
    <div class="card">
        <img src="{{ url_for('static', filename=p.imagem) }}" class="produto">
        <h3>{{ p.nome }}</h3>
        <div class="preco">{{ p.preco }}</div>
        <button>Comprar</button>
    </div>
    {% else %}
    <p>Nenhum medicamento encontrado.</p>
    {% endfor %}
</section>

<footer>

h3>Farmácia Pollo</h3>

<p>📍 Avenida londrina, 1000</p>

<p>📞 (44) 99943-3016</p>

<p>✉ contato@farmaciapollo.com.br</p>

<p>© 2026 - Todos os direitos reservados.</p>

<br>

<footer>

</body>
</html>
"""

HTML_HIGIENE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Higiene - Farmácia Pollo</title>
    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, Helvetica, sans-serif;
        }
        body{
            background:#f5f5f5;
        }
        header{
            background:#d50000;
            color:white;
            padding:20px 60px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }
        .logo{
            display:flex;
            align-items:center;
            gap:15px;
            font-size:30px;
            font-weight:bold;
        }
        .logo img{
            width:60px;
            height:60px;
            object-fit:contain;
            border-radius:8px;
        }
        nav a{
            color:white;
            text-decoration:none;
            font-size:18px;
        }
        h2{
            text-align:center;
            color:#d50000;
            margin-top:40px;
            margin-bottom:20px;
            font-size:38px;
        }
        .produtos {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            padding: 20px;
        }
        .produto{
            width:170px;
            height:170px;
            object-fit:contain;
            margin-bottom:15px;
        }
        .card{
            background:white;
            border-radius:15px;
            text-align:center;
            padding:25px;
            box-shadow:0 0 15px rgba(0,0,0,.15);
            transition:.3s;
            width: 250px;
        }
        .preco{
            color:#d50000;
            font-size:24px;
            font-weight:bold;
            margin-bottom:20px;
        }
        button{
            padding:14px 25px;
            background:#d50000;
            color:white;
            border:none;
            border-radius:8px;
            cursor:pointer;
            font-size:18px;
        }
        footer{
            margin-top:350px;
            background:#d50000;
            color:white;
            text-align:center;
            padding:20px;
        }
    </style>
</head>
<body>

<header>
    <div class="logo">
        <img src="/static/logo.webp" alt="Logo Farmácia Pollo">
        <span>Farmácia Pollo</span>
    </div>
    <nav>
      <a href="/">Início</a>
    <nav>
</header>

<h2>Setor de Higiene</h2>

<section class="produtos">
    {% for p in produtos %}
    <div class="card">
        <img src="{{ url_for('static', filename=p.imagem) }}" class="produto">
        <h3>{{ p.nome }}</h3>
        <div class="preco">{{ p.preco }}</div>
        <button>Comprar</button>
    </div>
    {% else %}
    <p>Nenhum produto de higiene encontrado.</p>
    {% endfor %}
</section>

<footer>

h3>Farmácia Pollo</h3>

<p>📍 Avenida londrina, 1000</p>

<p>📞 (44) 99943-3016</p>

<p>✉ contato@farmaciapollo.com.br</p>

<p>© 2026 - Todos os direitos reservados.</p>

<br>

<footer>

</body>
</html>
"""

HTML_cosmeticos = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cosméticos - Farmácia Pollo</title>
    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, Helvetica, sans-serif;
        }
        body{
            background:#f5f5f5;
        }
        header{
            background:#d50000;
            color:white;
            padding:20px 60px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }
        .logo{
            display:flex;
            align-items:center;
            gap:15px;
            font-size:30px;
            font-weight:bold;
        }
        .logo img{
            width:60px;
            height:60px;
            object-fit:contain;
            border-radius:8px;
        }
        nav a{
            color:white;
            text-decoration:none;
            font-size:18px;
        }
        h2{
            text-align:center;
            color:#d50000;
            margin-top:40px;
            margin-bottom:20px;
            font-size:38px;
        }
        .produtos {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            padding: 20px;
        }
        .produto{
            width:170px;
            height:170px;
            object-fit:contain;
            margin-bottom:15px;
        }
        .card{
            background:white;
            border-radius:15px;
            text-align:center;
            padding:25px;
            box-shadow:0 0 15px rgba(0,0,0,.15);
            transition:.3s;
            width: 250px;
        }
        .preco{
            color:#d50000;
            font-size:24px;
            font-weight:bold;
            margin-bottom:20px;
        }
        button{
            padding:14px 25px;
            background:#d50000;
            color:white;
            border:none;
            border-radius:8px;
            cursor:pointer;
            font-size:18px;
        }
        footer{
            margin-top:350px;
            background:#d50000;
            color:white;
            text-align:center;
            padding:20px;
        }
    </style>
</head>
<body>

<header>
    <div class="logo">
        <img src="/static/logo.webp" alt="Logo Farmácia Pollo">
        <span>Farmácia Pollo</span>
    </div>
    <nav>
      <a href="/">Início</a>
    <nav>
</header>

<h2>Setor de Cosméticos</h2>

<section class="produtos">
    {% for p in produtos %}
    <div class="card">
        <img src="{{ url_for('static', filename=p.imagem) }}" class="produto">
        <h3>{{ p.nome }}</h3>
        <div class="preco">{{ p.preco }}</div>
        <button>Comprar</button>
    </div>
    {% else %}
    <p>Nenhum cosmético encontrado.</p>
    {% endfor %}
</section>

<footer>

h3>Farmácia Pollo</h3>

<p>📍 Avenida londrina, 1000</p>

<p>📞 (44) 99943-3016</p>

<p>✉ contato@farmaciapollo.com.br</p>

<p>© 2026 - Todos os direitos reservados.</p>

<br>

<footer>

</body>
</html>
"""

HTML_contato = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Contato - Farmácia Pollo</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, Helvetica, sans-serif;
}

header{
    background:#d50000;
    color:white;
    padding:20px 60px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.logo{
    display:flex;
    align-items:center;
    gap:15px;
    font-size:30px;
    font-weight:bold;
    color:white;
}

.logo img{
    width:60px;
    height:60px;
    object-fit:contain;
    border-radius:8px;
}
nav a{
    color:white;
    text-decoration:none;
    margin-left:20px;
    font-size:18px;
}

h2{
    text-align:center;
    color:#d50000;
    margin-top:40px;
    margin-bottom:20px;
    font-size:38px;
}

.informacoes-contato {
    text-align: center;
    font-size: 20px;
    margin-top: 30px;
    line-height: 1.8;
}


footer{
    margin-top:600px;
    background:#d50000;
    color:white;
    text-align:center;
    padding:20px;
}
</style>
</head>
<body>

<header>
<div class="logo">
    <img src="/static/logo.webp" alt="Logo Farmácia Pollo">
    <span>Farmácia Pollo</span>
</div>
<nav>
    <a href="/">Início</a>
</nav>
</header>

<h2>Entre em Contato Conosco</h2>

<div class="informacoes-contato">
    <p>📍 Avenida Londrina, 1283, Sarandi, Paraná, 87114-010</p>
    <p>📞 <a href="https://wa.me/5544999733016" target="_blank">Fale conosco no WhatsApp</a></p>
    <p>✉ contato@farmaciapollo.com.br</p>

</section>

<footer>

h3>Farmácia Pollo</h3>

<p>📍 Avenida londrina, 1000</p>

<p>📞 (44) 99943-3016</p>

<p>✉ contato@farmaciapollo.com.br</p>

<p>© 2026 - Todos os direitos reservados.</p>

<br>

<footer>

</div>

</footer> </body>
</html>
"""

HTML_CARRINHO = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Meu Carrinho - Farmácia Pollo</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 40px; text-align: center;}
        .container { background: white; padding: 30px; border-radius: 15px; max-width: 600px; margin: 0 auto; box-shadow: 0 0 15px rgba(0,0,0,0.1); }
        h1 { color: #d50000; }
        ul { list-style: none; padding: 0; text-align: left; margin: 20px 0; }
        li { padding: 10px; border-bottom: 1px solid #ddd; display: flex; justify-content: space-between; }
        .btn { display: inline-block; padding: 10px 20px; background: #d50000; color: white; text-decoration: none; border-radius: 5px; margin-top: 20px; }
        .btn-voltar { background: #555; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Seu Carrinho de Compras</h1>
        {% if itens %}
            <ul>
            {% for item in itens %}
                <li><span>🛒 {{ item.nome }}</span> <strong>{{ item.preco }}</strong></li>
            {% endfor %}
            </ul>
            <a href="#" class="btn" onclick="alert('Integração de pagamento simulada com sucesso!')">Finalizar Compra</a>
        {% else %}
            <p>Seu carrinho está vazio.</p>
        {% endif %}
        <br>
        <a href="/" class="btn btn-voltar">Continuar Comprando</a>
    </div>
</body>
</html>
"""
@app.route("/")
def home():
    termo_pesquisa = request.args.get('q', '').strip().lower()

    if termo_pesquisa:
        produtos_exibidos = [p for p in produtos if termo_pesquisa in p['nome'].lower()]
    else:
        produtos_exibidos = produtos

    return render_template_string(HTML, produtos=produtos_exibidos)

@app.route("/med")
def pagina_med():
    med_lista = [p for p in produtos if p["categoria"] == "med"]
    return render_template_string(HTML_MEDICAMENTOS, produtos=med_lista)

@app.route("/hig")
def pagina_hig():
    hig_lista = [p for p in produtos if p["categoria"] == "hig"]
    return render_template_string(HTML_HIGIENE, produtos=hig_lista)

@app.route("/cos")
def pagina_cos():

    cos_lista = [p for p in produtos if p['categoria'] == 'cos']
    return render_template_string(HTML_cosmeticos, produtos=cos_lista)

@app.route("/cont")
def pagina_cont():
    return render_template_string(HTML_contato)


@app.route("/adicionar/<nome_produto>")
def adicionar_carrinho(nome_produto):
    # Se o carrinho não existir na sessão do usuário, cria uma lista vazia
    if 'carrinho' not in session:
        session['carrinho'] = []

    # Procura o produto completo na sua lista original
    produto_encontrado = next((p for p in produtos if p['nome'] == nome_produto), None)

    if produto_encontrado:
        # Adiciona o produto ao carrinho
        carrinho_atual = session['carrinho']
        carrinho_atual.append(produto_encontrado)
        session['carrinho'] = carrinho_atual  # Salva as alterações na sessão

    return redirect(url_for('exibir_carrinho'))


# --- ROTA PARA VER O CARRINHO ---
@app.route("/carrinho")
def exibir_carrinho():
    itens_carrinho = session.get('carrinho', [])

    return render_template_string(HTML_CARRINHO, itens=itens_carrinho)



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)