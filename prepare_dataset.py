import os
import shutil

source_folder = "UTKFace"

male_folder = "dataset/male"
female_folder = "dataset/female"

os.makedirs(male_folder, exist_ok=True)
os.makedirs(female_folder, exist_ok=True)

for file in os.listdir(source_folder):

    try:
        gender = file.split("_")[1]

        if gender == "0":
            shutil.copy(
                os.path.join(source_folder,file),
                male_folder
            )

        elif gender == "1":
            shutil.copy(
                os.path.join(source_folder,file),
                female_folder
            )

    except:
        pass

print("Dataset Organized")