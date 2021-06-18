import argparse
import re
from sketchstyler.utils import list_palettes, load_img, save_img, load_palettes, save_palette, remove_palette, load_palette
from sketchstyler.colors import rgb2

ap = argparse.ArgumentParser(description='Replace red, green, and blue pixels with alternatives')

ap.add_argument("-i", "--input", type=str, help="input file.")
ap.add_argument("-o", "--output", type=str,default='output', help="output file.")
ap.add_argument("-l", "--list", action='store_true', help="list available palettes.")
ap.add_argument("-s", "--save", type=str, help="save a palette as SAVE.")
ap.add_argument("-rm", "--remove", type=str, help="remove the palette REMOVE")
ap.add_argument("-r", "--red", type=str, help="rgb color that replaces red")
ap.add_argument("-g", "--green", type=str, help="rgb color that replaces green")
ap.add_argument("-b", "--blue", type=str, help="rgb color that replaces blue")
ap.add_argument("-p", "--palette", type=str, help="use existing palette.")

args = vars(ap.parse_args())

''' Help functions '''
def parse_rgb(string):
    '''Returns None or the rgb values as a list of ints.'''
    if string == None:
        return None
        
    p = re.compile('[0-9]+')
    rgbs = [int(value) for value in p.findall(string)]
    if max(rgbs) > 255 or min(rgbs) < 0 or len(rgbs) != 3:
        print(f'invalid rgb argument {string} will be ignored.')
        return None
    else:
        return rgbs
        
        
''' Listing palettes '''
if args['list']:
    for palette in load_palettes().items():
        print(palette)
    quit()

''' Remove palette '''
to_be_removed = args['remove']
if to_be_removed != None:
    remove_palette(to_be_removed)
    quit()


''' Load colors '''
palette_to_be_used = args['palette']
if palette_to_be_used != None:
    colors = load_palette(palette_to_be_used)
elif args['red'] != None or args['green'] != None or args['blue'] != None:
    colors = []
    for c in ['red', 'green', 'blue']:
        colors.append(parse_rgb(args[c]))
else:
    colors = load_palette('default')


''' Save palette '''      
save_as = args['save']
if save_as != None:

    if save_as in load_palettes().keys(): # name already in use
        print(f"Do you want to overwrite palette saved as '{save_as}'?")
        answer = input('(yes or no) > ')
        confirmed = answer.lower() in ['y', 'yes']
    else:
        confirmed = True # name is not in use
    
    if confirmed:
        print(f"Saved current pallet as '{save_as}'")
        save_palette(colors, save_as)
    else:
        print(f"Did not save the pallete.")
 
''' Transform image '''
input_file = args['input']
if input_file != None:
    img = load_img(input_file)
    adjusted_img = rgb2(img, *colors)
    output_file = args['output']
    if output_file.split('.')[-1] != 'png':
        output_file += '.png'
    
    save_img(output_file, adjusted_img)
 
    
    