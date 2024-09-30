import opensim as osim
import xml.etree.ElementTree as ET
import os

file_address=r'input_your_.trc_address'
body_Mass=['input_your_subject_mass']
scale_xml_name='scale_tool.xml'
model_name='gait2392_simbody.osim'




def get_file_paths_with_extension(folder_path, file_extension):
    all_files = os.listdir(folder_path)
    specific_files = [f for f in all_files if f.endswith(file_extension)]
    file_paths = [os.path.join(folder_path, f) for f in specific_files]
    return file_paths


folder_path = file_address
file_extension = '.trc'
file_paths = get_file_paths_with_extension(folder_path, file_extension)
file_paths = [item.replace('\\', '/') for item in file_paths]
print(f'文件读取成功,共{len(file_paths)}个文件,正在处理中....')
print(file_paths)



for i in range(len(file_paths)):
    tree = ET.parse(scale_xml_name)
    root = tree.getroot()
    for marker_file in root.findall('.//marker_file'):
        marker_file.text = file_address+f'/{i}.trc'
    for marker_file in root.findall('.//output_model_file'):
        marker_file.text = f'{i}.osim'
    for marker_file in root.findall('.//mass'):
        marker_file.text = f'{body_Mass[i]}'
    tree.write(scale_xml_name)

    scaleTool = osim.ScaleTool(scale_xml_name)
    scaleTool.getGenericModelMaker().setModelFileName(model_name)
    a=scaleTool.run()


