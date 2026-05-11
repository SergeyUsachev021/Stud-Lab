from djoser.email import ActivationEmail


class AwesomeActivationEmail(ActivationEmail):
    template_name = "email/activation.html"