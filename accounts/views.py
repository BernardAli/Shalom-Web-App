import csv

from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.forms import CashFlowCreateForm, CashFlowUpdateForm, InflowForm, OutflowForm, CashFlowHistorySearchForm, \
    CashHistorySearchForm, IssueCashForm, ReceiveCashForm
from accounts.models import Category, CashFlow, CashFlowHistory, CashHistory, Cash
from core.models import Family, Auxiliaries, Ministries
from authy.models import User, Profile

from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from mysite.settings import EMAIL_HOST_USER


# Create your views here.


def accounts_home(request):
    member_count = User.objects.all().count()
    family_count = Family.objects.all().count()
    auxiliary_count = Auxiliaries.objects.all().count()
    ministry_count = Auxiliaries.objects.all().count()
    cash_flow = CashFlow.objects.all()
    cash_flow_items = CashFlowHistory.objects.all().order_by('-created_on')[:5]
    context = {
        "member_count": member_count,
        "family_count": family_count,
        'auxiliary_count': auxiliary_count,
        'ministry_count': ministry_count,
        'cash_flow': cash_flow,
        'cash_flow_items': cash_flow_items
    }
    return render(request, 'accounts/home.html', context)


def members(request):
    members = Profile.objects.all()
    context = {
        'members': members
    }
    return render(request, 'accounts/member_list.html', context)


def member_details(request, id):
    member = Profile.objects.get(id=id)
    payments = CashFlowHistory.objects.filter(received_from=member)
    context = {
        'member': member,
        'payments': payments
    }
    return render(request, 'accounts/member_details.html', context)


class CategoryListView(ListView):
    template_name = 'accounts/category_list.html'
    model = Category
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'accounts/category_details.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'accounts/category_create.html'
    fields = "__all__"
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'accounts/category_create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'accounts/category_delete.html'
    success_url = reverse_lazy("category_list")


def list_item(request):
    queryset = CashFlow.objects.all()
    context = {
        "queryset": queryset,
    }
    return render(request, "accounts/list_item.html", context)


def cashflow_detail(request, pk):
    queryset = CashFlow.objects.get(id=pk)
    context = {
        "queryset": queryset,
    }
    return render(request, "accounts/cashflow_detail.html", context)


def add_items(request):
    form = CashFlowCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('list_items')
    context = {
        "form": form,
    }
    return render(request, "accounts/add_item.html", context)


def update_items(request, pk):
    queryset = CashFlow.objects.get(id=pk)
    form = CashFlowUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CashFlowUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('list_items')

    context = {
        'form': form
    }
    return render(request, 'accounts/add_item.html', context)


def inflows_items(request, pk):
    queryset = CashFlow.objects.get(id=pk)
    form = InflowForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.amount <= 0:
            messages.success(request, "Amount can not be equal or less than zero")
        else:
            # instance.purchased_quantity = 0
            instance.balance += instance.amount
            messages.success(request, f"GHS {instance.amount} received successfully!")

            # email alert
            subject = 'Contributions Received Successfully'
            message = f"Shalom Baptist has received GHS{instance.amount} as {instance.item_name} contribution\n\n" \
                      f"May God bless God \n\n\n" \
                      f"visit https://shalombaptist.pythonanywhere.com/login to check your profile"
            recipient = instance.received_from.user.email
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)

            instance.save()
            cashflow_history = CashFlowHistory(
                category_id=instance.category_id,
                last_updated=instance.last_updated,
                item_name=instance.item_name,
                received_from=instance.received_from,
                amount=instance.amount,
                balance=instance.balance,
            )
            cashflow_history.save()

        return redirect('list_items')
    # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "queryset": queryset,
        "form": form,
    }
    return render(request, "accounts/add_item.html", context)


def outflows_items(request, pk):
    queryset = CashFlow.objects.get(id=pk)
    form = OutflowForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.amount <= 0:
            messages.success(request, "Amount can not be equal or less than zero")
        elif instance.amount >= instance.balance:
            messages.success(request, "Not enough balance")
        else:
            # instance.purchased_quantity = 0
            instance.balance -= instance.amount
            messages.success(request, f"GHS {instance.amount} issued successfully!")
            subject = 'Withdrawal Issued Successfully'
            message = f"Shalom Baptist has issued GHS{instance.amount} to {instance.returned_to}\n\n\n " \
                      f"visit https://shalombaptist.pythonanywhere.com/accounts to check outstanding balances"
            recipient = 'alibernard.coding@gmail.com'
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            instance.save()
            cashflow_history = CashFlowHistory(
                last_updated=instance.last_updated,
                category_id=instance.category_id,
                item_name=instance.item_name,
                returned_to=instance.returned_to,
                item_description=instance.item_description,
                amount=instance.amount,
                receipt_no=instance.receipt_no,
                balance=instance.balance,
            )
            cashflow_history.save()

        return redirect('list_items')
    # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "queryset": queryset,
        "form": form,
    }
    return render(request, "accounts/add_item.html", context)


def list_history(request):
    header = 'HISTORY DATA'
    queryset = CashFlowHistory.objects.all().order_by("-last_updated")
    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    form = CashFlowHistorySearchForm(request.POST or None)
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        category = form['category'].value()
        # queryset = StockHistory.objects.filter(
        #     item_name__icontains=form['item_name'].value()
        # )

        queryset = CashFlowHistory.objects.filter(
            item_name__icontains=form['item_name'].value(),
            last_updated__range=[
                form['start_date'].value(),
                form['end_date'].value()
            ]
        )

        if category != '':
            queryset = queryset.filter(category_id=category).order_by("-last_updated")

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Stock History.csv"'
            writer = csv.writer(response)
            writer.writerow(
                ['CATEGORY',
                 'ITEM NAME',
                 'AMOUNT',
                 'RECEIVE FROM',
                 'ISSUE TO',
                 'BALANCE',
                 'LAST UPDATED'])
            instance = queryset
            for stock in instance:
                writer.writerow(
                    [stock.category,
                     stock.item_name,
                     stock.amount,
                     stock.received_from,
                     stock.returned_to,
                     stock.balance,
                     stock.last_updated])
            return response

        paginator = Paginator(queryset, 15)
        page_number = request.GET.get('page')
        queryset = paginator.get_page(page_number)

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "accounts/list_history.html", context)


def cash_item(request):

    queryset = Cash.objects.all()
    context = {
        "queryset": queryset,
    }

    return render(request, "accounts/cash_item.html", context)


def cash_detail(request, pk):
    queryset = Cash.objects.get(id=pk)
    context = {
        "queryset": queryset,
    }
    return render(request, "accounts/cash_detail.html", context)


def issue_cash(request, pk):
    queryset = Cash.objects.get(id=pk)
    form = IssueCashForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.amount_out > instance.balance:
            messages.success(request, "Not Enough Cash")
        else:
            # instance.purchased_quantity = 0
            instance.balance -= instance.amount_out
            instance.issue_by = str(request.user)
            messages.success(request, "Issued SUCCESSFULLY. " + str(instance.balance) + " " + str(
                instance.category) + " balance left")
            subject = 'Withdrawal Issued Successfully'
            message = f"Shalom Baptist has issued GHS{instance.amount_out} to {instance.recipient} for {instance.detail} \n" \
                      f"The balance of {instance.category} is {instance.balance}\n\n " \
                      f"visit https://shalombaptist.pythonanywhere.com/accounts to check outstanding balances"
            recipient = 'alibernard.coding@gmail.com'
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            instance.save()
            cash_issue_history = CashHistory(
                last_updated=instance.last_updated,
                category=instance.category,
                detail=instance.detail,
                recipient=instance.recipient,
                issue_by=instance.issue_by,
                amount_out=instance.amount_out,
                created_on=instance.created_on,
                balance=instance.balance,
            )
            cash_issue_history.save()

        return redirect('cash_items')
    # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "queryset": queryset,
        "form": form,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "accounts/add_item.html", context)


def receive_cash(request, pk):
    queryset = Cash.objects.get(id=pk)
    form = ReceiveCashForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.purchased_quantity = 0
        instance.balance += instance.amount_in
        messages.success(request, "Received SUCCESSFULLY. " + str(instance.balance) + " " + str(
            instance.category) + " balance left")
        subject = 'Received Successfully'
        message = f"Shalom Baptist has received GHS{instance.amount_in} for {instance.detail} \n" \
                  f"The balance {instance.category} is GHS{instance.balance}\n\n " \
                  f"visit https://shalombaptist.pythonanywhere.com/accounts to check outstanding balances"
        recipient = 'alibernard.coding@gmail.com'
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        instance.save()
        cash_receive_history = CashHistory(
            last_updated=instance.last_updated,
            category=instance.category,
            detail=instance.detail,
            issue_by=instance.issue_by,
            amount_in=instance.amount_in,
            created_on=instance.created_on,
            balance=instance.balance,
        )
        cash_receive_history.save()

        return redirect('cash_items')

    context = {
        "queryset": queryset,
        "form": form,
        "username": 'Received By: ' + str(request.user),
    }
    return render(request, "accounts/add_item.html", context)


def cash_history(request):
    header = 'CASH HISTORY'
    queryset = CashHistory.objects.all()
    form = CashHistorySearchForm(request.POST or None)
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':

        queryset = CashHistory.objects.filter(
            category__icontains=form['category'].value(),
            last_updated__range=[
                form['start_date'].value(),
                form['end_date'].value()
            ]
        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Stock History.csv"'
            writer = csv.writer(response)
            writer.writerow(
                ['CATEGORY',
                 'RECIPIENT',
                 'DETAIL',
                 'RECEIVED AMOUNT',
                 'PAID AMOUNT',
                 'BALANCE',
                 'ISSUED BY',
                 'LAST UPDATED'])
            instance = queryset
            for stock in instance:
                writer.writerow(
                    [stock.category,
                     stock.recipient,
                     stock.detail,
                     stock.amount_in,
                     stock.amount_out,
                     stock.balance,
                     stock.issue_by,
                     stock.last_updated])
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "accounts/cash_history.html", context)