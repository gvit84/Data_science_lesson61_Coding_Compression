import gzip

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            f_out.writelines(f_in)

input_file = 'Garri-Pottier_task_2.txt'
output_file = 'compressed_task_2.gz'

compress_file(input_file, output_file)
