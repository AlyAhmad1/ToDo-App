from django import forms


class PersonForm(forms.Form):
    text = forms.CharField(max_length=75, label = "Items",
                           widget=forms.TextInput(
                               attrs={"class": "input_1" , "Placeholder":"Max 70"}
                           ))
    Date = forms.DateField(label = "Date",
    widget=forms.DateInput(
            attrs={"class": "input_1", "Placeholder":"YYYY-DD-MM"}
        )
    )
