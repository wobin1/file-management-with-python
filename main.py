import shutil, os


def file_manager(file_source_dir, file_destination_dir):
    source_dir = file_source_dir
    destination_dir = file_destination_dir


    file_names = os.listdir(source_dir)

    for file_name in file_names:
        if os.path.join(source_dir, file_name).endswith('.mp3'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'audios'))

        if os.path.join(source_dir, file_name).endswith('.mp4'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'videos'))

        if os.path.join(source_dir, file_name).endswith('.zip'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'zip'))

        if os.path.join(source_dir, file_name).endswith('.geojson'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'geojson'))

        if os.path.join(source_dir, file_name).endswith('.pdf'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pdf'))

        if os.path.join(source_dir, file_name).endswith('.jpg'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pictures'))

        if os.path.join(source_dir, file_name).endswith('.png'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pictures'))

        print("success!!!!!")



file_manager('C:\\Users\\User\\Downloads', 'C:\\Users\\User\\Downloads')