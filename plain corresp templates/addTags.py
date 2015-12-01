"""simple script to add start and end tags to list of items"""
import os



def add_tags(strg):
    strg = ''.join(strg.split('#'))
    strg = ''.join(strg.split('.'))
    strg = ''.join(strg.split("'"))
    lst = strg.split('\n')
    
    return '<value>#' + '</value>\n<value>#'.join(lst) + '</value>'

if __name__ == '__main__':
    f_name = 'place_ids.txt'
    cwd = os.getcwd()
    f_path = cwd + os.sep + f_name
    f_opath = cwd +os.sep + 'out_places.txt'

    with open(f_path, 'r') as f:
        strg = f.read()

    out_strg = add_tags(strg)

    with open(f_opath, 'w') as f:
        f.write(out_strg)
    
    print('finished!')
    
    
