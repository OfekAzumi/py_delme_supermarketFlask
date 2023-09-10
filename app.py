from flask import Flask, render_template, request, send_from_directory
from helper import save_data, load_data

app = Flask(__name__)

market = [
    {"name": "milk", "price": 2.99},
    {"name": "banana", "price": 0.79},
    {"name": "apple", "price": 1.29},
    {"name": "beef", "price": 7.99},
    {"name": "bread", "price": 2.49},
    {"name": "eggs", "price": 1.99},
    {"name": "chicken", "price": 5.99},
    {"name": "rice", "price": 3.49},
    {"name": "lettuce", "price": 0.99},
    {"name": "pasta", "price": 1.79},
    {"name": "tomatoes", "price": 1.49}
]
sum = 0

@app.route('/products')
def process():
    # color = request.args.get('color')
    slc = request.args.get('slc')
    if slc: addToCart(int(slc))
    slc = None
    return render_template('index.html', slc=slc,sum = sumUp(), market = market, cart=cart)

@app.route('/cart')
def shopped():
    global cart,sum
    return render_template('mycart.html',sum=sumUp(), cart=cart)

@app.route('/reset')
def reset():
    global cart, sum
    cart = []
    sum = 0
    return render_template('index.html',slc=None,sum=0, market=market, cart=cart)

@app.route('/about')
def aboutus():
    return render_template('about.html')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('media', filename)

def sumUp():
    if cart:
        sum = 0
        for prd in cart:
            sum+=(prd["price"]*prd["quan"])
        return sum
    else: return 0


def addToCart(iPrd):
    prd = market[iPrd]
    if cart:
        for p in cart: #in case existing in cart
            if(prd["name"] == p["name"]):
                p["quan"]+=1
                return
    #in case cart empty / if new product to existing cart
    cart.append({"name" : prd["name"] , "price" : prd["price"], "quan" : 1}) #add new product to cart



# def mergeDuplicated(arr):
#     tmp = cart
#     final = []
#     for prd in tmp:
#         tname = prd["name"]
#         c = 0
#         for x in cart:
#             if tname == x["name"]: c+=1
#         final.append({"name": tname, "price": (c*prd["price"])})
#         tmp.remove(tname)



if __name__ == '__main__':
    cart = load_data()
    app.run(debug=True)
    save_data(cart)