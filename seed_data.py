
import os
import django
import random
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales_leaderboard.settings')
django.setup()

from leaderboard.models import SalesRecord

agents = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

for _ in range(100):
    agent_name = random.choice(agents)
    sales_amount = Decimal(random.uniform(1000, 10000)).quantize(Decimal('0.01'))
    deals_count = random.randint(1, 20)

    SalesRecord.objects.create(
        agent_name=agent_name,
        sales_amount=sales_amount,
        deals_count=deals_count
    )
print("Seed data created successfully.")
