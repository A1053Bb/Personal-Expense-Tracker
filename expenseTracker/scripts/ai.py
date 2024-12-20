import openai
from ExpTrack.models import Issue, Category



def categorize_transaction(transaction_name):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content": "You are categorization assistant."},
            {"role": "user", "content": f"Categorize the following transaction: {transaction_name}. Example categories: Food, Travel, Shopping, etc."}
        ],
        max_tokens=50
    )
    category = response['choices'][0]['message']['content'].strip()
    return category

def process_transactions():
    transactions = Issue.objects.all()

    category_totals = {}

    for transaction in transactions:
        category = categorize_transaction(transaction.txn_name)

        if category in category_totals :
            category_totals[category] += transaction.charges
        else :
            category_totals[category] = transaction.charges

    for category, total_amount in category_totals.items():
        categorized_transaction, created = Category.objects.get_or_create(
            category_name = category,
            defaults={'category_amount': 0}
        )

        categorized_transaction.category_amount += total_amount
        categorized_transaction.save()