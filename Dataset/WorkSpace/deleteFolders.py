import os
import shutil

# List of folder codes to delete
folders_to_delete = [
    '001', '002', '005', '006', '007', '011', '015', '016', '019', '024', '025',
    '027', '030', '032', '035', '037', '039', '040', '041', '042', '043', '047',
    '050', '052', '053', '055', '056', '057', '059', '060', '061', '062', '063',
    '064', '065', '068', '069', '071', '074', '075', '079', '080', '082', '089',
    '096', '097', '098', '101', '111', '113', '114', '115', '116', '117', '118',
    '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129',
    '131', '132', '133', '136', '137', '138', '139', '141', '143', '146', '147',
    '150', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161',
    '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172',
    '173', '174', '175', '176', '177', '178', '179', '180', '181', '183', '187',
    '189', '190', '191', '192', '193', '194', '195', '196', '197', '198'
]

# Parent directory containing the folders
parent_dir = r"C:\Users\meghp\Desktop\Ahmedabad University\Term 1\Artificial Intelligence Lab\Bird Species Detection\Dataset\Working Dataset\images"

# Loop through all folders in the directory
for folder in os.listdir(parent_dir):
    folder_path = os.path.join(parent_dir, folder)
    
    if os.path.isdir(folder_path):
        # Extract the first 3 characters (folder code)
        folder_code = folder.split('.')[0]
        
        if folder_code in folders_to_delete:
            shutil.rmtree(folder_path)  # delete folder and contents
            print(f"Deleted: {folder}")
        else:
            print(f"Kept: {folder}")