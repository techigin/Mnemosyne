from django.dispatch import Signal

calculate_current_balance_signal = Signal(providing_args=[
    'instance',
    'request'
])
