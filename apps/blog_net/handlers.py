def model_saved(sender, **kwargs):
    print "SAVED", sender, kwargs

def message_sent(sender, email, **kwargs):
    print "Received email:", email, sender, kwargs
