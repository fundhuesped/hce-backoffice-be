#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_hce import views

app_name = "hc_hce"
urlpatterns = [
    url(r'^visit/(?P<pk>[0-9]+)/$', views.VisitDetails.as_view(), name='Visit-detail'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/visits$', views.PacienteVisitList.as_view(), name='Paciente-Visit-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/hivChart$', views.PatientHIVChart.as_view(), name='Paciente-HIV-Chart'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/currentVisit$', views.CurrentVisitDetail.as_view(), name='Current-Visit-detail'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/problems$', views.PatientProblemsList.as_view(), name='Patient-Problems-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/medications$', views.PatientMedicationsList.as_view(), name='Patient-Medications-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/arvTreatments$', views.PatientARVTreartmentsList.as_view(), name='Patient-Medications-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/familyProblems$', views.PatientFamilyHistoryProblemsList.as_view(), name='Patient-Family-History-Problems-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/vaccines$', views.PatientVaccineList.as_view(), name='Patient-Vaccines-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/patientPrescriptions$', views.PatientPrescriptionList.as_view(), name='Patient-Prescription-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/patientVacinePrescriptions$', views.PatientVaccinePrescriptionList.as_view(), name='Patient-Vaccine-Prescription-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/clinicalStudyResults$', views.PatientClinicalStudyResultList.as_view(), name='Patient-ClinicalStudyResult-list'),
    url(r'^patientProblem/(?P<pk>[0-9]+)/$', views.PatientProblemDetail.as_view(), name='Patient-Problem-detail'),
    url(r'^patientArvTreatment/(?P<pk>[0-9]+)/$', views.PatientARVTreatmentDetail.as_view(), name='Patient-ARVTreatment-detail'),
    url(r'^familyProblem/(?P<pk>[0-9]+)/$', views.PatientFamilyHistoryProblemDetail.as_view(), name='Patient-Family-History-Problems-detail'),
    url(r'^patientVaccine/(?P<pk>[0-9]+)/$', views.PatientVaccineDetail.as_view(), name='Patient-Vaccine-detail'),
    url(r'^patientMedication/(?P<pk>[0-9]+)/$', views.PatientMedicationDetail.as_view(), name='Patient-Medication-detail'),
    url(r'^patientClinicalStudyResult/(?P<pk>[0-9]+)/$', views.PatientClinicalStudyResultDetail.as_view(), name='Patient-ClinicalStudyResult-detail'),
    url(r'^patientPrescriptions/(?P<pk>[0-9]+)$', views.PatientPrescriptionDetail.as_view(), name='Patient-Prescription-detail'),
    url(r'^patientARVPrescriptions/(?P<pk>[0-9]+)$', views.PatientARVPrescriptionDetail.as_view(), name='Patient-Prescription-detail'),
    url(r'^patientVaccinePrescriptions/(?P<pk>[0-9]+)$', views.PatientVaccinePrescriptionDetail.as_view(), name='Patient-Vaccine-Prescription-detail'),

]
