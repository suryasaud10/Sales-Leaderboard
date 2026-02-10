from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .services import get_aggregated_leaderboard
from rest_framework.views import APIView
from .models import SalesRecord
from .pagination import StandardPagination
from .serializers import LeaderboardItemSerializer, SalesRecordSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SaleForm
from django.db.models import Sum




# Create your views here.

class SalesRecordCreateView(generics.CreateAPIView):
    queryset = SalesRecord.objects.all()
    serializer_class = SalesRecordSerializer


class LeaderboardView(APIView):
    def get(self, request):
        # Get the aggregated leaderboard data
        data = get_aggregated_leaderboard()
        paginator = StandardPagination()
        page= paginator.paginate_queryset(data, request)
        serializer = LeaderboardItemSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
def leaderboard_frontend(request):
    return render(request, 'leaderboard.html')




class SaleListView(ListView):
    model = SalesRecord
    template_name = 'sales/sale_list.html'
    context_object_name = 'sales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        totals = SalesRecord.objects.aggregate(
            total_sales_amount=Sum("sales_amount"),
            total_deal_count=Sum("deals_count")
        )

        context["total_sales_amount"] = totals["total_sales_amount"] or 0
        context["total_deal_count"] = totals["total_deal_count"] or 0

        return context

class SaleCreateView(CreateView):
    model = SalesRecord
    form_class = SaleForm
    template_name = "sales/sale_form.html"
    success_url = reverse_lazy("sale-list")
    
class SaleUpdateView(UpdateView):
    model = SalesRecord
    form_class = SaleForm
    template_name = "sales/sale_form.html"
    success_url = reverse_lazy("sale-list")


class SaleDeleteView(DeleteView):
    model = SalesRecord
    template_name = "sales/sale_confirm_delete.html"
    success_url = reverse_lazy("sale-list")


def sales_list(request):
    sales = SalesRecord.objects.all()

    totals = sales.aggregate(
        total_deal_count=Sum("deals_count"),
        total_sales_amount=Sum("sales_amount")
    )

    context = {
        "sales": sales,
        "total_deal_count": totals["total_deal_count"] or 0,
        "total_sales_amount": totals["total_sales_amount"] or 0,
    }
    return render(request, "sales/sales_list.html", context)
