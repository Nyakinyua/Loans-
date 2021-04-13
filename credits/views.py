from django.shortcuts import render
from .models import *
from .forms import LoanForm
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.


def index(request):
    all_customers = Customer.get_customers()
    return render(request,"index.html",{"customers":all_customers})

def Payment(principal,rate,no_of_periods):
    if rate == 0:
        periodic_payment = principal/no_of_periods
    else:
        monthly_interest_rate = rate/12
        periodic_payment = principal*(monthly_interest_rate/((1+monthly_interest_rate)**number_of_periods - 1)))

    return periodic_payment

def Loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Gather and sanitize inputs
            amount_borrowed = form.cleaned_data['amount_borrowed']
            repayment = form.cleaned_data['repayment']
            int_rate = form.cleaned_data['interest_rate']
            installments = form.cleaned_data['installments']
            
            # Calculated Values
            company_principle = amount_borrowed + repayment

            # Monthly Payment calculations
            company_monthly_payment = Payment(company_principle,rate,installments)

            # Total Calculations
            company_total_amount = company_monthly_payment + installments

            # Interest calculations
             company_total_interest_Ksh = round(Decimal(company_total_amount) - company_principle, 2) #

            #  Calculation
            int_rate = round(company_apr * 100, 4)

             # Return values to HTML page
            # Ksh amounts are formatted to exactly two decimal places
            return render(request, 'loan.html', {'form': form,
                                                 'company_total_amount': Decimal('%.2f' % company_total_amount),
                                                 'company_total_interest_Ksh': Decimal('%.2f' % company_total_interest_Ksh),
                                                 'company_monthly_payment': Decimal('%.2f' % company_monthly_payment),
                                                 'real_company_interest_rate': company_apr})
    else:
        form = LoanForm()
    return render(request, 'loan.html', {'form': form})



 
