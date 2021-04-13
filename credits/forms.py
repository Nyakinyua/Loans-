from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, Fieldset
from crispy_forms.bootstrap import PrependedText


class LoanForm(forms.Form):
    amount_borrowed = forms.DecimalField(label='Amount to borrow',decimal_places=2,help_text=u"Amount to be borrowed")
    repayment = forms.DecimalField(label='Cash Paid Periodically',decimal_places=2,help_text=u"Repayment per month")
    interest_rate = forms.DecimalField(label='interest rate',decimal_places=2,help_text=u"Company borrowing rate")
    installments = forms.ChoiceField(choices=((x, x) for x in range(1, 85)))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.disable_csrf = False
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    'Company loan Rate',
                    Div(
                        Div(PrependedText('amount_borrowed', 'Ksh:', placeholder='Amount Borrowed'), css_class="col-lg-12"),
                        Div(PrependedText('repayment', 'Ksh: ', placeholder='Cash Payment Monthly '), css_class="col-lg-12"),
                        Div(PrependedText('interest_rate', '%', placeholder='Company borrowing rate'), css_class="col-lg-12"),
                        Div(Field('installments'), css_class="col-lg-12"),
                        css_class="row"
                    ),
                ),
            ),
            Div(
                Div(
                    HTML('<input title="Calculate" type="submit" name="submit" value="Calculate" class="btn btn-primary btn-lg"/>'),
                    css_class="col-lg-12",
                ),
                css_class="row",
            ),
        )
        super(LoanForm, self).__init__(*args, **kwargs)