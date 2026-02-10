from django.db.models import Sum
from .models import SalesRecord

def get_aggregated_leaderboard():
    # Aggregate total sales and deals for each agent
    leaderboard_data = SalesRecord.objects.values('agent_name').annotate(
        total_sales=Sum('sales_amount'),
        total_deals=Sum('deals_count')
    ).order_by('-total_sales', '-total_deals')

    # Assign ranks based on total sales and deals
    ranked_leaderboard = []
    current_rank = 1
    previous_sales = None
    previous_deals = None

    for index, record in enumerate(leaderboard_data):
        if previous_sales is not None:
            if record['total_sales'] < previous_sales or (record['total_sales'] == previous_sales and record['total_deals'] < previous_deals):
                current_rank = index + 1
        
        ranked_leaderboard.append({
            'rank': current_rank,
            'agent_name': record['agent_name'],
            'total_sales': record['total_sales'],
            'total_deals': record['total_deals']
        })

        previous_sales = record['total_sales']
        previous_deals = record['total_deals']

    return ranked_leaderboard