from .signals import calculate_current_balance_signal

class CalculateCurrentBalanceMixins(object):
    def get_context_data(self, *args, **kwargs):
        context = super(CalculateCurrentBalanceMixins, self).get_context_data(*args, **kwargs)
        request = self.request
        instance = context.get('object')
        if instance:
            calculate_current_balance_signal.send(instance.__class__, instance=instance, request=request)
        return context
