from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-functio
    print("welcome/ url is requested & display() is executed");
    #ss ----> is html-data
    ss = '''		
        <center>
            <h2 style="color:Blue;">
            Hello User, Welcome to Django First-Project First-App
            </h2>
            <hr />
            </center>
        ''';

    return HttpResponse(ss);


# Create your views here.

def show(request):
    ss='''
        <html>
            <head>
                <title>***welcome-page***</title>
                <style>
                    h1{color:blue;}
                    h2{color:green;}
                    h3{color:red;}
                    h4{color:orange;}
                    h5{color:pink;}
                    h6{color:violet;}
                    h1,h3,h5{background-color:yellow;}
                    h2,h4,h6{background-color:lightgreen;}
                    
                </style>
            </head>
            <body>
                <center>
                    <h1>welcome to django html webpage</h1>
                    <hr color="brown" width="95%"/>
                    <h2>Welcome to DJANGO HTML webpage</h2>
                    <hr color="brown" width="85%"/>
                    <h3>Welcome to DJANGO HTML webpage</h3>
                    <hr color="brown" width="75%"/>
                    <h4>Welcome to DJANGO HTML webpage</h4>
                    <hr color="brown" width="65%"/>
                    <h5>Welcome to DJANGO HTML webpage</h5>
                    <hr color="brown" width="55%"/>
                    <h6>Welcome to DJANGO HTML webpage</h6>
                    <hr color="brown" width="45%"/>
                    
                </center>
            </body>
        </html>
    '''
    return HttpResponse(ss)
    
def hello(request):
	print("hello/ url is requested & hello() is executed");
	ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightblue;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='60%'/>
				<h3>Have a nice day...</h3>
				<hr color='brown' width='40%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
