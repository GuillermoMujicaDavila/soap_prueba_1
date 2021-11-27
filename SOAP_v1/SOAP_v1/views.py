from django.views.decorators.csrf import csrf_exempt
from spyne.application import Aplications
from spyne.decorator import rpc
from spyne.model.primitive import Unicode,Integer,Double,String,DateTime
from spyne.protocol.soap import Soap11, soap11
from spyne.server import django
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
import json
# from apps.comun.models.Pais import Pais
from spyne import Iterable,Array
from spyne import ComplexModel
from django.forms.models import model_to_dict
# from app.comun.always.SearchFilter import keys_add_none
from django.db import IntegrityError
from spyne.error import ResourceNotFoundError
from spyne.model.fault import Fault
from django.db.models.deletion import ProtectedError

class SoapService (ServiceBase):
    @rpc(Double(),Double(), _returns=Double)
    def suma(ctx,a,b):
        return a + b

soap_app = Application(
    [SoapService],
    tns= 'django.soap.example',
    in_protocol=Soap11(validator = 'lxml'),
    out_protocol=Soap11().    
)

def consulta():
    django_soap_app = DjangoApplication(soap_app)
    my_soap_app = csrf_exempt(django_soap_app)

    return my_soap_app