from flask import Flask,request,render_template
from math import *

app = Flask(__name__)

class Urls:
	index = '/'
	example = '/example'

@app.route(Urls.index)
def index():
	txt = request.args.get('txt')
	try:
		e = eval(txt)
		formulas = str((txt))
		e = str(e)
		return render_template('calc.html',txt=e,formula=formulas)
	except SyntaxError:
		return render_template('calc.html',txt="متاسفم اما فرمول شما استباه است")
	except TypeError:
		return render_template('calc.html')
	except AttributeError:
		return render_template('calc.html')
	except ZeroDivisionError:
		return render_template('calc.html',txt="عدد تقسیم بر صفر تعریف نشده است")
	except NameError:
		return render_template('calc.html',txt="متاسفم اما فرمول شما استباه است")
	except AttributeError:
		pass
	except ValueError:
		return render_template('calc.html',txt="متاسفانه نمی توانید از متن در ماشین حساب استفاده کنید")
		
@app.route(Urls.example)
def example():
	return render_template('example.html')

@app.route(Urls.index+"/<name>")
def handle(name):
	return f"<h2> {name}: is Not Found 404 <a href='/'>خانه</a></h2> <br> <h2> ما آدرس شما پیدا نکردیم </h2>" 

def Counter(n, N):
	count = 0
	n,N = abs(n),abs(N)
	while n <= N:
		N -= n
		count += 1
	return(count)