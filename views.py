from django.shortcuts import render
from django.db import connection
from .models import *
from django.db.models import Count, Min, Sum, Avg

# Create your views here.
from django.http import HttpResponse
import json

def index(request):
	return render(request,'index.html',{})

def q1(request,start_date,days):
	cur = connection.cursor()
	cur.callproc('q1', [start_date,days])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q2(request,size,typ,name):
	typ=typ.replace('_',' ')
	cur = connection.cursor()
	cur.callproc('q2', [size,typ,name])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q3(request,mktsegment,orderdate):
	cur = connection.cursor()
	cur.callproc('q3', [mktsegment,orderdate])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q4(request,order_date):
	cur = connection.cursor()
	cur.callproc('q4', [order_date])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))
	
def q5(request,region_name,order_date):
	cur = connection.cursor()
	cur.callproc('q5', [region_name,order_date])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q6(request,ship_date,discount,quantity):
	cur = connection.cursor()
	cur.callproc('q6', [ship_date,discount,quantity])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))
	
def q7(request,n_name1,n_name2):
	cur = connection.cursor()
	cur.callproc('q7', [n_name1,n_name2])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))
	
def q8(request,n_name,r_name,p_type):
	p_type=p_type.replace('_',' ')
	cur = connection.cursor()
	cur.callproc('q8', [n_name,r_name,p_type])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))
	
def q9(request,p_name):
	p_name=p_name.replace('_',' ')
	cur = connection.cursor()
	cur.callproc('q9', [p_name])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q10(request,order_date):
	cur = connection.cursor()
	cur.callproc('q10', [order_date])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q11(request,name,per):
	cur = connection.cursor()
	cur.callproc('q11', [name,per])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q12(request,shm1,shm2,receipt_date):
	shm1=shm1.replace('_',' ')
	shm2=shm2.replace('_',' ')
	cur = connection.cursor()
	cur.callproc('q12', [shm1,shm2,receipt_date])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q13(request,word1,word2):
	cur = connection.cursor()
	cur.callproc('q13', [word1,word2])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q14(request,ship_date):
	cur = connection.cursor()
	cur.callproc('q14', [ship_date])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q15(request,ship_date):
	cur = connection.cursor()
	cur.callproc('q15', [ship_date])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q16(request,ptype,pbrand,psize):
	ptype=ptype.replace('_',' ')
	pbrand=pbrand.replace('-','#')
	cur = connection.cursor()
	cur.callproc('q16_1', [ptype,pbrand,psize])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q17(request,pbrand,pcontainer):
	pcontainer=pcontainer.replace('_',' ')
	pbrand=pbrand.replace('-','#')
	cur = connection.cursor()
	cur.callproc('q17_1', [pbrand,pcontainer])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q18(request,quantity):
	cur = connection.cursor()
	cur.callproc('q18', [quantity])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q19(request,brand1,quantity1,brand2,quantity2,brand3,quantity3):
	brand1=brand1.replace('-','#')
	brand2=brand2.replace('-','#')
	brand3=brand3.replace('-','#')
	cur = connection.cursor()
	cur.callproc('q19', [brand1,brand2,brand3,quantity1,quantity2,quantity3])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))

def q20(request,p_name,ship_date,n_name):
	cur = connection.cursor()
	cur.callproc('q20_1', [p_name,ship_date,n_name])
	results = cur.fetchall()[0][0]
	cur.close()
	return HttpResponse(json.dumps(results))
	
def indexQ1(request):
	return render(request,'indexQ1.html',{})

def indexQ2(request):
	p=Part.objects.values("p_size","p_type").distinct()
	plist={}
	plist=[(i['p_size'],i['p_type']) for i in p]
	plist.sort(key=lambda x:(x[0],x[1]))
	r=Region.objects.values("r_name").distinct()
	rlist=[i['r_name'] for i in r]
	rlist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ2.html',{'plist':plist,'region':rlist})

def indexQ3(request):
	mktseg=Customer.objects.values("c_mktsegment").distinct()
	mlist=[]
	mlist.extend([i['c_mktsegment'] for i in mktseg])
	mlist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ3.html',{'mlist':mlist})

def indexQ4(request):
	return render(request,'indexQ4.html',{})

def indexQ5(request):
	r=Region.objects.values("r_name").distinct()
	rlist=[i['r_name'] for i in r]
	rlist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ5.html',{'region':rlist})

def indexQ6(request):
	return render(request,'indexQ6.html',{})

def indexQ7(request):
	n_names=Nation.objects.values('n_name').distinct()
	nlist=[i['n_name'] for i in n_names]
	nlist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ7.html',{'nlist':nlist})

def indexQ8(request):
	n_names=Nation.objects.values('n_name').distinct()
	nlist=[i['n_name'] for i in n_names]
	nlist.sort(cmp=lambda x,y:cmp(x,y))
	r=Region.objects.values("r_name").distinct()
	rlist=[i['r_name'] for i in r]
	rlist.sort(cmp=lambda x,y:cmp(x,y))
	p=Part.objects.values("p_type").distinct()
	plist=[i['p_type'] for i in p]
	plist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ8.html',{'nlist':nlist,'rlist':rlist,'plist':plist})
		
def indexQ9(request):
	p_names=Part.objects.values('p_name').distinct()
	plist=[i['p_name'] for i in p_names]
	plist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ9.html',{'plist':plist})

def indexQ10(request):
	return render(request,'indexQ10.html',{})

def indexQ11(request):
	n_names=Nation.objects.values('n_name').distinct()
	nlist=[i['n_name'] for i in n_names]
	nlist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ11.html',{'nlist':nlist})

def indexQ12(request):
	shipmodes=Lineitem.objects.values('l_shipmode').distinct()
	nlist=[i['l_shipmode'] for i in shipmodes]
	nlist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ12.html',{'nlist':nlist})

def indexQ13(request):
	return render(request,'indexQ13.html',{})

def indexQ14(request):
	return render(request,'indexQ14.html',{})

def indexQ15(request):
	return render(request,'indexQ15.html',{})

def indexQ16(request):
	pt=Part.objects.values("p_type").distinct()
	ptlist=(i['p_type'] for i in pt)
	ptlist=list(set((' '.join(i.split(' ')[:-1]) for i in ptlist)))
	ptlist.sort(cmp=lambda x,y:cmp(x,y))
	ps=Part.objects.values("p_size").distinct()
	pslist=list(set([i['p_size'] for i in ps]))
	pslist.sort(cmp=lambda x,y:cmp(x,y))
	pb=Part.objects.values("p_brand").distinct()
	pblist=[i['p_brand'] for i in pb]
	pblist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ16.html',{"ptlist":ptlist,"pslist":pslist,"pblist":pblist})

def indexQ17(request):
	pb=Part.objects.values("p_brand").distinct()
	pblist=[i['p_brand'] for i in pb]
	pblist.sort(cmp=lambda x,y:cmp(x,y))
	pc=Part.objects.values("p_container").distinct()
	pclist=[i['p_container'] for i in pc]
	pclist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ17.html',{"pblist":pblist,"pclist":pclist})

def indexQ18(request):
	qu=Lineitem.objects.values('l_orderkey').annotate(Sum('l_quantity'))
	qulist=[i['l_quantity__sum'] for i in qu]
	return render(request,'indexQ18.html',{"qulist":(min(qulist)-1,max(qulist)-1)})

def indexQ19(request):
	pb=Part.objects.values("p_brand").distinct()
	pblist=[i['p_brand'] for i in pb]
	pblist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ19.html',{"pblist":pblist})

def indexQ20(request):
	pn=Part.objects.values("p_name").distinct()
	pnlist=list(set([i['p_name'].split(' ')[0] for i in pn]))
	pnlist.sort(cmp=lambda x,y:cmp(x,y))
	nn=Nation.objects.values("n_name").distinct()
	nnlist=[i['n_name'] for i in nn]
	nnlist.sort(cmp=lambda x,y:cmp(x,y))
	return render(request,'indexQ20.html',{"pnlist":pnlist,"nnlist":nnlist})