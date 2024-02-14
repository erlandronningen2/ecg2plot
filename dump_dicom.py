import datetime
import pydicom
import matplotlib.pyplot as plt
#@Erland Rønningen
#..\Python\Python310\PYTHON.EXE ..\dump_dicom.py


def logg(mld):
    print(datetime.datetime.now(), mld)

def fil_logg(mld):
    f = open("dump_dicom.log", "a")
    f.write(datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + " --> " + mld + "\n")
    f.close()

if __name__ == '__main__':
    logg('Program starter...')
    logg(pydicom.__version__)
    from pydicom import dcmread
    ds = dcmread("../OB000001.dcm")
    print(ds)
    #print("Modalitet" + ds.Modality)
    #print("Accession Number " + ds.AccessionNumber)
    #logg("Study date " + ds.StudyDate)
    #logg(ds.InstanceCreationDate)                       
    #print("StudyInstanceUID " + ds.StudyInstanceUID)   
    #print("SeriesInstanceUID " + ds.SeriesInstanceUID)
    #print("Pasient navn " + ds.PatientName)
    #print("Pasient fødsel " + ds.PatientBirthDate)
    #print("")
    #print(dir(ds))
    #print(dir(ds.StudyDescription))
    #sopidobj = ds[0X0008, 0X0018]
    #testobj = ds[0x0040, 0xa730]
    #sopident = sopidobj.value
    #person_obj = ds[0x0010, 0x0020]
    #studyid_obj = ds[0X0008, 0X0018]
    #studydate_obj = ds[0X0008, 0X0020]
    #seriesdesc_obj = ds[0X0008, 0X103e]
    #person_id = person_obj.value
    #study_id = studyid_obj.value
    #study_date = studydate_obj.value
    #series_desc = seriesdesc_obj.value
    #logg(study_id + "," + person_id + "," + study_date + "," + series_desc)
    #logg(sopident) 
    #fil_logg(sopident)
    #person_obj = ds[0x0010, 0x0020]
    #studyid_obj = ds[0X0008, 0X0018]
    #studydate_obj = ds[0X0008, 0X0020]
    #seriesdesc_obj = ds[0X0008, 0X103e]
    #person_id = person_obj.value
    #study_id = studyid_obj.value
    #study_date = studydate_obj.value
    #series_desc = seriesdesc_obj.value
    #print("Person nr " + person_id)
    #print("Study ID " + study_id)
    #print("Study dato " + study_date)
    #print("Series beskrivelse " + series_desc)
    logg('Program stopper...')