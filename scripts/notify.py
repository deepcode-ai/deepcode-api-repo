import requests
import json

def send_notification(message):
    try:
        print("Sending notification...")

        # Example: Send a Slack notification (replace with your actual Slack webhook URL)
        slack_webhook_url = "https://hooks.slack.com/services/your-webhook-url"
        payload = {
            "text": message
        }

        response = requests.post(slack_webhook_url, json=payload)
        response.raise_for_status()

        print("Notification sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    send_notification("Automation task completed successfully!")
