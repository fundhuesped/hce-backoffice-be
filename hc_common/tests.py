#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_common.models import CivilStatusType, Province, District, DocumentType, EducationType, Location, SexType, SocialService
from rest_framework import status

class LocationTest(APITestCase):
    def test_createLocation(self):
        """
        Asegura crear una location
        :return:
        """
        testh = CommonTestHelper()
        testh.createDistrict()

        data= {
            'name': 'District',
            'description': 'Districto nuevo',
            'status': 'Active',
            'district': {
                'id':1
            }
        }
        response = self.client.post('/comun/location/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(),1)

    def test_getLocationss(self):
        """
        Obtiene todos los Location
        :return:
        """
        helper = CommonTestHelper()
        helper.createLocation()
        response = self.client.get('/comun/location/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getLocation(self):
        """
        Obtiene un Location
        :return:
        """
        helper = CommonTestHelper()
        helper.createLocation()
        response = self.client.get('/comun/location/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteLocation(self):
        """
        Elinima un Location
        :return:
        """
        helper = CommonTestHelper()
        helper.createLocation()
        response = self.client.delete('/comun/location/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Location.objects.count(),0)

    def test_updateLocation(self):
        """
        Modifica un Location
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createLocation()
        helperp.createDistrict()

        data= {
            'name': 'DA',
            'description': 'Districto 2',
            'status': 'Inactive',
            'district': {
                'id': 2
            }
        }
        response = self.client.put('/comun/location/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'DA')
        self.assertEqual(response.json()['description'],'Districto 2')
        self.assertEqual(response.json()['status'],'Inactive')
        self.assertEqual(response.json()['district']['id'],2)


class EducationTypeTest(APITestCase):
    def test_createEducationType(self):
        """
        Asegura crear un tipo de educacion
        :return:
        """

        data= {
            'name': 'UNI',
            'description': 'Universitario',
            'status': 'Active'
        }
        response = self.client.post('/comun/educationType/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationType.objects.count(),1)

    def test_getEducationTypes(self):
        """
        Obtiene todos los Tipos de Educacion
        :return:
        """
        helper = CommonTestHelper()
        helper.createEducationType()
        response = self.client.get('/comun/educationType/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getEducationType(self):
        """
        Obtiene un Tipo de educacion
        :return:
        """
        helper = CommonTestHelper()
        helper.createEducationType()
        response = self.client.get('/comun/educationType/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteEducationType(self):
        """
        Elinima un Tipo de educacion
        :return:
        """
        helper = CommonTestHelper()
        helper.createEducationType()
        response = self.client.delete('/comun/educationType/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EducationType.objects.count(),0)

    def test_updateEducationType(self):
        """
        Modifica un Tipo de educacion
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createEducationType()

        data= {
            'name': 'SEC',
            'description': 'Secundaria',
            'status': 'Inactive'
        }
        response = self.client.put('/comun/educationType/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'SEC')
        self.assertEqual(response.json()['description'],'Secundaria')
        self.assertEqual(response.json()['status'],'Inactive')


class SocialServiceTest(APITestCase):
    def test_createSocialService(self):
        """
        Asegura crear un servicio social
        :return:
        """

        data= {
            'name': 'PAMI',
            'description': 'Obra social del estado',
            'status': 'Active'
        }
        response = self.client.post('/comun/socialService/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialService.objects.count(),1)

    def test_getSocialServices(self):
        """
        Obtiene todos los Servicios Sociales
        :return:
        """
        helper = CommonTestHelper()
        helper.createSexType()
        response = self.client.get('/comun/socialService/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getSocialService(self):
        """
        Obtiene un Servicio Social
        :return:
        """
        helper = CommonTestHelper()
        helper.createSocialService()
        response = self.client.get('/comun/socialService/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteSocialService(self):
        """
        Elinima un Servicio Social
        :return:
        """
        helper = CommonTestHelper()
        helper.createSocialService()
        response = self.client.delete('/comun/socialService/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SocialService.objects.count(),0)

    def test_updateSocialService(self):
        """
        Modifica un Servicio Social
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createSocialService()

        data= {
            'name': 'OSECAC',
            'description': 'Comercio',
            'status': 'Inactive'
        }
        response = self.client.put('/comun/socialService/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'OSECAC')
        self.assertEqual(response.json()['description'],'Comercio')
        self.assertEqual(response.json()['status'],'Inactive')


class SexTypeTest(APITestCase):
    def test_createSexType(self):
        """
        Asegura crear un tipo de sexo
        :return:
        """

        data= {
            'name': 'MASC',
            'description': 'Masculino',
            'status': 'Active'
        }
        response = self.client.post('/comun/sexType/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SexType.objects.count(),1)

    def test_getSexTypes(self):
        """
        Obtiene todos los Tipos de Sexo
        :return:
        """
        helper = CommonTestHelper()
        helper.createSexType()
        response = self.client.get('/comun/sexType/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getSexType(self):
        """
        Obtiene un Tipo de sexo
        :return:
        """
        helper = CommonTestHelper()
        helper.createSexType()
        response = self.client.get('/comun/sexType/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteSexType(self):
        """
        Elinima un Tipo de sexo
        :return:
        """
        helper = CommonTestHelper()
        helper.createSexType()
        response = self.client.delete('/comun/sexType/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SexType.objects.count(),0)

    def test_updateSexType(self):
        """
        Modifica un Tipo de sexo
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createSexType()

        data= {
            'name': 'FEM',
            'description': 'Femenino',
            'status': 'Inactive'
        }
        response = self.client.put('/comun/sexType/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'FEM')
        self.assertEqual(response.json()['description'],'Femenino')
        self.assertEqual(response.json()['status'],'Inactive')


class DocumentTypeTest(APITestCase):
    def test_createDocumentType(self):
        """
        Asegura crear un tipo de documento
        :return:
        """

        data= {
            'name': 'PAS',
            'description': 'Pasaporte',
            'status': 'Active'
        }
        response = self.client.post('/comun/documentType/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DocumentType.objects.count(),1)

    def test_getDocumentTypes(self):
        """
        Obtiene todos los Tipos de documento
        :return:
        """
        helper = CommonTestHelper()
        helper.createDocumentType()
        response = self.client.get('/comun/documentType/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getDocumentType(self):
        """
        Obtiene un Tipo de documento
        :return:
        """
        helper = CommonTestHelper()
        helper.createDocumentType()
        response = self.client.get('/comun/documentType/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteDocumentType(self):
        """
        Elinima un Tipo de documento
        :return:
        """
        helper = CommonTestHelper()
        helper.createDocumentType()
        response = self.client.delete('/comun/documentType/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DocumentType.objects.count(),0)

    def test_updateDocumentType(self):
        """
        Modifica un Tipo de documento
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createDocumentType()

        data= {
            'name': 'DNI',
            'description': 'Documento',
            'status': 'Inactive'
        }
        response = self.client.put('/comun/documentType/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'DNI')
        self.assertEqual(response.json()['description'],'Documento')
        self.assertEqual(response.json()['status'],'Inactive')


class CivilStatusTest(APITestCase):
    def test_createCivilStatus(self):
        """
        Asegura crear un estado civil
        :return:
        """

        data= {
            'name': 'Casado',
            'description': 'Estado casado',
            'status': 'Active'
        }
        response = self.client.post('/comun/civilStatusType/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CivilStatusType.objects.count(),1)

    def test_getCivilStatus(self):
        """
        Obtiene todos los Estados civiles
        :return:
        """
        helper = CommonTestHelper()
        helper.createCivilStatus()
        response = self.client.get('/comun/civilStatusType/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getCivilStatus(self):
        """
        Obtiene un Estado Civil
        :return:
        """
        helper = CommonTestHelper()
        helper.createCivilStatus()
        response = self.client.get('/comun/civilStatusType/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteCivilStatus(self):
        """
        Elinima un Estado Civil
        :return:
        """
        helper = CommonTestHelper()
        helper.createCivilStatus()
        response = self.client.delete('/comun/civilStatusType/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CivilStatusType.objects.count(),0)

    def test_updateCivilStatus(self):
        """
        Modifica un Estado Civil
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createCivilStatus()

        data= {
            'name': 'Soltero',
            'description': 'Estado soltero',
            'status': 'Inactive'
        }
        response = self.client.put('/comun/civilStatusType/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Soltero')
        self.assertEqual(response.json()['description'],'Estado soltero')
        self.assertEqual(response.json()['status'],'Inactive')


class DistrictTest(APITestCase):
    def test_createDistrict(self):
        """
        Asegura crear un districto
        :return:
        """
        testh = CommonTestHelper()
        testh.createProvince()

        data= {
            'name': 'San Martin',
            'description': 'Partido de San Martin',
            'status': 'Active',
            'province': {
                'id': 1
            }
        }
        response = self.client.post('/comun/district/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(District.objects.count(),1)

    def test_getDistricts(self):
        """
        Obtiene todos los districtos
        :return:
        """
        helper = CommonTestHelper()
        helper.createDistrict()
        response = self.client.get('/comun/district/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getDistrict(self):
        """
        Obtiene un Districto
        :return:
        """
        helper = CommonTestHelper()
        helper.createDistrict()
        response = self.client.get('/comun/district/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteDistrict(self):
        """
        Elinima un Districto
        :return:
        """
        helper = CommonTestHelper()
        helper.createDistrict()
        response = self.client.delete('/comun/district/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(District.objects.count(),0)

    def test_updateDistrict(self):
        """
        Modifica un District
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createDistrict()
        helperp.createProvince()

        data= {
            'name': 'Caseros',
            'description': 'Partido de caseros',
            'status': 'Inactive',
            'province': {
                'id': 2
            }
        }
        response = self.client.put('/comun/district/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Caseros')
        self.assertEqual(response.json()['description'],'Partido de caseros')
        self.assertEqual(response.json()['status'],'Inactive')
        self.assertEqual(response.json()['province']['id'],2)


class ProvinceTest(APITestCase):
    def test_createProvince(self):
        """
        Asegura crear una provincia
        :return:
        """

        data= {
            'name': 'Cordoba',
            'description': 'Provincia de Cordiba',
            'status': 'Active'
        }
        response = self.client.post('/comun/province/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Province.objects.count(),1)

    def test_getProvinces(self):
        """
        Obtiene todas las Provincias
        :return:
        """
        helper = CommonTestHelper()
        helper.createProvince()
        response = self.client.get('/comun/province/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getProvince(self):
        """
        Obtiene una Provincia
        :return:
        """
        helper = CommonTestHelper()
        helper.createProvince()
        response = self.client.get('/comun/province/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteProvince(self):
        """
        Elinima una Provincia
        :return:
        """
        helper = CommonTestHelper()
        helper.createProvince()
        response = self.client.delete('/comun/province/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Province.objects.count(),0)

    def test_updateProvince(self):
        """
        Modifica una Provincia
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createProvince()

        data= {
            'name': 'Santa Fe',
            'description': 'Prov de Santa Fe',
            'status': 'Inactive'
        }
        response = self.client.put('/comun/province/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Santa Fe')
        self.assertEqual(response.json()['description'],'Prov de Santa Fe')
        self.assertEqual(response.json()['status'],'Inactive')


class CommonTestHelper():

    def createLocation(self):
        district = self.createDistrict()
        location = Location.objects.create(
            name='Districto A',
            description='Nuevo districto',
            status='Active',
            district=district
        )
        return location

    def createSocialService(self):
        socs = SocialService.objects.create(
            name = 'PAMI',
            description = 'Viejitos',
            status = 'Active'
        )
        return socs

    def createSexType(self):
        sexT = SexType.objects.create(
            name = 'MASC',
            description = 'Masculino',
            status = 'Active'
        )
        return sexT

    def createEducationType(self):
        eduT = EducationType.objects.create(
            name = 'UNI',
            description = 'Universitario',
            status = 'Active'
        )
        return eduT

    def createDocumentType(self):
        docT = DocumentType.objects.create(
            name = 'PAS',
            description = 'Pasaporte',
            status = 'Active'
        )
        return docT

    def createCivilStatus(self):
        civilStatus = CivilStatusType.objects.create(
            name = 'Casado',
            description = 'Estado casado',
            status = 'Active'
        )
        return civilStatus

    def createProvince(self):
        province = Province.objects.create(
            name = 'Cordoba',
            description = 'Provincia de Cordoba',
            status = 'Active'
        )
        return province

    def createDistrict(self):
        district = District.objects.create(
            name='San Martin',
            description='Partido de San Martin',
            status='Active',
            province=self.createProvince()
        )
        return district

