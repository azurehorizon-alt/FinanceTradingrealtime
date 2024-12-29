import random
import time
from datetime import datetime, timezone  # Import timezone for UTC
from azure.eventhub import EventHubProducerClient, EventData

# Azure Event Hub connection details
connection_str = "Endpoint=sb://livestrm-ns.servicebus.windows.net/;SharedAccessKeyName=livestrm-pol;SharedAccessKey=H7bYnOh8m9O4mcnrLgAykBtcgqspJuSzn+AEhN9Z5Ew=;EntityPath=livestrm-eh"
event_hub_name = "livestrm-eh"

# Expanded list of symbols
symbols = [
    "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA",  # Original symbols

]
transaction_types = ["BUY", "SELL"]

# Initialize Event Hub producer
producer = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=event_hub_name)

def generate_transaction():
    """
    Generate a simulated financial transaction with extremely volatile market conditions.
    """
    symbol = random.choice(symbols)
    transaction_type = "SELL" if random.random() < 0.5 else "BUY"

    # Generate a base price with extreme variability
    base_price = round(random.uniform(1, 1000), 2)
    multiplier = random.choice([0.1, 0.3, 0.7, 1.2, 2.5, 5, 10])  # More volatility
    price = round(base_price * multiplier, 2)

    # Generate a base quantity with higher variability
    base_quantity = random.randint(10, 1000)
    quantity = base_quantity * random.choice([1, 2, 5, 10])

    # Add random spikes or dips
    if random.random() < 0.1:  # 10% chance of a sudden spike or dip
        price *= random.choice([0.5, 2, 3])
        quantity *= random.choice([2, 3, 5])

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "symbol": symbol,
        "transaction_type": transaction_type,
        "price": round(price, 2),
        "quantity": quantity
    }

def send_transactions():
    """
    Simulate and send batches of transactions to Azure Event Hub.
    """
    try:
        with producer:
            while True:
                event_data_batch = producer.create_batch()

                # Generate and add 100 transactions to the batch for high activity
                for _ in range(100):
                    transaction = generate_transaction()
                    event_data_batch.add(EventData(str(transaction)))

                # Send the batch to Event Hub
                producer.send_batch(event_data_batch)
                print("Transaction batch sent!")
                time.sleep(0.03)  # Shorter pause for faster data generation

    except KeyboardInterrupt:
        print("Transaction simulation stopped.")

if __name__ == "__main__":
    send_transactions()
