import os

output_dir = 'public'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

os.system('site.py')

print("Build completed!")
