from django import forms
from base.models import Contato, Reserva


class ContatoForm(forms.ModelForm):
    class Meta:
        #Definir modelo do formulario
        model = Contato

        #Definir os campos do formulario
        fields = ['nome', 'email', 'mensagem']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu nome'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Insira seu e-mail'
                }
            ),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder': 'Insira sua mensagem'
                }
            )
        }    

        #Definir "titulos" dos campos
        labels = {
            'nome': 'Nome:',
            'email': 'E-mail:', 
            'mensagem': 'Mensagem:'
        }

class DateImput(forms.DateInput):
     input_type = 'date'

#Formulario de reservas
class ReservaForm(forms.ModelForm):
    class Meta:
        #Definir modelo do formulario
        model = Reserva

        #Definir os campos do formulario
        fields = ['nome_pet', 'telefone', 'data_reserva', 'observacao']

        widgets = {
            'nome_pet': forms.TextInput(
                attrs={
                    'placeholder': 'Insira o nome do seu pet'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Insira o telefone'
                }
            ),
            'data_reserva': DateImput(),

            'observacao': forms.Textarea(
                attrs={
                    'placeholder': 'Insira suas observação'
                }
            )
        }    

        #Definir "titulos" dos campos
        labels = {
            'nome': 'Nome do pet:',
            'telefone': 'Telefone:', 
            'data': 'Dara da Reserva:',
            'observacao': 'Observação:'
        }