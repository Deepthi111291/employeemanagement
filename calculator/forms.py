from django import forms                 #forms module,Form class

class OperationForm(forms.Form):
    num1=forms.IntegerField(label='Enter number 1')
    num2=forms.IntegerField(label="Enter number 2")
    def clean(self):
        cleaned_data=super().clean()
        n1=cleaned_data.get("num1")
        n2=cleaned_data.get("num2")
        if n1<0:
            msg="invalid number"
            self.add_error("num1",msg)
        if n2<0:
            msg="Invalid number"
            self.add_error("num2",msg)







