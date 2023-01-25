import csv

from django.contrib import messages
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.forms import CashFlowCreateForm, CashFlowUpdateForm, InflowForm, OutflowForm, CashFlowHistorySearchForm
from accounts.models import Category, CashFlow, CashFlowHistory
from core.models import Family, Auxiliaries, Ministries
from authy.models import User, Profile

from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.


def accounts_home(request):
    member_count = User.objects.all().count()
    family_count = Family.objects.all().count()
    auxiliary_count = Auxiliaries.objects.all().count()
    ministry_count = Auxiliaries.objects.all().count()
    context = {
        "member_count": member_count,
        "family_count": family_count,
        'auxiliary_count': auxiliary_count,
        'ministry_count': ministry_count
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
    context = {
        'member': member
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