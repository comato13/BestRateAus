from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_exchange_rates
import time

scheduler = BackgroundScheduler()

# Schedule the scraper to run every 30 minutes
scheduler.add_job(scrape_exchange_rates, "interval", minutes=30)

# Start the scheduler
scheduler.start()

# Keep the script running
try:
    while True:
        time.sleep(60)  # Prevent script from exiting
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()