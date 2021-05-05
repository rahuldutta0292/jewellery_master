# # -*- encoding: utf-8 -*-
# """
# Copyright (c) 2019 - present AppSeed.us
# """
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django import template
from .models import Customer
from .models import Item
from .models import Order
from .models import Payment
from .models import ItemList
from .forms import CustomerForm
from .forms import ItemForm
from .forms import OrderForm
from .forms import PaymentForm
from .forms import ItemListForm

#
#
# # Create your views here.
#
# def createfile(request):
#     form = FileForm
#     if request.method == 'POST':
#         form = FileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # redirect('home') //redirect to any page you wish to send the user after registration
#     context = {'form': form}
#     return render(request, 'CreateFile.html', context)
#
#
# @login_required(login_url="/signin/")
# def neworder(request, file_id):
#     try:
#         fav_color_ini = 0
#         if 'fav_color' in request.session:
#             fav_color_ini = request.session['fav_color']
#
#         request.session['fav_color'] = fav_color_ini + 1
#         print(fav_color_ini)
#         print(request.user.username)
#         puc_form = PUCForm
#         fileMovementForm = FileMovementForm
#         section_list = Section.objects.all()
#         file_details = File.objects.get(pk=file_id)
#         context = {"section_list": section_list, "file_details": file_details}
#         if request.method == 'POST':
#             # puc_date = request.POST['puc_date']
#             puc_form = PUCForm(request.POST)
#             file_movement_form_input = FileMovementForm(request.POST)
#
#             if puc_form.is_valid() and file_movement_form_input.is_valid():
#                 file_movement = file_movement_form_input.save(commit=False)
#                 file_movement.section_from = Section.objects.get(pk=puc_form.data.get('section'))
#                 file_movement.puc = puc_form.save()
#                 file_movement.save()
#
#                 # redirect('home') //redirect to any page you wish to send the user after registration
#                 context['successMessage'] = f"Successfully Forwarded"
#             else:
#                 for error in puc_form.errors:
#                     print(error)
#                 for error in file_movement_form_input.errors:
#                     print(error)
#
#                 context['errorMessage'] = "Some Error occurred"
#                 print(context)
#         return render(request, 'CreatePUC.html', context)
#     except:
#         return render(request, 'page-500.html')


def order(request):
    form = CustomerForm()
    return render(request, 'Order.html', {'form': form})


def customer(request):
    form = CustomerForm()
    customer_list = Customer.objects.all().order_by('-id')
    context = {"customer_list": customer_list}
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_name = request.POST.get('customer_name')
            date_of_birth = request.POST.get('date_of_birth')
            if not date_of_birth:
                date_of_birth = None
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            if Customer.objects.filter(contact=contact).exists():
                context['customerexistmsg'] = "Customer : "+customer_name+ " already exists."
                return render(request, 'Customer.html', context)
            email = request.POST.get('email')
            pan = request.POST.get('pan')
            customer = Customer(
                customer_name=customer_name,
                date_of_birth=date_of_birth,
                address=address,
                contact=contact,
                email=email,
                pan=pan)
            customer.save()
            context['successmsg'] = "Customer : "+customer_name+" has been added successfully."
            return render(request, 'Customer.html', context)
            # return render(request, "Customer.html", {"successmsg": successmsg})
        else:
            context['errormsg'] = "Some Error Occurred."
        # errormsg = "Some Error Occurred."
            context['form'] = CustomerForm()
        # return redirect('../', successmsg='The Customer '+customer_name+' was added successfully.')
            return render(request, "Customer.html", context)
    return render(request, 'Customer.html', context)


def checkcontact(request):
    if request.is_ajax and request.method == 'GET':
        contact=request.GET.get("contact")
        if Customer.objects.filter(contact=contact).exists():
            customer=Customer.objects.get(contact=contact)
            customer_id=customer.id
            print(customer_id)
            return JsonResponse({"valid": False, "id": customer_id}, status = 200)
        else:
            return JsonResponse({"valid": True}, status = 200)
    return JsonResponse({}, status = 400)


def addcustomer(request):
    successmsg=None
    errormsg=None
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_name = request.POST.get('customer_name')
            date_of_birth = request.POST.get('date_of_birth')
            if not date_of_birth:
                date_of_birth = None
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            email = request.POST.get('email')
            pan = request.POST.get('pan')
            customer = Customer(
                customer_name=customer_name,
                date_of_birth=date_of_birth,
                address=address,
                contact=contact,
                email=email,
                pan=pan)
            customer.save()
            successmsg = "The Customer "+customer_name+" was added successfully."
            return redirect('../')
            # return render(request, "Customer.html", {"successmsg": successmsg})
    else:
        errormsg = "Some Error Occurred."
        form = CustomerForm()
        # return redirect('../', successmsg='The Customer '+customer_name+' was added successfully.')
    return render(request, "Customer.html", {'errormsg': errormsg}, {'form': form})


def changecustomer(request, customer_id):
    form = CustomerForm()
    customer_list = Customer.objects.filter(pk=customer_id) 
    context = {"customer_list": customer_list}
    return render(request, 'EditCustomer.html', context)


def placeorder(request):
    form = CustomerForm(request.POST or None)
    msg=None
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        item_form = ItemForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if customer_form.is_valid() and order_form.is_valid():
            # and order_form_data.is_valid() and  and payment_form.is_valid():
            customer_name = request.POST.get('customer_name')
            date_of_birth = request.POST.get('date_of_birth')
            if not date_of_birth:
                date_of_birth = None
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            email = request.POST.get('email')
            pan = request.POST.get('pan')
            customer = Customer(
                customer_name=customer_name,
                date_of_birth=date_of_birth,
                address=address,
                contact=contact,
                email=email,
                pan=pan)
            customer.save()
            customerid = 10
            created_date = request.POST.get('created_date')
            updated_date = request.POST.get('updated_date')
            delivery_date = request.POST.get('delivery_date')
            order_amount = request.POST.get('order_amount')
            discount = request.POST.get('discount')
            tax_amount = request.POST.get('tax_amount')
            order_details = "order"
            ordered = Order(

                created_date=created_date,
                updated_date=updated_date,
                delivery_date=delivery_date,
                order_amount=order_amount,
                discount=discount,
                tax_amount=tax_amount,
                order_details=order_details)
            ordered.save()

        # if item_form.is_valid():
        #     no_of_item=request.POST.get('no_of_item')
        #     item_names = request.POST.getlist('item_name')
        #     item_descriptions = request.POST.getlist('item_description')
        #     weights = request.POST.getlist('weight')
        #     rate_per_grams = request.POST.getlist('rate_per_gram')
        #     charge_per_grams = request.POST.getlist('charge_per_gram')
        #     making_charges = request.POST.getlist('making_charge')
        #     totals = request.POST.getlist('total')
        #     for i in range(no_of_item):
        #         item=ItemForm({
        #             'item_name': item_names[i],
        #             'item_description': item_descriptions[i],
        #             'weight': weights[i],
        #             'rate_per_gram': rate_per_grams[i],
        #             'charge_per_gram': charge_per_grams[i],
        #             'making_charge': making_charges[i],
        #             'total': totals[i]
        #         })
        #         item.save()

            msg = "Successfully Added"
            # order_form.save
            # item_form.save
            # payment_form.save
            # redirect('home') //redirect to any page you wish to send the user after registration
            # context['successMessage'] = "Successfully Forwarded"
        else:
            msg = "Some Error Occured"
    return render(request, "Order.html", {"msg": msg})


def addorder(request):
    item_list = ItemList.objects.all()
    context = {"item_list": item_list}
    return render(request, 'Order.html', context)


# def neworder(request):
#     form1 = CustomerForm()
#     form2 = ItemListForm()
#     form3 = OrderForm()
#     form4 = ItemForm()
#
#     print(form1)
#     print(form2)
#     print(form3)
#     print(form4)
#
#     return render(request, 'Order.html', {'form1': form1, form2: form2, form3: form3, form4: form4})


def signin_view(request):
    try:
        if 'username' in request.session:
            print("already logged")
            return redirect("/")
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.get(username=username, password=password, section=section)
            print(user)
            request.session['username'] = username
            context = {"username": username, "section": section}
            return redirect("/")
    except:
        print("abc")
        return render(request, 'signin.html')


def signout_view(request):
    print("logot trigger")
    if 'username' in request.session:
        del request.session['username']
    return render(request, 'signin.html')


# @login_required(login_url="/login/")
# @login_required(login_url="/signin/")
def index(request):
    context = {}
    context['segment'] = 'index'
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
