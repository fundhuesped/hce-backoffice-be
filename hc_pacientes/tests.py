#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_common.tests import CommonTestHelper
from hc_pacientes.models import Paciente
from rest_framework import status
import datetime

class PacienteTest(APITestCase):
    def test_createPaciente(self):
        """
        Asegura crear un Paciente
        :return:
        """
        cth = CommonTestHelper()
        cth.createDocumentType()
        cth.createSexType()
        cth.createLocation()
        cth.createCivilStatus()
        cth.createEducationType()
        cth.createSocialService()
        data= {
            "idpaciente": "AAAA",
            "prospect": False,
            "firstName": "Paciente",
            "otherNames": "Pacientito",
            "fatherSurname": "Prueba",
            "motherSurname": "Del test",
            "birthDate": datetime.date(year=1986,month=1,day=2),
            "email": "prueba@me.com",
            "street": "Calle",
            "postal": "1234",
            "status": "Active",
            "documentType": {
                "id": 1
            },
            "documentNumber": "25456111",
            "genderAtBirth": {
                "id": 1
            },
            "genderOfChoice": {
                "id": 1
            },
            "location": {
                "id": 1
            },
            "occupation": "Ocupacion",
            "civilStatus": {
                "id": 1
            },
            "education": {
                "id": 1
            },
            "socialService": {
                "id": 1
            },
            "socialServiceNumber": "AAADDD",
            "terms": True,
            "bornPlace": "Capital",
            "firstVisit": datetime.date(year=2015, month=3, day=5),
            "notes": "Notitas",
            "primaryPhoneNumber": "111444555",
            "primaryPhoneContact": "Yo",
            "primaryPhoneMessage": True,
            "secondPhoneNumber": "21454545",
            "secondPhoneContact": "El",
            "secondPhoneMessage": False,
            "thirdPhoneNumber": "45654654",
            "thirdPhoneContact": "Ella",
            "thirdPhoneMessage": False
        }
        response = self.client.post('/pacientes/paciente/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Paciente.objects.count(),1)

    def test_getPacientes(self):
        """
        Obtiene todos los Pacientes
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.get('/pacientes/paciente/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPaciente(self):
        """
        Obtiene un Paciente
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.get('/pacientes/paciente/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredPaciente(self):
        """
        Obtiene un Paciente filtrado por nombre y apellido
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.get('/pacientes/paciente/?firstName=Cac&fatherSurename=Cas',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePaciente(self):
        """
        Elinima un Paciente
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.delete('/pacientes/paciente/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Paciente.objects.count(),0)

    def test_updatePaciente(self):
        """
        Modifica un Paciente
        :return:
        """
        helperp = PacienteTestHelper()
        helperp.createPaciente()
        cth = CommonTestHelper()
        cth.createDocumentType()
        cth.createSexType()
        cth.createLocation()
        cth.createCivilStatus()
        cth.createEducationType()
        cth.createSocialService()

        data= {
            "idpaciente": "ABABAB",
            "prospect": True,
            "firstName": "Paciente 2",
            "otherNames": "Pacientito 2",
            "fatherSurname": "Prueba 2",
            "motherSurname": "Del test 2",
            "birthDate": datetime.date(year=1985,month=1,day=2),
            "email": "prueba@me.com.ar",
            "street": "Calle 2",
            "postal": "12342",
            "status": "Inactive",
            "documentType": {
                "id": 2
            },
            "documentNumber": "254561112",
            "genderAtBirth": {
                "id": 2
            },
            "genderOfChoice": {
                "id": 2
            },
            "location": {
                "id": 2
            },
            "occupation": "Ocupacion2",
            "civilStatus": {
                "id": 2
            },
            "education": {
                "id": 2
            },
            "socialService": {
                "id": 2
            },
            "socialServiceNumber": "AAADDDD",
            "terms": False,
            "bornPlace": "Capital2",
            "firstVisit": datetime.date(year=2014, month=3, day=5),
            "notes": "Notitas2",
            "primaryPhoneNumber": "1114445552",
            "primaryPhoneContact": "Yo2",
            "primaryPhoneMessage": False,
            "secondPhoneNumber": "214545452",
            "secondPhoneContact": "El2",
            "secondPhoneMessage": True,
            "thirdPhoneNumber": "456546542",
            "thirdPhoneContact": "Ella2",
            "thirdPhoneMessage": True
        }
        response = self.client.put('/pacientes/paciente/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["idpaciente"], "ABABAB")
        self.assertEqual(response.json()["prospect"], True)
        self.assertEqual(response.json()["firstName"], "Paciente 2")
        self.assertEqual(response.json()["otherNames"], "Pacientito 2")
        self.assertEqual(response.json()["fatherSurname"], "Prueba 2")
        self.assertEqual(response.json()["motherSurname"], "Del test 2")
        self.assertEqual(response.json()["birthDate"], "1985-01-02")
        self.assertEqual(response.json()["email"], "prueba@me.com.ar")
        self.assertEqual(response.json()["street"], "Calle 2")
        self.assertEqual(response.json()["postal"], "12342")
        self.assertEqual(response.json()["status"], "Inactive")
        self.assertEqual(response.json()["documentType"]["id"],2)
        self.assertEqual(response.json()["documentNumber"], "254561112")
        self.assertEqual(response.json()["genderAtBirth"]["id"],2)
        self.assertEqual(response.json()["genderOfChoice"]["id"],2)
        self.assertEqual(response.json()["location"]["id"],2)
        self.assertEqual(response.json()["occupation"],"Ocupacion2")
        self.assertEqual(response.json()["civilStatus"]["id"],2)
        self.assertEqual(response.json()["education"]["id"],2)
        self.assertEqual(response.json()["socialService"]["id"],2)
        self.assertEqual(response.json()["socialServiceNumber"],"AAADDDD")
        self.assertEqual(response.json()["terms"], False)
        self.assertEqual(response.json()["bornPlace"],"Capital2")
        self.assertEqual(response.json()["firstVisit"], "2014-03-05")
        self.assertEqual(response.json()["notes"], "Notitas2")
        self.assertEqual(response.json()["primaryPhoneNumber"], "1114445552")
        self.assertEqual(response.json()["primaryPhoneContact"], "Yo2")
        self.assertEqual(response.json()["primaryPhoneMessage"], False)
        self.assertEqual(response.json()["secondPhoneNumber"], "214545452")
        self.assertEqual(response.json()["secondPhoneContact"],"El2")
        self.assertEqual(response.json()["secondPhoneMessage"], True)
        self.assertEqual(response.json()["thirdPhoneNumber"], "456546542")
        self.assertEqual(response.json()["thirdPhoneContact"], "Ella2")
        self.assertEqual(response.json()["thirdPhoneMessage"], True)


class PacienteTestHelper():

    def createPaciente(self):
        cth = CommonTestHelper()
        dt=cth.createDocumentType()
        st=cth.createSexType()
        loc= cth.createLocation()
        cs=cth.createCivilStatus()
        et=cth.createEducationType()
        ss=cth.createSocialService()

        paciente = Paciente.objects.create(
            idpaciente= "AAAA",
            prospect= False,
            firstName= "Paciente",
            otherNames= "Pacientito",
            fatherSurname= "Prueba",
            motherSurname= "Del test",
            birthDate= datetime.date(year=1986,month=1,day=2),
            email= "prueba@me.com",
            street= "Calle",
            postal= "1234",
            status= "Active",
            documentType = dt,
            documentNumber= "25456111",
            genderAtBirth=st,
            genderOfChoice=st,
            location=loc,
            occupation= "Ocupacion",
            civilStatus=cs,
            education=et,
            socialService=ss,
            socialServiceNumber= "AAADDD",
            terms= True,
            bornPlace= "Capital",
            firstVisit= datetime.date(year=2015, month=3, day=5),
            notes= "Notitas",
            primaryPhoneNumber= "111444555",
            primaryPhoneContact= "Yo",
            primaryPhoneMessage= True,
            secondPhoneNumber= "21454545",
            secondPhoneContact= "El",
            secondPhoneMessage= False,
            thirdPhoneNumber="45654654",
            thirdPhoneContact= "Ella",
            thirdPhoneMessage= False
        )

        return paciente