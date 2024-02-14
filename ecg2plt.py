import datetime
import pydicom
import matplotlib.pyplot as plt
import argparse

#   @Erland Rønningen
#   Usage ..\Programs\Python\Python310>python ..\ecg2plt.py --x <..\Dicom path>
#   Batch command...
#   FOR /F %G IN (ecg_joblist.txt) DO ..\PYTHON.EXE ..\ecg2plt.py --x %G
#   Testfile: ../ecg2plt/OB000001.dcm

def logg(mld):
    print(datetime.datetime.now(), mld)

def meta_output(data):
    f = open(outputfolder + "meta_output.csv", "a")
    f.write(data + "\n")
    f.close()

if __name__ == '__main__':
    logg('Program starts...')
    outputfolder = "../Documents/ecg2plt/"
        #read parameter from commandline, in this case the path to dicom file
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=str, required=False)
        #parser.add_argument('--y', type=str, required=False)
    args = parser.parse_args()
    dcm_input = args.x
    logg(dcm_input)
        #reads the dicom file
    from pydicom import dcmread
    from pydicom.fileset import FileSet
    from pydicom.waveforms import multiplex_array
    ds = dcmread(dcm_input)
    waveforms = ds.WaveformSequence
    multiplex = waveforms[0]
        # Read dicom meta info of interest
    patient_id = ds[0x0010, 0x0020].value
    instance_id = ds[0X0008, 0X0018].value
    instance_date = ds[0X0008, 0X0012].value
        #Output 
    job_id = datetime.datetime.now().strftime("%Y%m%d.%H%M%S.%f") 
    output_path = outputfolder + job_id + ".png"
    meta_output(job_id + "," + instance_date + "," + patient_id + "," + instance_id + "," + "label")
        #Drawing the ecg plot
    raw = multiplex_array(ds, 0, as_raw=True)
    newarr = ds.waveform_array(0)
    fig, axs = plt.subplots(6, 2)
    axs[0, 0].plot(newarr[:,0], linewidth=0.3)
    axs[0, 0].set_title(multiplex.ChannelDefinitionSequence[0].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[0, 0].axis('off')
    axs[1, 0].plot(newarr[:,1], linewidth=0.3)
    axs[1, 0].set_title(multiplex.ChannelDefinitionSequence[1].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[1, 0].axis('off')
    axs[2, 0].plot(newarr[:,2], linewidth=0.3)
    axs[2, 0].set_title(multiplex.ChannelDefinitionSequence[2].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[2, 0].axis('off')
    axs[3, 0].plot(newarr[:,3], linewidth=0.3)
    axs[3, 0].set_title(multiplex.ChannelDefinitionSequence[3].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[3, 0].axis('off')
    axs[4, 0].plot(newarr[:,4], linewidth=0.3)
    axs[4, 0].set_title(multiplex.ChannelDefinitionSequence[4].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[4, 0].axis('off')
    axs[5, 0].plot(newarr[:,5], linewidth=0.3)
    axs[5, 0].set_title(multiplex.ChannelDefinitionSequence[5].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[5, 0].axis('off')
    axs[0, 1].plot(newarr[:,6], linewidth=0.3)
    axs[0, 1].set_title(multiplex.ChannelDefinitionSequence[6].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[0, 1].axis('off')
    axs[1, 1].plot(newarr[:,7], linewidth=0.3)
    axs[1, 1].set_title(multiplex.ChannelDefinitionSequence[7].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[1, 1].axis('off')
    axs[2, 1].plot(newarr[:,8], linewidth=0.3)
    axs[2, 1].set_title(multiplex.ChannelDefinitionSequence[8].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[2, 1].axis('off')
    axs[3, 1].plot(newarr[:,9], linewidth=0.3)
    axs[3, 1].set_title(multiplex.ChannelDefinitionSequence[9].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[3, 1].axis('off')
    axs[4, 1].plot(newarr[:,10], linewidth=0.3)
    axs[4, 1].set_title(multiplex.ChannelDefinitionSequence[10].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[4, 1].axis('off')
    axs[5, 1].plot(newarr[:,11], linewidth=0.3)
    axs[5, 1].set_title(multiplex.ChannelDefinitionSequence[11].ChannelSourceSequence[0].CodeMeaning, fontsize=4, loc='left')
    axs[5, 1].axis('off')
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=600)
    logg('Program stops...')