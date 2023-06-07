from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/MeuEstoque"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Defina a chave secreta
app.secret_key = "your_secret_key"

# Cria a instância do SQLAlchemy com o app
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    supplier = db.Column(db.String(100))
    purchase_price = db.Column(db.Float, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)

    category = db.relationship("Category", backref=db.backref("products", lazy=True))

    def __repr__(self):
        return self.name


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/categorias", methods=["GET"])
def categorias():
    categories = Category.query.all()
    return render_template("categorias.html", categories=categories)

@app.route("/incluir_categoria", methods=["POST"])
def incluir_categoria():
    name = request.form["name"]
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    flash("Categoria adicionada com sucesso!", "success")
    return redirect(url_for("categorias"))



@app.route("/editar_categoria/<int:categoria_id>", methods=["GET", "POST"])
def editar_categoria(categoria_id):
    categoria = Category.query.get_or_404(categoria_id)

    if request.method == "POST":
        categoria.name = request.form["name"]
        db.session.commit()
        flash("Categoria atualizada com sucesso!", "success")
        return redirect(url_for("categorias"))
    else:
        return render_template("editar_categoria.html", categoria=categoria)

    
@app.route("/excluir_categoria/<int:categoria_id>", methods=["GET", "POST"])
def excluir_categoria(categoria_id):
    categoria = Category.query.get_or_404(categoria_id)
    db.session.delete(categoria)
    db.session.commit()
    flash("Categoria excluída com sucesso!", "success")
    return redirect(url_for("categorias"))


@app.route("/estoque")
def estoque():
    products = Product.query.order_by(Product.name).all()
    return render_template("estoque.html", products=products)


@app.route("/novo_produto", methods=["GET", "POST"])
def novo_produto():
    if request.method == "POST":
        name = request.form["name"]
        category_id = int(request.form["category"])
        quantity = int(request.form["quantity"])
        supplier = request.form["supplier"]
        purchase_price = float(request.form["purchase_price"])
        sale_price = float(request.form["sale_price"])

        product = Product(
            name=name,
            category_id=category_id,
            quantity=quantity,
            supplier=supplier,
            purchase_price=purchase_price,
            sale_price=sale_price,
        )
        db.session.add(product)
        db.session.commit()
        flash("Produto adicionado com sucesso!", "success")
        return redirect(url_for("estoque"))
    else:
        categories = Category.query.all()
        return render_template("novo_produto.html", categories=categories)


@app.route("/editar_produto/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    product = Product.query.get_or_404(id)

    if request.method == "POST":
        product.name = request.form["name"]
        product.category_id = int(request.form["category"])
        product.quantity = int(request.form["quantity"])
        product.supplier = request.form["supplier"]
        product.purchase_price = float(request.form["purchase_price"])
        product.sale_price = float(request.form["sale_price"])

        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for("estoque"))
    else:
        categories = Category.query.all()
        return render_template(
            "editar_produto.html", product=product, categories=categories
        )


@app.route("/excluir_produto/<int:id>", methods=["GET", "POST"])
def excluir_produto(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash("Produto excluído com sucesso!", "success")
    return redirect(url_for("estoque"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)