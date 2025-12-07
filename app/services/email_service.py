from app.core.logger import logger
from app.models.user import User
from app.models.order import Order


class EmailService:
    def send_welcome_email(self, user: User):
        # In a real app, use smtplib or a provider
        logger.info(f"Sending welcome email to {user.email}")
        # Mock sending
        logger.info(
            f"Subject: Welcome to E-Commerce\nTo: {user.email}\nBody: Welcome {user.first_name}!"
        )

    def send_order_confirmation(self, user: User, order: Order):
        logger.info(f"Sending order confirmation to {user.email}")
        # Mock sending
        logger.info(
            f"Subject: Order Confirmation #{order.order_number}\nTo: {user.email}\nBody: Thank you for your order! Total: {order.total_amount}"
        )
