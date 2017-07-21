#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_practicas.models import Especialidad, Prestacion, Profesional, Period, DayOfWeek, Agenda, Turno, Ausencia
from hc_common.tests import CommonTestHelper
from hc_pacientes.tests import PacienteTestHelper
from hc_pacientes.models import Paciente
import datetime, calendar
from rest_framework import status

class ProfesionalTest(APITestCase):
    def test_createProfesional(self):
        """
        Asegura crear un Profesional
        :return:
        """
        cth = CommonTestHelper()
        cth.createDocumentType()
        cth.createSexType()
        cth.createLocation()
        cth.createCivilStatus()
        cth.createEducationType()
        cth.createSocialService()
        helper = GatewayTestHelper()
        helper.createPrestacion()

        data= {
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
            "thirdPhoneMessage": False,
            "prestaciones":[
                {
                    "id":1
                }
            ]
        }
        response = self.client.post('/practicas/profesional/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profesional.objects.count(),1)

    def test_createProfesionalBasico(self):
        """
        Asegura crear un Profesional con los datos basicos
        :return:
        """
        cth = CommonTestHelper()
        cth.createDocumentType()
        helper = GatewayTestHelper()
        helper.createPrestacion()

        data = {
            "firstName": "Paciente",
            "otherNames": "Pacientito",
            "fatherSurname": "Prueba",
            "motherSurname": "Del test",
            "prestaciones": [
                {
                    "id": 1
                }
            ]
        }
        response = self.client.post('/practicas/profesional/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profesional.objects.count(), 1)

    def test_getProfesionales(self):
        """
        Obtiene todos los Profesionales
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.get('/practicas/profesional/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getProfesional(self):
        """
        Obtiene un Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.get('/practicas/profesional/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredProfesional(self):
        """
        Obtiene un Profesional filtrado por nombre y apellido
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.get('/practicas/profesional/?firstName=Cac&fatherSurename=Cas',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteProfesional(self):
        """
        Elinima un Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.delete('/practicas/profesional/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profesional.objects.count(),0)

    def test_updateProfesional(self):
        """
        Modifica un Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        cth = CommonTestHelper()
        cth.createDocumentType()
        cth.createSexType()
        cth.createLocation()
        cth.createCivilStatus()
        cth.createEducationType()
        cth.createSocialService()
        helper.createPrestacion()

        data= {
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
                "id": 1
            },
            "documentNumber": "254561112",
            "genderAtBirth": {
                "id": 1
            },
            "genderOfChoice": {
                "id": 1
            },
            "location": {
                "id": 1
            },
            "occupation": "Ocupacion2",
            "civilStatus": {
                "id": 1
            },
            "education": {
                "id": 1
            },
            "socialService": {
                "id": 1
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
            "thirdPhoneMessage": True,
            "prestaciones":[
                {
                    "id":1
                }
            ]
        }
        response = self.client.put('/practicas/profesional/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["firstName"], "Paciente 2")
        self.assertEqual(response.json()["otherNames"], "Pacientito 2")
        self.assertEqual(response.json()["fatherSurname"], "Prueba 2")
        self.assertEqual(response.json()["motherSurname"], "Del test 2")
        self.assertEqual(response.json()["birthDate"], "1985-01-02")
        self.assertEqual(response.json()["email"], "prueba@me.com.ar")
        self.assertEqual(response.json()["street"], "Calle 2")
        self.assertEqual(response.json()["postal"], "12342")
        self.assertEqual(response.json()["status"], "Inactive")
        self.assertEqual(response.json()["documentType"]["id"],1)
        self.assertEqual(response.json()["documentNumber"], "254561112")
        self.assertEqual(response.json()["genderAtBirth"]["id"],1)
        self.assertEqual(response.json()["genderOfChoice"]["id"],1)
        self.assertEqual(response.json()["location"]["id"],1)
        self.assertEqual(response.json()["occupation"],"Ocupacion2")
        self.assertEqual(response.json()["civilStatus"]["id"],1)
        self.assertEqual(response.json()["education"]["id"],1)
        self.assertEqual(response.json()["socialService"]["id"],1)
        self.assertEqual(response.json()["socialServiceNumber"],"AAADDDD")
        self.assertEqual(response.json()["bornPlace"],"Capital2")
        self.assertEqual(response.json()["notes"], "Notitas2")
        self.assertEqual(response.json()["primaryPhoneNumber"], "1114445552")
        self.assertEqual(response.json()["primaryPhoneContact"], "Yo2")
        self.assertEqual(response.json()["primaryPhoneMessage"], False)


class PeriodTest(APITestCase):
    def test_createPeriod(self):
        """
        Asegura crear un Periodo
        :return:
        """
        helper = GatewayTestHelper()
        helper.createDayOfWeek(),
        helper.createDayOfWeek()
        data= {
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
            'selected': False,
            'daysOfWeek': [
                {"id":1},
                {"id":2}
            ]
        }
        response = self.client.post('/practicas/period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Period.objects.count(),1)

    def test_getPeriods(self):
        """
        Obtiene todos los Periodos
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPeriod()
        response = self.client.get('/practicas/period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPeriodo(self):
        """
        Obtiene un Periodo
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPeriod()
        response = self.client.get('/practicas/period/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePeriod(self):
        """
        Elinima un Periodo
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPeriod()
        response = self.client.delete('/practicas/period/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Period.objects.count(),0)

    def test_updatePeriod(self):
        """
        Modifica un Period
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createPeriod()
        helperp.createDayOfWeek()
        data= {
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
            'selected': False,
            'daysOfWeek': [
                {"id":1}
            ]
        }
        response = self.client.put('/practicas/period/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['start'], datetime.datetime.now().strftime('%H:%M:%S'))
        self.assertEqual(response.json()['end'],(datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'))
        self.assertEqual(response.json()['selected'], False)
        self.assertEqual(response.json()['daysOfWeek'][0]['id'], 1)


class EspecialidadTest(APITestCase):
    def test_createEspecialidad(self):
        """
        Asegura crear una Especialidad
        :return:
        """
        data= {'name': 'Pediatria', 'description':'Especialidad dedicada a menores de 15 anos', 'status':'Active'}
        response = self.client.post('/practicas/especialidad/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Especialidad.objects.count(),1)

    def test_getEspecialidades(self):
        """
        Obtiene todas las Especialidades
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/especialidad/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getEspecialidad(self):
        """
        Obtiene una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/especialidad/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredEspecialidad(self):
        """
        Obtiene una Especialidad filtrada
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/especialidad/?name=Ped',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteEspecialidad(self):
        """
        Elinima una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.delete('/practicas/especialidad/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Especialidad.objects.count(),0)

    def test_updateEspecialidad(self):
        """
        Modifica una Especialidad
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createEspecialidad()
        data= {'name': 'Pediatria pediatrica', 'description':'Especialidad dedicada a personas no mayores de 15 anos', 'status':'Active'}
        response = self.client.put('/practicas/especialidad/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],'Pediatria pediatrica')
        self.assertEqual(response.json()['description'],'Especialidad dedicada a personas no mayores de 15 anos')


class PrestacionTest(APITestCase):
    def test_createPrestacion(self):
        """
        Asegura crear una Prestacion
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()

        data = {
            'name': 'Consulta infectologia 2',
            'description': 'Consulta infectologia 2',
            'duration': 40,
            'status': Prestacion.STATUS_INACTIVE,
            'notes': 'Consulta infectologia 2',
            'default': False,
            'especialidad': {'id':1}
        }

        response = self.client.post('/practicas/prestacion/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Prestacion.objects.count(),1)

    def test_getPrestacioneses(self):
        """
        Obtiene todas las Prestaciones
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.get('/practicas/prestacion/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPrestacion(self):
        """
        Obtiene una Prestacion
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.get('/practicas/prestacion/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredPrestacion(self):
        """
        Obtiene una Prestacion filtrada
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.get('/practicas/prestacion/?name=Ped&status=Active',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_getPrestacinFilteredByProf(self):
        """
        Obtiene una prestacion filtrada por pk del profesional
        :return:
        """
        helper = GatewayTestHelper()
        pres = helper.createPrestacion()
        prof = helper.createProfesional()
        prof.prestaciones.add(pres)
        prof.save()
        response = self.client.get('/practicas/prestacion/?profesional=1',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())


    def test_deletePrestacion(self):
        """
        Elinima una Prestacion
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.delete('/practicas/prestacion/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Prestacion.objects.count(),0)

    def test_updatePrestacion(self):
        """
        Modifica una Prestacion
        :return:
        """
        helperp = GatewayTestHelper()
        prestacion = helperp.createPrestacion()
        especialidad = helperp.createEspecialidad()
        prestacion.especialidad.status=Especialidad.STATUS_INACTIVE
        prestacion.especialidad.save()

        data = {
            'name': 'Consulta infectologia 2',
            'description': 'Consulta infectologia 2',
            'duration': 40,
            'status': Prestacion.STATUS_INACTIVE,
            'notes': 'Consulta infectologia 2',
            'default': False,
            'especialidad': {'id':2}
        }
        response = self.client.put('/practicas/prestacion/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],'Consulta infectologia 2')
        self.assertEqual(response.json()['description'],'Consulta infectologia 2')
        self.assertEqual(response.json()['duration'],40)
        self.assertEqual(response.json()['notes'],'Consulta infectologia 2')
        self.assertEqual(response.json()['default'],False)
        self.assertEqual(response.json()['especialidad']['id'],2)


class AgendaTest(APITestCase):

    def test_createAgendaSinFecha(self):
        """
        Asegura crear una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()
        prof.prestaciones.add(pres)
        prof.save()

        data= {
            'status':'Active',
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'periods':[
                {
                    "id":1,
                    'start': datetime.datetime.now().strftime('%H:%M:%S'),
                    'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                    'selected': False,
                    'daysOfWeek': [
                        {"id":1, "index": 0, "name":"Lunes", "selected":True},
                        {"id": 2, "index": 1, "name": "Martes", "selected": True},
                    ]
                }
            ]
        }
        response = self.client.post('/practicas/agenda/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agenda.objects.count(),1)
        self.assertEqual(DayOfWeek.objects.count(),2)
        self.assertEqual(response.json()['validFrom'],datetime.date.today().strftime('%Y-%m-%d'))
        self.assertEqual(response.json()['validTo'],datetime.date(year=datetime.date.today().year,
                                                                 month=datetime.date.today().month,
                                                                 day=calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]).strftime('%Y-%m-%d'))

    def test_createAgenda(self):
        """
        Asegura crear una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()

        helper.createDayOfWeek()
        helper.createDayOfWeek()

        data= {
            'status':'Active',
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'validFrom':datetime.date.today().strftime('%Y-%m-%d'),
            'validTo' : (datetime.date.today()+datetime.timedelta(days=3)).strftime('%Y-%m-%d'),
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'periods':[
                {
                    'start': datetime.datetime.now().strftime('%H:%M:%S'),
                    'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                    'selected': False,
                    'daysOfWeek': [
                        {"id":1},
                        {"id":2}
                    ]
                }
            ]
        }
        response = self.client.post('/practicas/agenda/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agenda.objects.count(),1)

    def test_getAgendas(self):
        """
        Obtiene todas las Especialidades
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        response = self.client.get('/practicas/agenda/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAgenda(self):
        """
        Obtiene una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        response = self.client.get('/practicas/agenda/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredAgenda(self):
        """
        Obtiene una Agenda filtrada
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/agenda/?status=Active&profesional=1&prestacion=1',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteAgenda(self):
        """
        Elinima una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        response = self.client.delete('/practicas/agenda/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agenda.objects.count(),0)

    def test_updateAgenda(self):
        """
        Modifica una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()
        prof.prestaciones.add(pres)
        prof.save()

        data= {
            'status':'Inactive',
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'validFrom': datetime.date.today().strftime('%Y-%m-%d'),
            'validTo': (datetime.date.today()+datetime.timedelta(days=3)).strftime('%Y-%m-%d'),
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'periods':[
                {
                    "id":1,
                    'start': datetime.datetime.now().strftime('%H:%M:%S'),
                    'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                    'selected': False,
                    'daysOfWeek': [
                        {"id":1,"index":0, "name":"Lunes", "selected":True},
                        {"id":2, "index":1, "name":"Martes", "selected":False}
                    ]
                }
            ]
        }
        response = self.client.put('/practicas/agenda/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['status'],'Inactive')
        self.assertEqual(response.json()['start'],datetime.datetime.now().strftime('%H:%M:%S'))
        self.assertEqual(response.json()['end'],(datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'))
        self.assertEqual(response.json()['validFrom'],datetime.date.today().strftime('%Y-%m-%d'))
        self.assertEqual(response.json()['validTo'],(datetime.date.today()+datetime.timedelta(days=3)).strftime('%Y-%m-%d'))
        self.assertEqual(response.json()['profesional']['id'],1)
        self.assertEqual(response.json()['prestacion']['id'],1)

    def test_updateAgendaConTurno(self):
        """
        Modifica una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        phelper = PacienteTestHelper()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()
        prof.prestaciones.add(pres)
        prof.save()
        agenda = helper.createAgendaConTurno(prestacion=pres, profesional=prof)
        turnos = Turno.objects.all().filter(profesional=prof, prestacion=pres)
        turnos[0].taken=True
        turnos[0].paciente = phelper.createPaciente()
        turnos[0].save()

        start = agenda.start
        end=agenda.end
        data= {
            'status':'Inactive',
            'start': start.strftime('%H:%M:%S'),
            'end': end.strftime('%H:%M:%S'),
            'validFrom': agenda.validFrom.strftime('%Y-%m-%d'),
            'validTo': agenda.validTo.strftime('%Y-%m-%d'),
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'periods':[
                {   'id':1,
                    'start': datetime.datetime.now().strftime('%H:%M:%S'),
                    'end': (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime('%H:%M:%S'),
                    'selected': True,
                    'daysOfWeek': [
                        {"id":1,"index":0, "name":"Lunes", "selected":True},
                        {"id":2, "index":1, "name":"Martes", "selected":True}
                    ]
                 },
                {'id': 2,
                 'start': (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%H:%M:%S'),
                 'end': (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime('%H:%M:%S'),
                 'selected': True,
                 'daysOfWeek': [
                     {"id": 1, "index": 0, "name": "Lunes", "selected": True},
                     {"id": 2, "index": 1, "name": "Martes", "selected": True}
                 ]
                 }
            ]
        }
        response = self.client.put('/practicas/agenda/1/', data, format='json')
        turnos = Turno.objects.all().filter(profesional=prof, prestacion=pres, start__gte=start, day__gte=datetime.date.today(), day__lte=datetime.date.today()+datetime.timedelta(days=3))#, status=Turno.STATUS_INACTIVE)
        self.assertGreaterEqual(turnos.count(),1)
        #self.assertEqual(turnos[0].status,Turno.STATUS_INACTIVE)

class TurnoTest(APITestCase):

    def test_createTurno(self):
        """
        Asegura crear un Turno
        :return:
        """
        helper = GatewayTestHelper()
        phelper = PacienteTestHelper()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()
        pas = phelper.createPaciente()

        data= {
            'day': datetime.date.today().strftime('%Y-%m-%d'),
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'taken':'False',
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'paciente': {"id": Paciente.objects.all()[0].pk}
        }
        response = self.client.post('/practicas/turno/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Turno.objects.count(),1)

    def test_getTurnos(self):
        """
        Obtiene todos los Turnos
        :return:
        """
        helper = GatewayTestHelper()
        helper.createTurno()
        response = self.client.get('/practicas/turno/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getTurno(self):
        """
        Obtiene un Turno
        :return:
        """
        helper = GatewayTestHelper()
        helper.createTurno()
        response = self.client.get('/practicas/turno/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteTurno(self):
        """
        Elinima una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        helper.createTurno()
        response = self.client.delete('/practicas/turno/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agenda.objects.count(),0)

    def test_updateTakenTurno(self):
        """
        Modifica el estado de taken de un turno
        :return:
        """
        helper = GatewayTestHelper()
        phelper = PacienteTestHelper()
        profesional = helper.createProfesional()
        prestacion1 = helper.createPrestacion()
        prestacion2 = helper.createPrestacion()
        profesional.prestaciones.add(prestacion1)
        profesional.prestaciones.add(prestacion2)
        profesional.save()

        helper.createTurno(datetime.time(10, 0, 0),datetime.time(10, 30, 0),profesional=profesional,
                           prestacion=prestacion1)
        turno_a_tomar = helper.createTurno(datetime.time(10, 30, 0), datetime.time(11, 00, 0), profesional=profesional,
                           prestacion=prestacion1)
        helper.createTurno(datetime.time(11, 0, 0), datetime.time(11, 30, 0), profesional=profesional,
                           prestacion=prestacion1)
        helper.createTurno(datetime.time(10, 30, 0), datetime.time(11, 30, 0), profesional=profesional,
                           prestacion=prestacion2)
        turno_no_modificar = helper.createTurno(datetime.time(12, 0, 0), datetime.time(12, 30, 0), profesional=profesional,
                           prestacion=prestacion2)
        turno_no_modificar.status = Turno.STATUS_ACTIVE
        turno_no_modificar.save()

        paciente = phelper.createPaciente()

        data = {
            'day': turno_a_tomar.day.strftime('%Y-%m-%d'),
            'start': turno_a_tomar.start.strftime('%H:%M:%S'),
            'end': turno_a_tomar.end.strftime('%H:%M:%S'),
            'taken': 'True',
            'profesional': {"id": profesional.pk},
            'prestacion': {"id": prestacion1.pk},
            'paciente': {"id": paciente.pk}
        }
        response = self.client.put('/practicas/turno/' + str(turno_a_tomar.pk) + '/', data, format='json')
        turnos_modificados = Turno.objects.filter(start=datetime.time(10,30,0), end=datetime.time(11,30,0), profesional=profesional, prestacion=prestacion2)
        turnos_no_modificados = Turno.objects.filter(start=datetime.time(12,0,0), end = datetime.time(12,30,0), profesional = profesional, prestacion=prestacion2)
        self.assertEqual(turnos_modificados[0].status,Turno.STATUS_INACTIVE)
        self.assertEqual(turnos_no_modificados[0].status,Turno.STATUS_ACTIVE)

    def test_updateTurno(self):
        """
        Modifica un Turno
        :return:
        """
        helper = GatewayTestHelper()
        helper.createTurno()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()
        prof.prestaciones.add(pres)
        prof.save()
        phelper = PacienteTestHelper()
        paciente = phelper.createPaciente()

        data= {
            'day': datetime.date.today().strftime('%Y-%m-%d'),
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'taken':'True',
            'profesional': {"id":prof.pk},
            'prestacion': {"id": pres.pk},
            'paciente': {"id": paciente.pk}
        }
        response = self.client.put('/practicas/turno/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['start'],datetime.datetime.now().strftime('%H:%M:%S'))
        self.assertEqual(response.json()['end'],(datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'))
        self.assertEqual(response.json()['taken'],True)
        self.assertEqual(response.json()['profesional']['id'],prof.pk)
        self.assertEqual(response.json()['prestacion']['id'],pres.pk)
        self.assertEqual(response.json()['paciente']['id'],paciente.pk)

class AusenciaTest(APITestCase):

    def test_createAusencia(self):
        """
        Asegura crear una Ausencia
        :return:
        """
        helper = GatewayTestHelper()
        profesional = helper.createProfesional()
        prestacion = helper.createPrestacion()
        profesional.prestaciones.add(prestacion)
        profesional.save()
        turno = helper.createTurno(start=datetime.time(10, 0, 0), end=datetime.time(10, 30, 0), profesional=profesional,
                                   prestacion=prestacion)
        turno.day=datetime.date(2016,12,02)
        turno.status = Turno.STATUS_ACTIVE
        turno.save()

        start_date = datetime.date(2016,12,01)
        end_date = datetime.date(2016,12,05)
        data= {
            'start_day': start_date.strftime('%Y-%m-%d'),
            'end_day': end_date.strftime('%Y-%m-%d'),
            'profesional': {"id":1},
            'reason': 'Se enfermo',
            'notes': 'De gripe'
        }
        response = self.client.post('/practicas/ausencia/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        Turnos = Turno.objects.filter(day=turno.day, profesional=profesional)

        self.assertEqual(Ausencia.objects.count(), 1)
        self.assertEqual(Turnos[0].status, Turno.STATUS_INACTIVE)

    def test_getAusencias(self):
        """
        Obtiene todas las ausencias
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAusencia()
        response = self.client.get('/practicas/ausencia/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAusencia(self):
        """
        Obtiene una ausencia
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAusencia()
        response = self.client.get('/practicas/ausencia/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAusenciaFiltered(self):
        """
        Obtiene una ausencia filtrada por profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAusencia()
        response = self.client.get('/practicas/ausencia/?profesional=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteAusencia(self):
        """
        Elimina una Ausencia
        :return:
        """
        helper = GatewayTestHelper()
        profesional = helper.createProfesional()
        prestacion = helper.createPrestacion()
        profesional.prestaciones.add(prestacion)
        profesional.save()
        turno = helper.createTurno(start = datetime.time(10,0,0), end=datetime.time(10,30,0),profesional=profesional, prestacion=prestacion)
        turno.status=Turno.STATUS_INACTIVE #Lo inactivo para simular ausencia
        ausencia = helper.createAusencia()
        ausencia.profesional = profesional
        ausencia.start_day = turno.day
        ausencia.end_day = turno.day
        ausencia.save()
        day = turno.day

        response = self.client.delete('/practicas/ausencia/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        Turnos = Turno.objects.filter(day=day, profesional=profesional)

        self.assertEqual(Ausencia.objects.count(),0)
        self.assertEqual(Turnos[0].status, Turno.STATUS_ACTIVE)

    def test_updateAusencia(self):
        """
        Modifica una Ausencia
        :return:
        """
        helper = GatewayTestHelper()
        prof = helper.createProfesional()
        turno=helper.createTurno(profesional=prof)

        data= {
            'start_day': turno.day.strftime('%Y-%m-%d'),
            'end_day': (turno.day+datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            'profesional': {"id":prof.pk},
            'notes':'Notitas',
            'reason':'Razon'
        }
        response = self.client.put('/practicas/turno/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GatewayTestHelper():
    def createAusencia(self, start=datetime.datetime.now(), end=datetime.datetime.now() + datetime.timedelta(hours=4),
                    profesional=None):
        prof = profesional if profesional is not None else self.createProfesional()

        instance = Ausencia.objects.create(
            start_day=datetime.date.today(),
            end_day=datetime.date.today()+datetime.timedelta(days=1),
            profesional=prof,
            reason='se enfermo',
            notes='notitas',
            status=Ausencia.STATUS_ACTIVE
        )
        return instance

    def createTurno(self, start=datetime.datetime.now(), end=datetime.datetime.now()+datetime.timedelta(hours=4), profesional=None, prestacion=None, paciente=None):
        prof = profesional if profesional is not None else self.createProfesional()
        pres = prestacion if prestacion is not None else self.createPrestacion()
        pasHelper = PacienteTestHelper()
        pac = paciente if paciente is not None else pasHelper.createPaciente()
        instance = Turno.objects.create(
            day=datetime.date.today(),
            start = start,
            end = end,
            taken=False,
            profesional=prof,
            prestacion=pres,
            paciente=pac
        )
        return instance

    def createAgenda(self):
        prof = self.createProfesional()
        pres = self.createPrestacion()
        agenda = Agenda.objects.create(
            status='Active',
            start = datetime.datetime.now(),
            end = datetime.datetime.now()+datetime.timedelta(hours=4),
            validFrom = datetime.date.today(),
            validTo = datetime.date.today()+datetime.timedelta(days=3),
            profesional = prof,
            prestacion = pres
        )
        dow = self.createDayOfWeek()
        period = Period.objects.create(
            start=agenda.start,
            end=agenda.end,
            selected=True
        )
        period.daysOfWeek.add(dow)
        agenda.periods.add(period)
        return agenda

    def createAgendaConTurno(self, profesional=None, prestacion=None, start=datetime.datetime.now(), end=datetime.datetime.now()+datetime.timedelta(hours=2)):
        prof = profesional if profesional is not None else self.createProfesional()
        pres = prestacion if prestacion is not None else self.createPrestacion()
        start = start
        end = end
        agenda = Agenda.objects.create(
            status='Active',
            start = start,
            end = end,
            validFrom = datetime.date.today(),
            validTo = datetime.date.today()+datetime.timedelta(days=3),
            profesional = prof,
            prestacion = pres
        )
        dow1=self.createDayOfWeek(index=0, name="Lunes", selected=True)
        period = Period.objects.create(
            start = start,
            end = start+datetime.timedelta(hours=1),
            selected = True
        )
        period.daysOfWeek.add(dow1)
        dow2 = self.createDayOfWeek(index=1, name="Martes", selected=True)
        period.daysOfWeek.add(dow2)
        agenda.periods.add(period)

        period = Period.objects.create(
            start=start + datetime.timedelta(hours=1),
            end=start + datetime.timedelta(hours=2),
            selected=True
        )
        period.daysOfWeek.add(dow1)
        period.daysOfWeek.add(dow2)

        agenda.periods.add(period)
        agenda.save()
        self.createTurno(start,start+datetime.timedelta(hours=1), prof, pres)
        self.createTurno(start + datetime.timedelta(hours=1), start + datetime.timedelta(hours=2), prof, pres)

        return agenda

    def createProfesional(self):
        cth = CommonTestHelper()
        dt=cth.createDocumentType()
        st=cth.createSexType()
        loc= cth.createLocation()
        cs=cth.createCivilStatus()
        et=cth.createEducationType()
        ss=cth.createSocialService()

        profesional = Paciente.objects.create(
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

        return profesional

    def createPeriod(self):
        dow=self.createDayOfWeek()
        period = Period.objects.create(
            start = datetime.datetime.now(),
            end = datetime.datetime.now()+datetime.timedelta(minutes=30),
            selected = False
        )
        period.daysOfWeek.add(dow)
        return period

    def createDayOfWeek(self, index=0, name="Lunes", selected=True):
        dow = DayOfWeek.objects.create(
            index=index,
            name=name,
            selected=selected
        )
        return dow

    def createEspecialidad(self):
        especialidad = Especialidad.objects.create(
            name = 'Pediatria',
            description = 'Especialidad dedicada a menores de 15 anos',
            status = Especialidad.STATUS_ACTIVE,
        )
        return especialidad

    def createPrestacion(self):
        especialidad = self.createEspecialidad()
        prestacion = Prestacion.objects.create(
            name = 'Consulta infectologia',
            description = 'Consulta infectologia',
            duration = 20,
            status = Prestacion.STATUS_ACTIVE,
            default=False,
            notes = 'Consulta infectologia',
            especialidad = especialidad
        )
        return prestacion

    def createProfesional(self):
        prestacion = self.createPrestacion()
        profesional = Profesional.objects.create(
            firstName = 'Cacho',
            otherNames = 'Ruben Adolfo',
            fatherSurname = 'Castana',
            motherSurname = 'De los Limones',
            birthDate = datetime.date(1942,6,11)
        )
        profesional.prestaciones.add(prestacion)
        profesional.save()

        return profesional