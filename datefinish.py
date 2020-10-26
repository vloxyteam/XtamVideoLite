import subprocess 

def get_duration(file):
    """Get the duration of a video using ffprobe."""
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(file)
    output = subprocess.check_output(
        cmd,
        shell=True, # Let this run in the shell
        stderr=subprocess.STDOUT
    )
    # return round(float(output))  # ugly, but rounds your seconds up or down
    return float(output)
